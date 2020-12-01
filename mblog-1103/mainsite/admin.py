from django.contrib import admin
from mainsite.models import Post,AccessInfo,Branch,StoreIncome

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch','income_year','income_month','income')
admin.site.register(Post, PostAdmin)
admin.site.register(AccessInfo)
admin.site.register(Branch,BranchAdmin)
admin.site.register(StoreIncome,StoreIncomeAdmin)