from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.models import Video, Comment
from channel.models import Channel
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    video = Video.objects.filter(visibility="public")
    context = {
        "video":video
    }
    return render(request,"index.html", context)

def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    channel =  Channel.objects.get(user=video.user)

    channel.total_views = channel.total_views + 1
    channel.save()


    video.views = video.views + 1
    video.save()

    # Suggesting Video
    video_tags_id = video.tags.values_list("id", flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count("tags")).order_by("-same_tags", "-date")[:25]

    #Getting All Comments Relating To The Video
    comment = Comment.objects.filter(active=True, video=video).order_by("-date")
    

    context = {
        "video":video,
        "channel":channel,
        "comment":comment,
        "similar_videos":similar_videos,
    }
    return render(request,"video-detail.html", context)

def ajax_save_comment(request):
    if request.method == "POST":
        pk = request.POST.get("id")
        comment = request.POST.get("comment")
        video = Video.objects.get(id=pk)
        user = request.user

        new_comment = Comment.objects.create(comment=comment, user=user, video=video)
        new_comment.save()

        response = "Comment Posted"
        return HttpResponse(response)


@csrf_exempt
def ajax_delete_comment(request):
    if request.method == "POST":
        id  = request.POST.get("cid")
        comment = Comment.objects.get(id=id)
        comment.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":2})


def add_new_subscribers(request, id):
    subscribers = Channel.objects.get(id=id)
    user = request.user

    #If Israel is in [Israel's Subscribers]
    if user in subscribers.subscribers.all():
        subscribers.subscribers.remove(user)
        response = "Subscribe"
        return JsonResponse(response, safe=False, status=200)
    else:
        subscribers.subscribers.add(user)
        response = "Unsubscribe"
        return JsonResponse(response, safe=False, status=200)
    
#Load Channel Subs    
def load_channel_subs(request, id):
    subscribers = Channel.objects.get(id=id)
    sub_list = list(subscribers.subscribers.values())
    return JsonResponse(sub_list, safe=False, status=200)



def add_new_like(request, id):
    video = Video.objects.get(id=id)
    user = request.user

    #If Israel is in [Israel's Subscribers]
    if user in video.likes.all():
        video.likes.remove(user)
        like_response = "Like"
        return JsonResponse(like_response, safe=False, status=200)
    else:
        video.likes.add(user)
        like_response = "Dislike"
        return JsonResponse(like_response, safe=False, status=200)
    
def load_video_likes(request, id):
    video = Video.objects.get(id=id)
    likes_lists = list(video.likes.values())
    return JsonResponse(likes_lists, safe=False, status=200)



# def homepage(request):
#     return render(request,"test_temp/index.html")

# def aboutpage(request):
#     return render(request,"test_temp/about.html")

# def contact(request):
#     return render(request,"test_temp/contact.html")



