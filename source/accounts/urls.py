from accounts.views import logout_view, login_view, register_view, user_activate, UserDetailView, \
    UserPasswordChangeView, UsersView, update_profile
from django.urls import path


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('register/activate/', user_activate, name='user_activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    # path('<int:pk>/update', UserEditView.as_view(), name='user_update'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('users/', UsersView.as_view(), name='user_list'),
    path('update/', update_profile, name='user_update'),
]


app_name = 'accounts'