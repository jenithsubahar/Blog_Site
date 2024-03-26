from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.reg,name='register'),
    path('login/', views.log, name='login'),
    path('blogPage/', views.blog, name='blogPage'),
    path('blogCreate/', views.create, name='blogCreate'),
    path('blogView/', views.view, name='blogView'),
    path('api/delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('api/submit-comment/', views.submit_comment, name='submit_comment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)