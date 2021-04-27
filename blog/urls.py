from django.urls import path
from .views import BlogListView, BLogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, AddCommentView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BLogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='post_comment'),
]