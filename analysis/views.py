from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from .models import AnalysisSheet

class AnalysisSheetListView(View):
    def get(self, request, *args, **kwargs):
        analysis_sheets = AnalysisSheet.objects.all().values()
        return JsonResponse(list(analysis_sheets), safe=False)

class AnalysisSheetDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        analysis_sheet = get_object_or_404(AnalysisSheet, pk=pk)
        return JsonResponse({
            'id': analysis_sheet.id,
            'sheet_code': analysis_sheet.sheet_code,
            'sheet_name': analysis_sheet.sheet_name
        })

class AnalysisSheetCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        analysis_sheet = AnalysisSheet.objects.create(
            sheet_code=data.get('sheet_code'),
            sheet_name=data.get('sheet_name')
        )
        return JsonResponse({
            'id': analysis_sheet.id,
            'sheet_code': analysis_sheet.sheet_code,
            'sheet_name': analysis_sheet.sheet_name
        }, status=201)

class AnalysisSheetUpdateView(View):
    def post(self, request, pk, *args, **kwargs):
        analysis_sheet = get_object_or_404(AnalysisSheet, pk=pk)
        data = request.POST
        analysis_sheet.sheet_code = data.get('sheet_code')
        analysis_sheet.sheet_name = data.get('sheet_name')
        analysis_sheet.save()
        return JsonResponse({
            'id': analysis_sheet.id,
            'sheet_code': analysis_sheet.sheet_code,
            'sheet_name': analysis_sheet.sheet_name
        })

class AnalysisSheetDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        analysis_sheet = get_object_or_404(AnalysisSheet, pk=pk)
        analysis_sheet.delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=204)