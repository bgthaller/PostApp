from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'Post'

urlpatterns = [
		path('', views.home, name='home'),
		path('<int:post_id>/', views.post_view, name='post_view'),
		path('post-home', views.posthome, name='posthome'),
		path('admin_postlist', views.admin_postlist, name='admin_postlist'),
		path('delete/<int:id>/', views.post_delete, name='post_delete'),
		path('editpost', views.editpost, name='editpost'),
		path('update/<int:id>/', views.editpost, name='post_update'),
		path('imageList/<int:id>/', views.imageList, name='imageList'),
		path('image/update/<int:id>', views.image_update, name='image_update'),
		path('image/delete/<int:id>/', views.image_delete, name='image_delete'),

	]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)