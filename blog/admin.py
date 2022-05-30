from django.contrib import admin
from blog.models import Post,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title','author','status','published_date','created_date')
    list_filter = ['status','published_date']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','title')

admin.site.register(Category,CategoryAdmin)