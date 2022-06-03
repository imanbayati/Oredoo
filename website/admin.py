from django.contrib import admin
from website.models import Newsletter,Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
admin.site.register(Newsletter)
admin.site.register(Contact,ContactAdmin)