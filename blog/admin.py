from django.contrib import admin
from blog.models import Post, Tag

# registrar los modelos para el panel del admin
admin.site.register(Post)
admin.site.register(Tag)