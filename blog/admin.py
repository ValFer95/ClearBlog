from django.contrib import admin

from django.db import models
from django.forms import Textarea
from blog.models import PostCategory, Post, Comment

admin.site.site_header = 'ClearBlog'
admin.site.site_url = '/blog/accueil/'

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'auteur', 'text_abstr', 'status', 'moderation_text', 'created_at')
    list_filter = ('status',)
    search_fields = ['post__title', 'auteur']

    def text_abstr(self, obj):
        return obj.commentaire[:50]
    text_abstr.short_description = 'Short text'

    list_editable = ('status', 'moderation_text')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'category', 'published', 'created_at', 'comment_counts')
    list_filter = ('category', 'published')

    autocomplete_fields = ['category']

    formfield_overrides = {
        models.TextField: {'widget' : Textarea(attrs={'rows':15, 'cols':90})}
    }

    def comment_counts(self, obj):
        return Comment.objects.filter(post=obj).count()
    comment_counts.short_description = "Comments"

