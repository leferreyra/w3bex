from django.contrib import admin
from blog.models import Post, Tag, Image

class ImageInline(admin.TabularInline):
    model = Image


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# registrar los modelos para el panel del admin
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
