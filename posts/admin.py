from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from  .models import Post
from .models import Comment

class PostAdmin(SummernoteModelAdmin):
    list_display = ['id','author','publish_date']
    list_filter =['publish_date','tags']
    search_fields =['author','content']
    summernote_fields = ('content',)

    summernote_config = {
        'width': '100%',  # Set the width as needed
        'height': '400px',  # Set the height as needed
    }


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)