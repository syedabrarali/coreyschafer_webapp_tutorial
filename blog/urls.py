from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"), #Class based views need to called using as_view()
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name='post-create'), #this unlike the top two class based views doesn't expect a template like
                                                                      # <appname>/<model>_<viewtype> but <appname>/<model>_form and same goes for update view as well.
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about"),
]