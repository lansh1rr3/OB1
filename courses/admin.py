from django.contrib import admin
from .models import Section, Material, Test, TestResult

admin.site.register(Section)
admin.site.register(Material)
admin.site.register(Test)
admin.site.register(TestResult)
