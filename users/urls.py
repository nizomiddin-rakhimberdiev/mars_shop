from django.urls import path
from .views import (register_view,
                    login_view,
                    logout_view,
                    profile_view,
                    edit_profile_view,
                    add_coins_view,
                    group_detail_view,
                    buy_product_view,
                    )

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile_view, name='edit-profile'),
    path('add-coins/<int:id>/', add_coins_view, name='add-coins'),
    path('groups/<int:id>/', group_detail_view, name='group-detail'),
    path('buy/<int:id>/', buy_product_view, name='buy'),

]