from django.contrib import admin
from bbs import models
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","author","hidden","posttime")


# Register your models here.
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Comment)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)

