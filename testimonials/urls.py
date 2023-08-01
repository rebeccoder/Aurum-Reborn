from django.urls import path
from testimonials import views
from .views import testimonial_list, testimonial_create, testimonial_edit

app_name = 'testimonials'

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('create/', views.testimonial_create, name='testimonial_create'),
    path('edit/<int:testimonial_id>/',
         views.testimonial_edit, name='testimonial_edit'),
    path('delete/<int:testimonial_id>/',
         views.testimonial_delete, name='testimonial_delete'),
]
