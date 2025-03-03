from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Site, Comment, Vote, Category
from django.db.models import Count
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from sites.serializers import SiteSerializer


@api_view(['GET'])
def api_overview(request):
    print(request.user)
    api_urls = {
        "list": "sites/list"


    }
    return Response(api_urls)




@api_view(['GET'])
def SiteList(request):
    sites = Site.objects.all()
    serializer = SiteSerializer(sites, many=True)  # ✅ Create a serializer instance

    return Response(serializer.data)  # ✅ Use `.data` to extract JSON serializable data


@api_view(['GET'])
def SiteDetails(request , pk):
    site = get_object_or_404(Site, pk = pk)
    serializer = SiteSerializer(site, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def SiteCreate(request):
    serializer = SiteSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response("Created succesfully!!")


@api_view(['POST'])
def SiteUpdate(request , pk):
    site = get_object_or_404(Site , pk = pk)
    serializer = SiteSerializer(instance = site , data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response("Updated succesfilly!!")



@api_view(['DELETE'])
def SiteDelete(request , pk):
    site = get_object_or_404(Site , pk = pk)
    site.delete()

    return Response("Deleted succesfilly!!")



















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

 
