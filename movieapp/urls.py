from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup_user',views.signup_user,name='signup_user'),
    path('login_user',views.login_user,name='login_user'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('detail/<str:id>',views.detail,name='detail'),
    path('rate/<str:id>',views.rate,name='rate'),
    path('comment/<str:id>',views.comment,name='comment'),
    path('delete/<int:id>/<str:imdbID>',views.delete,name='delete'),
    path('favourite',views.favourite,name='favourite'),
    path('watch_list',views.watch_list,name='watch_list'),
    path('watch_list_delete/<str:id>',views.watch_list_delete,name='watch_list_delete'),
]
