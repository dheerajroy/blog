from django.contrib import admin
from .models import Article

admin.site.register(Article)
admin.site.site_header = 'PlutoPe Blog Admin'
admin.site.site_title = 'PlutoPe Blog Admin Portal'
admin.site.index_title = f'Welcome to {admin.site.site_title}'
