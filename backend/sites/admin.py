from django.contrib import admin
from .models import Site, Screenshot, Vote, Comment, Category, CommentImage


class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 1


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 1
    readonly_fields = ('created_at',)  # Make vote timestamps readonly


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('created_at',)


class CommentImageInline(admin.TabularInline):
    model = CommentImage
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_verified_by_owner', 'safe_percentage', 'rating')
    list_filter = ('is_verified_by_owner',)
    search_fields = ('name', 'url', 'owner__username')
    inlines = [ScreenshotInline, VoteInline, CommentInline, CategoryInline]
    readonly_fields = ('safe_percentage', 'rating')  # Rating is updated dynamically


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('site', 'image', 'description')
    search_fields = ('site__name',)
    list_filter = ('site',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'vote', 'created_at')
    list_filter = ('vote',)
    search_fields = ('site__name', 'user__username')
    readonly_fields = ('created_at',)  # Ensures created_at is not editable


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'text', 'get_likes_count', 'get_dislikes_count', 'created_at')
    search_fields = ('site__name', 'user__username', 'text')
    list_filter = ('site',)
    readonly_fields = ('created_at',)
    inlines = [CommentImageInline]  # Allow adding images to comments

    # Custom methods to count likes and dislikes
    def get_likes_count(self, obj):
        return obj.likes.count()
    get_likes_count.short_description = 'Likes'

    def get_dislikes_count(self, obj):
        return obj.dislikes.count()
    get_dislikes_count.short_description = 'Dislikes'


@admin.register(CommentImage)
class CommentImageAdmin(admin.ModelAdmin):
    list_display = ('comment', 'image')
    search_fields = ('comment__text',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('site', 'name')
    search_fields = ('site__name', 'name')
    list_filter = ('site',)
