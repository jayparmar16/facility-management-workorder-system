from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.login_request,name='login'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('dashboard/',views.view_home,name='dash'),
    path('dashboard-user/',views.view_dash_user,name='dashboard-user'),
    path('dashboard-admin/',views.view_dash_admin,name='dashboard-admin'),
    path('dashboard-super/',views.view_dash_super,name='dashboard-super'),
    path('initial/<str:r>/estimation_report/',views.view_estimation,name='estimation_report'),
    path('final/<str:r>/estimation_report/',views.view_estimation,name='estimation_report'),
    path('<str:r>/completion_report/',views.view_completion_form,name='completion_report'),
    path('view_request/<str:pk_r>/',views.view_request,name='view_request'),
    path('view_req_admin/<str:pk_r>/',views.view_request_admin,name='view_admin'),
    path('create_request/',views.create_request,name='create_request'),
    path('update_request/admin/<str:pk>/',views.update_req_admin,name='update_request_admin'),
    path('update_request/user/<str:pk>/',views.update_req_user,name='update_request_user'),
    path('delete_request/<str:pk>/',views.del_req,name='del_req'),
    path('update_status/<str:pk>/',views.update_status,name='update_status'),
    path('update_estimate/<str:pk>/',views.update_estimate,name='update_estimate'),
    path('delete_estimate/<str:pk>/',views.delete_estimate,name='delete_estimate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)