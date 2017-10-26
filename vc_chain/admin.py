from django.contrib import admin
from vc_chain import models

admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.Star)
admin.site.register(models.Fork)
admin.site.register(models.Follow)
admin.site.register(models.Commit)
