from django.contrib import admin

from .models import (Post, Group, Answer)
# Register your models here.

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Answer)
