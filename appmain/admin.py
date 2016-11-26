from django.contrib import admin

from .models import Person, Blog


class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('url',)
    list_filter = ('user',)


admin.site.register(Person)
admin.site.register(Blog, blogAdmin)