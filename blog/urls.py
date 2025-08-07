from django.urls import path

from . import views


urlpatterns = [
    # path('', views.index, name='blog_index'),
    # path('<int:pk>/', views.detail, name='blog_detail'),
    # path('create/', views.create, name='blog_create'),
    # path('createfake/', views.create_fake, name='blog_create_fake'),
    path('category/<slug>/', views.category, name='category'),
    # path('<int:pk>/delete/', views.delete, name='blog_delete'),
    # path('<int:pk>/update/', views.update, name='blog_update'),
    # path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    # path('<int:pk>/update_comment/', views.update_comment, name='update_comment'),
    # path('<int:pk>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
