from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import DataTemplate, DataTemplateCategory, DataTemplateDetails, DataTemplateTags, DataTemplateTagsRelative, Dictionary

class DataTemplateListView(View):
    def get(self, request, *args, **kwargs):
        data_templates = DataTemplate.objects.all().values()
        return JsonResponse(list(data_templates), safe=False)

class DataTemplateDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        data_template = get_object_or_404(DataTemplate, pk=pk)
        return JsonResponse({
            'id': data_template.id,
            'name': data_template.name,
            'description': data_template.description,
            'category_id': data_template.category_id,
            'used_n': data_template.used_n
        })

class DataTemplateCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        data_template = DataTemplate.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            category_id=data.get('category_id'),
            used_n=data.get('used_n')
        )
        return JsonResponse({
            'id': data_template.id,
            'name': data_template.name,
            'description': data_template.description,
            'category_id': data_template.category_id,
            'used_n': data_template.used_n
        }, status=201)

class DataTemplateUpdateView(View):
    def post(self, request, pk, *args, **kwargs):
        data_template = get_object_or_404(DataTemplate, pk=pk)
        data = request.POST
        data_template.name = data.get('name')
        data_template.description = data.get('description')
        data_template.category_id = data.get('category_id')
        data_template.used_n = data.get('used_n')
        data_template.save()
        return JsonResponse({
            'id': data_template.id,
            'name': data_template.name,
            'description': data_template.description,
            'category_id': data_template.category_id,
            'used_n': data_template.used_n
        })

class DataTemplateDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        data_template = get_object_or_404(DataTemplate, pk=pk)
        data_template.delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=204)