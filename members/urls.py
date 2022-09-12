from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'members'

urlpatterns = [
	path('login_user', views.login_user, name='login'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)