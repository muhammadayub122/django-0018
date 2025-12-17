from django.contrib import admin
from .models import Post,PostComment,PostView
# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostView
                    )

class Postadmin(admin.ModelAdmin):
  readonly_fields=['views_count','total_comments']