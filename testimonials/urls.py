from django.urls import path
from testimonials import views

app_name = 'testimonials'

urlpatterns = [
    path('/testimonials', views.testimonial_list, name='testimonial_list'),
    path('create/', views.testimonial_create, name='testimonial_create'),
    path('edit/<int:testimonial_id>/', views.testimonial_edit, name='testimonial_edit'),
    path('delete/<int:testimonial_id>/', views.testimonial_delete, name='testimonial_delete'),
]
