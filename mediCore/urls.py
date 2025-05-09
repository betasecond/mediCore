"""
URL configuration for mediCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from analysis.views import (
    AnalysisSheetDetailView, AnalysisSheetListCreateView,

)
from data_templates.views import (
    DictionaryListCreateView, DictionaryDetailView, DataTemplatesListCreateView, DataTemplatesDetailView,
    DataTemplateCategoryListCreateView, DataTemplateCategoryDetailView,
    dictionary_template_download, dictionary_import  # 添加新的视图函数导入
)
from records.views import (
    DataTableListCreateView, DataTableDetailView, ExaminationImagesListCreateView, ExaminationImagesDetailView,
    ExaminationSheetListCreateView, ExaminationSheetDetailView, TestingSheetListCreateView, TestingSheetDetailView,
    DocumentChartListCreateView, DocumentChartDetailView, DocumentsListCreateView, DocumentsDetailView,
    ImageListCreateView, ImageDetailView, ShapeListCreateView, ShapeDetailView, TextListCreateView, TextDetailView
)
from patients.views import (
    ArchiveListCreateView, ArchiveDetailView, ArchiveCaseRelativeListCreateView, ArchiveCaseRelativeDetailView,
    BaseInfoListCreateView, BaseInfoDetailView, CasesListCreateView, CasesDetailView,
    ClinicalInfoListCreateView, ClinicalInfoDetailView, IdentityListCreateView, IdentityDetailView, GenderCountView,
    AgeDistributionView
)
schema_view = get_schema_view(
   openapi.Info(
      default_version="1.0",
      title="Your API",
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import RegisterView, LoginView

api_patterns = [
    path('analysis-sheet/', AnalysisSheetListCreateView.as_view(), name='analysis-sheet-create'),
    path('analysis-sheet/<int:pk>/', AnalysisSheetDetailView.as_view(), name='analysis-sheet-detail'),
    path('data-templates/', DataTemplatesListCreateView.as_view(), name='data-templates-list-create'),
    path('data-templates/<int:pk>/', DataTemplatesDetailView.as_view(), name='data-templates-detail'),
    path('categories/', DataTemplateCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', DataTemplateCategoryDetailView.as_view(), name='category-detail'),
    path('dictionary/', DictionaryListCreateView.as_view(), name='dictionary-list-create'),
    path('dictionary/<int:pk>/', DictionaryDetailView.as_view(), name='dictionary-detail'),
    # 添加词条CSV导入相关的路由
    path('dictionary/import-template/', dictionary_template_download, name='dictionary_template_download'),
    path('dictionary/import/', dictionary_import, name='dictionary_import'),
    
    path('data-tables/', DataTableListCreateView.as_view(), name='data_table_list_create'),
    path('data-tables/<int:pk>/', DataTableDetailView.as_view(), name='data_table_detail'),
    path('examination-images/', ExaminationImagesListCreateView.as_view(), name='examination_images_list_create'),
    path('examination-images/<int:pk>/', ExaminationImagesDetailView.as_view(), name='examination_images_detail'),
    path('examination-sheets/', ExaminationSheetListCreateView.as_view(), name='examination_sheet_list_create'),
    path('examination-sheets/<int:pk>/', ExaminationSheetDetailView.as_view(), name='examination_sheet_detail'),
    path('testing-sheets/', TestingSheetListCreateView.as_view(), name='testing_sheet_list_create'),
    path('testing-sheets/<int:pk>/', TestingSheetDetailView.as_view(), name='testing_sheet_detail'),
    path('document-charts/', DocumentChartListCreateView.as_view(), name='document_chart_list_create'),
    path('document-charts/<int:pk>/', DocumentChartDetailView.as_view(), name='document_chart_detail'),
    path('documents/', DocumentsListCreateView.as_view(), name='documents_list_create'),
    path('documents/<int:pk>/', DocumentsDetailView.as_view(), name='documents_detail'),
    path('images/', ImageListCreateView.as_view(), name='image_list_create'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('shapes/', ShapeListCreateView.as_view(), name='shape_list_create'),
    path('shapes/<int:pk>/', ShapeDetailView.as_view(), name='shape_detail'),
    path('texts/', TextListCreateView.as_view(), name='text_list_create'),
    path('texts/<int:pk>/', TextDetailView.as_view(), name='text_detail'),

    path('archives/', ArchiveListCreateView.as_view(), name='archive_list_create'),
    path('archives/<int:pk>/', ArchiveDetailView.as_view(), name='archive_detail'),
    path('archive-case-relatives/', ArchiveCaseRelativeListCreateView.as_view(), name='archive_case_relative_list_create'),
    path('archive-case-relatives/<int:pk>/', ArchiveCaseRelativeDetailView.as_view(), name='archive_case_relative_detail'),
    path('base-info/', BaseInfoListCreateView.as_view(), name='base_info_list_create'),
    path('base-info/<int:pk>/', BaseInfoDetailView.as_view(), name='base_info_detail'),
    path('cases/', CasesListCreateView.as_view(), name='cases_list_create'),
    path('cases/<int:pk>/', CasesDetailView.as_view(), name='cases_detail'),
    path('clinical-info/', ClinicalInfoListCreateView.as_view(), name='clinical_info_list_create'),
    path('clinical-info/<int:pk>/', ClinicalInfoDetailView.as_view(), name='clinical_info_detail'),
    path('identity/', IdentityListCreateView.as_view(), name='identity_list_create'),
    path('identity/<int:pk>/', IdentityDetailView.as_view(), name='identity_detail'),
    path('gender-count/', GenderCountView.as_view(), name='gender-count'),
    path('age-distribution/', AgeDistributionView.as_view(), name='age-distribution'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/?format=openapi', schema_view.without_ui(cache_timeout=0), name='schema-openapi'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('openapi.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # Add these to api_patterns
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]