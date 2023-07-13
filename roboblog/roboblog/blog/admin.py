from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Blog, Category


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = (
        'id',
        'title',
        'time_created',
        'photo',
        'is_published',
    )
    list_display_links = (
        'id',
        'title',
    )
    search_fields = (
        'title',
        'content'
    )
    list_filter = (
        'is_published',
        'time_created'
    )
    list_editable = (
        'is_published',
    )
    form = BlogAdminForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
