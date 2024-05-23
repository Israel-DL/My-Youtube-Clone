from django.contrib import admin
from core.models import Video, Comment
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class VideoAdmin(ImportExportModelAdmin):
    pass

class CommentAdmin(ImportExportModelAdmin):
    list_display = ["user", "comment", "video", "active"]

admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)



 