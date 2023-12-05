from django.contrib import admin
from .models import JobPost, Location, Author,Skills

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','description','salary','expiry','date')
    list_filter = ('date','salary','expiry')
    search_fields = ('title','description')
    search_help_text = 'Write your queryset to search'
    #fields = (('title','description'),'expiry')
    #exclude = ('title',)
    fieldsets = (
        ('More Information', {
            'fields': ('title', 'description')
        }),
        ('More Information', {
            'classes': ('collapse',),
            'fields': (('salary','expiry'),'slug')
        }),
    )

admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)