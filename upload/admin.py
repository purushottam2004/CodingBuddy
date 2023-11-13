from django.contrib import admin

# Register your models here.

from .models import student, test, ans
admin.site.register(student)
admin.site.register(test)
admin.site.register(ans)
