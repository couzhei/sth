from django.contrib import admin

# recall that admin panel and databases are different things! well duh!

# Register your models here.

from .models import Project, Tag, Review # since it's right in the directory of this file


admin.site.register(Project) # get this model and show it in the admin panel
admin.site.register(Review)
admin.site.register(Tag)