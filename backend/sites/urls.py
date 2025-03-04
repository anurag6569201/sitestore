from django.urls import path
import sites.views as views

app_name="sites"

urlpatterns = [

    path('', views.api_overview, name='api-overview'),
    path('site-list/', views.SiteList, name='site-list'),
    path('site-details/<int:pk>/', views.SiteDetails, name='site-details'),
    path('site-create/', views.SiteCreate, name='site-create'),
    path('site-update/<int:pk>/', views.SiteUpdate, name='site-update'),
    path('site-delete/<int:pk>/', views.SiteDelete, name='site-delete'),
    path('site/<int:site_id>/vote/', views.vote_site, name='vote-site'),
    
    # Comments
    path('site-comment/<int:site_id>', views.comment_list, name='comment-list'),
    path('site-comment-create/<int:site_id>', views.comment_create, name='comment-create'),
    path('site-comment-like/<int:comment_id>', views.like_comment, name='like-comment'),
    path('site-comment-dislike/<int:comment_id>', views.dislike_comment, name='dislike-comment'),

    # Screenshots
    path('site-screenshots/<int:site_id>', views.screenshot_list, name='screenshot-list'),
    path('site-screenshots-upload/<int:site_id>', views.upload_screenshot, name='upload-screenshot'),




    path('list', views.site_list, name='site_list'),
    path('site/<int:site_id>/', views.site_detail, name='site_detail'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('comment/<int:comment_id>/dislike/', views.dislike_comment, name='dislike_comment'),
    path('site/<int:site_id>/vote/', views.vote_site, name='vote_site'),
]


