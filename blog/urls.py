# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.urls import path
from . import views
from .views import AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/slug/', AddPostView.as_view(), name='add_post'),
    path('add_category/slug/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<slug:slug>/', EditPostView.as_view(), name='edit_post'),
    path('post/<slug:slug>/remove', DeletePostView.as_view(),
         name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category')
    # path('delete_categroy/slug/', DeleteCategoryView.as_view(),
    #      name='delete_categroy')
]
