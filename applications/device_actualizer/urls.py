from django.urls import path
from . import views

app_name = 'applications.device_actualizer'
urlpatterns = [
    path('snmpc_devices/', views.snmpc_devices_view, name='snmpc_devices_all'),
    path('snmpc_devices/filter/<str:filter>', views.snmpc_devices_view_filter, name='snmpc_devices_filter'),
    path('snmpc_devices/<str:dev_snmpc_id>/', views.snmpc_device_view, name='snmpc_device_detail'),
    path('esma_devices/', views.esma_devices_view, name='esma_devices_all'),
    path('esma_devices/<str:dev_esma_id>/', views.esma_device_view, name='esma_device_detail'),
    path('upload_file/esma_devices', views.upload_file, name='esma_devices_upload_file'),
    path('error/', views.error, name='error')
]