from django.urls import path
import sites.views as views

app_name="sites"

urlpatterns = [
    path('', views.api_overview, name='api-overview'),   
    path('site-list', views.SiteList, name='site-list'),   
    path('site-details/<int:pk>', views.SiteDetails, name='site-details'),   
    path('site-create', views.SiteCreate, name='site-crate'),   
    path('site-update/<int:pk>', views.SiteUpdate, name='site-update'), 
    path('site-delete/<int:pk>', views.SiteDelete, name='site-delete'), 





    path('list', views.site_list, name='site_list'),
    path('site/<int:site_id>/', views.site_detail, name='site_detail'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('comment/<int:comment_id>/dislike/', views.dislike_comment, name='dislike_comment'),
    path('site/<int:site_id>/vote/', views.vote_site, name='vote_site'),
]
