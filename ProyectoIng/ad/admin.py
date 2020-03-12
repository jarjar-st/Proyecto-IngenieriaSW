from django.contrib import admin
from .models import Category,AdKind,Location,Ad, Unit

# Register your models here.
admin.site.register(Category)
admin.site.register(AdKind)
admin.site.register(Location)
admin.site.register(Ad)
admin.site.register(Unit)
