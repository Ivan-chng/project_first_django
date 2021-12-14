from django.urls import path

from . import views

app_name = 'company_training'

urlpatterns = [
    path('', views.index, name='index'),
    path('u2g2m/add/', views.add_u2g2m, name='add'),
    path('u2g2m/query/', views.query_u2g2m, name='query'),
    path('u2g2m/<int:id>/edit/', views.edit_u2g2m, name='edit'),
    path('u2g2m/<int:id>/delete/', views.delete_u2g2m, name='delete'),

    path('c2b2t/query/', views.query_c2b2t, name='query_c2b2t'),
    path('test/', views.test, name='test'),
]
