from django.contrib import admin
from .models import Archive, ArchiveCaseRelative, BaseInfo, Cases, ClinicalInfo, Identity
# Register your models here.
admin.site.register(Archive)
admin.site.register(ArchiveCaseRelative)
admin.site.register(BaseInfo)
admin.site.register(Cases)
admin.site.register(ClinicalInfo)
admin.site.register(Identity)