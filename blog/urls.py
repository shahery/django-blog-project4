# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.urls import path, include
from . import views
from .views import AddPostView, EditPostView, DeletePostView
from .views import AddCategoryView, category_view

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/slug/', AddPostView.as_view(), name='add_post'),
    path('add_category/slug/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<slug:slug>/', EditPostView.as_view(), name='edit_post'),
    path('post/<slug:slug>/remove', DeletePostView.as_view(),
         name='delete_post'),
    path('category/<str:cats>/', category_view, name='category'),
    path('summernote/', include('django_summernote.urls')),
    path(
        'delete_post_comment/<int:comment_id>/',
        views.delete_post_comment,
        name='delete_post_comment'),
]
