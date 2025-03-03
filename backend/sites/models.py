from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Site model
class Site(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    is_verified_by_owner = models.BooleanField(default=False)

    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True, blank=True, null=True)
    age_limit = models.BooleanField(default=False, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    additional_info = models.JSONField(_("Additional Info"), blank=True, null=True)
    url = models.URLField()
    about = models.TextField( blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    rating = models.FloatField(default=0)  # Stores the average rating

    def update_rating(self):
        """ Updates site rating based on votes """
        total_votes = self.votes.count()
        if total_votes == 0:
            self.rating = 0
        else:
            upvotes = self.votes.filter(vote=True).count()
            self.rating = (upvotes / total_votes) * 5  # Scale to 5-star rating
        self.save()

    @property
    def safe_percentage(self):
        total_votes = self.votes.count()
        positive_votes = self.votes.filter(vote=True).count()
        return (positive_votes / total_votes * 100) if total_votes else 0

    def __str__(self):
        return self.name


# Screenshot model
class Screenshot(models.Model):
    site = models.ForeignKey(Site, related_name='screenshots', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='screenshots/' )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Screenshot for {self.site.name}"


# Vote model
class Vote(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField()  # True (Upvote), False (Downvote)
    created_at = models.DateTimeField(auto_now_add=True , null=True, blank=True)

    class Meta:
        unique_together = ('site', 'user')

    def save(self, *args, **kwargs):
        """Override save method to update site's rating on vote"""
        super().save(*args, **kwargs)
        self.site.update_rating()

    def delete(self, *args, **kwargs):
        """Override delete method to update site's rating when vote is removed"""
        super().delete(*args, **kwargs)
        self.site.update_rating()


# Comment model
class Comment(models.Model):
    site = models.ForeignKey(Site, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)
    parent_comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True, blank=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.site.name}"


# Comment Images model (to allow multiple images per comment)
class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comments/' , blank=True, null=True)

    def __str__(self):
        return f"Image for comment {self.comment.id}"


# Category model
class Category(models.Model):
    site = models.ForeignKey(Site, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('site', 'name')  # Ensures unique category per site

    def __str__(self):
        return self.name
