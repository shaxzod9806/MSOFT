from django.contrib import admin
from . import models

admin.site.register(models.Title)
admin.site.register(models.Sector)
admin.site.register(models.Work_experience)
admin.site.register(models.Citezenship)
admin.site.register(models.Language)


@admin.register(models.Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'first_name', 'last_name', 'email', 'phone', 'sector', 'work_experience',
        'spoken_languages', 'citizenship', 'prefer_project_duration', 'cv_file',
        'created_at', 'updated_at'
    )
    list_filter = ('created_at', 'updated_at', 'work_experience', 'citizenship', 'prefer_project_duration')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_per_page = 10
