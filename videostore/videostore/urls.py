from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as vi
from django.contrib.auth import views as ausViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('reg/', vi.register, name='reg'),
    path('profile/', vi.profile, name='profile'),
    path('user/', ausViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', ausViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('pass-reset/', ausViews.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass-reset'),
    path('password_reset_complete/',
         ausViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/',
         ausViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done/<uidb64>/<token>/',
         ausViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
