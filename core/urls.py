from django.urls import path
from core import views


urlpatterns = [
    path("", views.index),
    path("watch/<int:pk>/", views.videoDetail, name="video-detail"),

    #Saving Comment TO DB
    path("ajax-save-comment/", views.ajax_save_comment, name="save_comment"),
    path("ajax-delete-comment/", views.ajax_delete_comment, name="delete_comment"),

    #Subscribe Function
    path("add-sub/<int:id>/", views.add_new_subscribers, name="add_sub"),
    path("load-sub/<int:id>/", views.load_channel_subs, name="load_sub"),

    #Like Function
    path("add-like/<int:id>/", views.add_new_like, name="add_like"),
    path("likes-load/<int:id>/", views.load_video_likes, name="likeLoad"),
]
