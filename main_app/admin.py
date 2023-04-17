from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main_app.models import User, Publications, Comments


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "birthday", "date_joined", "date_editing")
    # Поля которые будут показаны в админке.
    list_filter = ("first_name", "last_name", "birthday")
    # Поля по которым будет производиться фильтрация в админке.
    search_fields = ("first_name", "last_name", "full_name")
    # Поля по которым будет происходить поиск в админке.


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ("heading", "text", "image", "author_link", "comments", "date_creation", "date_editing")
    list_filter = ("heading", "author", "text", "date_creation")
    search_fields = ("heading", "text", "author_link")

    def author_link(self, obj):
        author = obj.author
        url = reverse("admin:main_app_user_changelist") + str(author.pk)
        return format_html(f"<a href='{url}'>{author}</a>")

    author_link.short_description = "Автор"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("author_link", "text", "date_creation", "date_editing")
    list_filter = ("author", "text")
    search_fields = ("author_link", "text")

    def author_link(self, obj):
        author = obj.author
        url = reverse("admin:main_app_user_changelist") + str(author.pk)
        return format_html(f"<a href='{url}'>{author}</a>")

    author_link.short_description = "Автор"


admin.site.register(User, UserAdmin)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Comments, CommentsAdmin)
