from django.contrib import admin

from .models import Search

admin.site.site_header = 'Soundplug Admin'
admin.site.site_title = 'Soundplug'
admin.site.index_header = 'Soundplug Admin'

admin.site.register(Search)