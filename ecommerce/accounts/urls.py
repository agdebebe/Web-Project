from django.urls import path


from .views import (UserLoginView, UserRegistrerView,
                    UserLogoutView)


app_name = 'accounts'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrerView.as_view(), name='register'),
   
]
