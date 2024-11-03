from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('pins/', views.Pins.as_view(), name='pins'),
    path('pins/<int:id>/', views.pin, name='pin-detail'),
    path('pins/<str:username>/', views.get_pins_by_user, name='pins-by-user'),
    path('users/', views.UserProfileView.as_view(), name='user-profiles'),
    path('users/<str:username>/', views.UserProfileView.as_view(), name='user-profile-detail'),
    path('media/<path:path>/', views.serve_avatar, name='serve-avatar'),
    path('albums/', views.Albums.as_view(), name='albums'),
    path('albums/<int:id>/', views.album, name='album-detail'),
    path('albums/<str:username>/', views.get_albums_by_user, name='albums-by-user'),
    path('albums/<str:username>/<str:albumname>/', views.get_album_by_name, name='album-by-name'),
]
