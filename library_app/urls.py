from django.urls import path

from library_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('user_home/',views.user_home,name='user_home'),
    path('login_view/',views.login_view,name='login_view'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('book_add/',views.book_add,name='book_add'),
    path('book_view/',views.book_view,name='book_view'),
    path('book_update<int:id>/',views.book_update,name='book_update'),
    path('book_delete<int:id>/',views.book_delete,name='book_delete'),
    path('user_book_view/',views.user_book_view,name='user_book_view')
]