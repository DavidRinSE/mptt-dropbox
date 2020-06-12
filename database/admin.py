from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Node_Model
# Register your models here.

admin.site.register(Node_Model, MPTTModelAdmin)