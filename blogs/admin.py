from django.contrib import admin

# modles
from blogs.models import PostsModel, CommentariyModel, MassageModel

# Register your models here.


admin.site.register(PostsModel)
admin.site.register(CommentariyModel)
admin.site.register(MassageModel)
