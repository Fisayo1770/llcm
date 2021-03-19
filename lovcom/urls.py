from django.urls import path

from . import views

app_name = 'lovcom'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('post_create', views.PostCreatView.as_view(), name='post_create'),

    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,
        name='post_detail'),
]
