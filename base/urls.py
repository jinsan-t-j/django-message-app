from django.urls import path 
from . import views

app_name = 'base'
urlpatterns = [
    path('login', views.loginAction, name="login"),
    path('register', views.registerAction, name="register"),

    path('', views.home, name="home"),
    path('rooms/<int:id>', views.room, name="room"),
    path('rooms/create', views.createRoom, name="create.room"),
    path('rooms/store', views.storeRoom, name="store.room"),
    path('rooms/edit/<int:id>', views.editRoom, name="edit.room"),
    path('rooms/update/<int:id>', views.updateRoom, name="update.room"),
    path('rooms/delete/<int:id>', views.destroyRoom, name="destroy.room"),
]