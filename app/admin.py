from django.contrib import admin
from .models import User, Thread, Club, Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Thread)
admin.site.register(Club)
admin.site.register(Comment)
