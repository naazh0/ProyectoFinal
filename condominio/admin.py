# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Condominio, AdminCondominio, Copropietario

# Register your models here.

admin.site.register(Condominio)
admin.site.register(AdminCondominio)
admin.site.register(Copropietario)