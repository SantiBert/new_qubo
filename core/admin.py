from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Profile


class ProfileResourseces(resources.ModelResource):
    class Meta:
        model = Profile


class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['user']
    resource_class = ProfileResourseces


admin.site.register(Profile, ProfileAdmin)
