from django.contrib import admin
from .models import Category, Photo, ExtraPhoto, User


class ExtraPhotoInline(admin.TabularInline):
    model = ExtraPhoto
    extra = 1

class PhotoAdmin(admin.ModelAdmin):
    inlines = [ExtraPhotoInline]
    list_display = ['title', 'category', 'author', 'date']


admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ExtraPhoto)
admin.site.register(User)




