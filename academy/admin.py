from django.contrib import admin
from .models import TokenProxy, TokenAdmin

admin.site.register(TokenProxy)
admin.site.register(TokenAdmin)
