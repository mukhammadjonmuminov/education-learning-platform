from django.contrib import admin
from .models import Subject, Courses, Modul

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}

class ModuleInline(admin.StackedInline):
    model = Modul

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title', )}
    inlines = [ModuleInline]
