from django.urls import path
from .views import recipe_list, recipe_detail, recipe_form, signup, logout_view, login_view


urlpatterns = [
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipes/add/', recipe_form, name='recipe_add'),
    path('recipes/<int:pk>/edit/', recipe_form, name='recipe_edit'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]
