from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date','status')
    empty_value_display = '-empty-'
    date_hierarchy = 'published_date'
    list_filter = ('title', 'created_date', 'published_date','status')
    search_fields = ('title', 'created_date', 'published_date','status')

admin.site.register(Post,PostAdmin)