from django.urls import path 
from . import views 

app_name = 'blog' 

urlpatterns = [
    path('', views.AllPost.as_view(), name='list'),
    path('new/', views.CreatePost.as_view(), name='new'),
    path('<slug:slug>/', views.ViewPost.as_view(), name='view'),
    path('edit/<slug:slug>/', views.UpdatePost.as_view(), name='edit'),
    path('remove/<slug:slug>/', views.RemovePost.as_view(), name='remove'),
    path('tag/<str:tag>', views.TaggedPosts.as_view(), name='tag'),
]
