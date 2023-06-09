from django.urls import path
from .views import CreatorListView, CreatorCreateView, CreatorUpdateView, CreatorDeleteView

app_name = 'creators'

urlpatterns = [
    path('', CreatorListView.as_view(), name='creators'),
    path('create/', CreatorCreateView.as_view(), name='creator_create'),
    path('update/<int:pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('delete/<int:pk>/', views.CreatorDeleteView.as_view(), name='creator_delete'),
]