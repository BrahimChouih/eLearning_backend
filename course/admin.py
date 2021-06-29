from django.contrib import admin
from .models import Course, Video, Reviewer, Category

# Register your models here.

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Reviewer)
admin.site.register(Category)
# admin.site.register(Rater)
