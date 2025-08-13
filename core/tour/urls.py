
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category_list, name='category'),
    path('category/<int:category_id>/', views.category_gallery, name='category_gallery'),
    path('category/<int:category_id>/add-photo/', views.add_photo_to_category, name='add_photo_to_category'),

    # аутентификация:
    path('login/',  auth_views.LoginView.as_view(template_name='tour/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # регистрация:
    path('signup/', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

