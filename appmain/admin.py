from django.contrib import admin

from .models import *


class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('url',)
    list_filter = ('user',)


admin.site.register(Person)
admin.site.register(css_crawl)
admin.site.register(Blog, blogAdmin)