from rest_framework import generics
from .models import Dictionary, DataTemplate, DataTemplateCategory
from .serializers import DictionarySerializer, DataTemplatesSerializer, DataTemplateCategorySerializer
import csv
import io
from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

# 自定义分页类
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

# -------------------------------
# 系统词条（Dictionary）的增删改查接口
# -------------------------------

class DictionaryListCreateView(generics.ListCreateAPIView):
    """
    获取所有词条 & 创建新词条
    GET: 查询所有词条
    POST: 创建新词条
    """
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    pagination_class = StandardResultsSetPagination

class DictionaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    获取、更新或删除指定 ID 的词条
    GET: 查询指定词条详情
    PUT/PATCH: 更新词条
    DELETE: 删除词条
    """
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

# -------------------------------
# 数据模板（DataTemplate）的增删改查接口
# -------------------------------

class DataTemplatesListCreateView(generics.ListCreateAPIView):
    """
    获取所有数据模板 & 创建新数据模板
    GET: 查询所有数据模板（自动联查关联的类别名称） 
    POST: 创建新数据模板
    """
    # 使用 select_related 优化外键关联查询，减少数据库查询次数
    queryset = DataTemplate.objects.select_related('category').all()
    serializer_class = DataTemplatesSerializer

class DataTemplatesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    获取、更新或删除指定 ID 的数据模板
    GET: 查询指定数据模板详情（包括关联的类别名称）
    PUT/PATCH: 更新数据模板
    DELETE: 删除数据模板
    """
    queryset = DataTemplate.objects.select_related('category').all()
    serializer_class = DataTemplatesSerializer
# -------------------------------
# 数据模板分类（DataTemplateCategory）的增删改查接口
# -------------------------------

class DataTemplateCategoryListCreateView(generics.ListCreateAPIView):
    """
    GET: 获取所有分类
    POST: 创建新分类
    """
    queryset = DataTemplateCategory.objects.all()
    serializer_class = DataTemplateCategorySerializer

class DataTemplateCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: 获取指定分类详情
    PUT/PATCH: 更新指定分类
    DELETE: 删除指定分类
    """
    queryset = DataTemplateCategory.objects.all()
    serializer_class = DataTemplateCategorySerializer

# -------------------------------
# CSV导入导出功能
# -------------------------------

@api_view(['GET'])
def dictionary_template_download(request):
    """提供词条导入模板下载"""
    # 创建CSV响应
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dictionary_import_template.csv"'
    
    # 创建CSV写入器
    writer = csv.writer(response)
    
    # 写入表头
    writer.writerow(['word_name', 'word_eng', 'word_short', 'word_code', 'word_class', 'word_apply', 'word_belong'])
    
    # 写入示例数据
    writer.writerow(['示例名称', 'Example', 'EX', 'EX001', '示例类型', '示例应用', ''])
    
    return response

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def dictionary_import(request):
    """处理词条批量导入"""
    if 'file' not in request.FILES:
        return Response({'error': '未找到上传文件'}, status=status.HTTP_400_BAD_REQUEST)
    
    csv_file = request.FILES['file']
    
    # 检查文件扩展名
    if not csv_file.name.endswith('.csv'):
        return Response({'error': '只支持CSV文件格式'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 解码CSV文件
    try:
        # 尝试使用不同编码读取文件
        try:
            csv_data = csv_file.read().decode('utf-8')
        except UnicodeDecodeError:
            # 如果UTF-8失败，尝试GBK（中文Windows常用）
            csv_file.seek(0)
            csv_data = csv_file.read().decode('gbk')
        
        reader = csv.DictReader(io.StringIO(csv_data))
        
        # 验证表头
        required_headers = ['word_name', 'word_eng', 'word_short', 'word_code', 'word_class', 'word_apply', 'word_belong']
        if not all(header in reader.fieldnames for header in required_headers):
            return Response({'error': 'CSV文件格式不正确，请使用提供的模板'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 计数器
        success_count = 0
        error_count = 0
        errors = []
        
        # 导入数据
        for i, row in enumerate(reader, start=2):  # 从2开始，表示CSV文件的第2行（考虑表头）
            try:
                # 检查必填字段
                if not row['word_name'] or not row['word_code'] or not row['word_class']:
                    errors.append(f"第{i}行：中文名称、词条编号和词条类型为必填项")
                    error_count += 1
                    continue
                
                # 检查词条编号是否已存在
                if Dictionary.objects.filter(word_code=row['word_code']).exists():
                    errors.append(f"第{i}行：词条编号 {row['word_code']} 已存在")
                    error_count += 1
                    continue
                
                # 创建新词条
                Dictionary.objects.create(
                    word_name=row['word_name'],
                    word_eng=row['word_eng'] or '',
                    word_short=row['word_short'] or '',
                    word_code=row['word_code'],
                    word_class=row['word_class'],
                    word_apply=row['word_apply'] or '',
                    word_belong=row['word_belong'] or ''
                )
                success_count += 1
                
            except Exception as e:
                errors.append(f"第{i}行：{str(e)}")
                error_count += 1
        
        # 返回导入结果
        return Response({
            'success': True,
            'message': f'导入完成：成功导入 {success_count} 条记录，失败 {error_count} 条记录',
            'errors': errors if errors else None
        })
        
    except Exception as e:
        return Response({'error': f'处理CSV文件时出错：{str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)