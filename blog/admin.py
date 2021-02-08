from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'content')
	prepopulated_fields = {'slug':('title',)}
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Post, PostAdmin)