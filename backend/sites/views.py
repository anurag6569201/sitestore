from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Site, Comment, Vote, Category
from django.db.models import Count
from django.http import JsonResponse


from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Site, Screenshot, Vote, Comment, CommentImage, Category
from .serializers import SiteSerializer, ScreenshotSerializer, VoteSerializer, CommentSerializer, CommentImageSerializer, CategorySerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "list": "/site-list",
        "details": "/site-details/<int:pk>",
        "create": "/site-create",
        "update": "/site-update/<int:pk>",
        "delete": "/site-delete/<int:pk>",
        "vote": "/site/<int:site_id>/vote/",
        "comment_list": "/site/<int:site_id>/comments/",
        "comment_create": "/site/<int:site_id>/comment-create/",
        "comment_like": "/comment/<int:comment_id>/like/",
        "comment_dislike": "/comment/<int:comment_id>/dislike/",
    }
    return Response(api_urls)


@api_view(['GET'])
def SiteList(request):
    sites = Site.objects.all()
    serializer = SiteSerializer(sites, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SiteDetails(request, pk):
    site = get_object_or_404(Site, pk=pk)
    serializer = SiteSerializer(site)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SiteCreate(request):
    serializer = SiteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def SiteUpdate(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.user != site.owner:
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = SiteSerializer(instance=site, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def SiteDelete(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.user != site.owner:
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    
    site.delete()
    return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    vote, created = Vote.objects.get_or_create(site=site, user=request.user)
    
    vote.vote = request.data.get('vote', True)  # Default to upvote
    vote.save()
    site.update_rating()

    return Response({"message": "Vote registered"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def comment_list(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    comments = site.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    data = request.data.copy()
    data['site'] = site.id
    data['user'] = request.user.id

    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes.add(request.user)
    return Response({"message": "Comment liked"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.dislikes.add(request.user)
    return Response({"message": "Comment disliked"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def screenshot_list(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    screenshots = site.screenshots.all()
    serializer = ScreenshotSerializer(screenshots, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_screenshot(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    data = request.data.copy()
    data['site'] = site.id

    serializer = ScreenshotSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



















def site_list(request):
    """
    View to list all sites with their categories.
    """
    sites = Site.objects.all()
    categories = Category.objects.all()
    return render(request, 'site_list.html', {'sites': sites, 'categories': categories})


def site_detail(request, site_id):
    """
    View to display a site's details, comments, categories, and votes.
    """
    site = get_object_or_404(Site, id=site_id)
    print("safe percentage:" , site.safe_percentage)

    comments = site.comments.all().annotate(total_likes=Count('likes')).order_by('-total_likes')
    categories = site.categories.all()
    user_vote = Vote.objects.filter(site=site, user=request.user).first() if request.user.is_authenticated else None
    
    if request.method == 'POST' and 'comment' in request.POST:
        if request.user.is_authenticated:
            text = request.POST.get('comment_text')
            if text:
                Comment.objects.create(site=site, user=request.user, text=text)
                return redirect('site_detail', site_id=site.id)
        else:
            return redirect('login')

    return render(request, 'site_detail.html', {
        'site': site, 
        'comments': comments, 
        'categories': categories, 
        'user_vote': user_vote,
    })


@login_required
def like_comment(request, comment_id):
    """
    AJAX-based view to like or dislike a comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)  # Unlike
        liked = False
    else:
        comment.likes.add(request.user)  # Like
        liked = True
    
    return JsonResponse({'liked': liked, 'total_likes': comment.likes.count()})


@login_required
def dislike_comment(request, comment_id):
    """
    AJAX-based view to dislike a comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user in comment.dislikes.all():
        comment.dislikes.remove(request.user)  # Remove dislike
        disliked = False
    else:
        comment.dislikes.add(request.user)  # Dislike
        disliked = True
    
    return JsonResponse({'disliked': disliked, 'total_dislikes': comment.dislikes.count()})


@login_required
def vote_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    print("safe percentage:" , site.safe_percentage)
    
    if request.method == 'POST':
        vote_value = request.POST.get('vote')
        
        # Ensure user is logged in
        if request.user.is_authenticated:
            # Check if the user has already voted for this site
            user_vote = Vote.objects.filter(site=site, user=request.user).first()

            if user_vote:
                # Update the vote if it already exists
                user_vote.vote = True if vote_value == 'upvote' else False
                user_vote.save()
            else:
                # Create a new vote if the user hasn't voted yet
                Vote.objects.create(site=site, user=request.user, vote=True if vote_value == 'upvote' else False)

            # After saving, we want to ensure the safe percentage is updated, so reload the site object
            site.refresh_from_db()
            
            # Optionally, redirect to the same page to reflect the updated data
            return redirect('site_detail', site_id=site.id)

    return render(request, 'site_detail.html', {'site': site})

 
