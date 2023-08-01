from django.urls import path
from .views import (BlogListView,
                    BlogDeleteView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDelete2View
                    )

urlpatterns = [
    path('post/<int:pk>/delete ', BlogDelete2View.as_view(), name='post_delete'),
    path('post/<int:pk>/edit ', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDeleteView.as_view(), name='post_detail'),
]