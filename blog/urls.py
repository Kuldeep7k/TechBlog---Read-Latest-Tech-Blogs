from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("allposts", views.AllPostsView.as_view(), name="allposts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_detail"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later")
]
