from django.contrib import admin
from . import models


admin.site.register(models.UserProfile)
admin.site.register(models.Board)
admin.site.register(models.BoardMember)
admin.site.register(models.Message)
