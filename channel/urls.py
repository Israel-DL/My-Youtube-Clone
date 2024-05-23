from django.urls import path
from channel import views


urlpatterns = [
    path("<channel_name>/", views.channel_profile, name="channel-profile"),
    path("<channel_name>/video/", views.channel_videos, name="channel-videos"),
    path("<channel_name>/about/", views.channel_about, name="channel-about"),
    path("<channel_name>/community/", views.channel_community, name="channel-community"),
    path("<channel_name>/community/<int:community_id>", views.channel_community_detail, name="channel-community-detail"),


    #Create Community Comment URL
    path("community/<int:community_id>/create-comment/", views.create_comment, name="community-create-comment"),

    #Delete Community Comment URL
    path("community/<int:community_id>/<int:comment_id>/", views.delete_comment, name="community-delete-comment"),

    #Like Community Post
    path("community/<int:community_id>/like/", views.like_community_post, name="community-post-like")
]
