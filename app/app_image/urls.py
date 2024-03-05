from django.urls import path
from app_image import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('profile/', views.PrivateDocumentCreateView.as_view(template_name="privatedocument_form.html"), name='profile'),
]
