from django.contrib import admin

from .models import TestElementA, TestElementB, TestElementC


class TestElementAAdmin(admin.ModelAdmin):
    pass


class TestElementBAdmin(admin.ModelAdmin):
    filter_horizontal = ('ace',)


class TestElementCAdmin(admin.ModelAdmin):
    pass


admin.site.register(TestElementA, TestElementAAdmin)
admin.site.register(TestElementB, TestElementBAdmin)
admin.site.register(TestElementC, TestElementCAdmin)
