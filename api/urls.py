from django.urls import path
from . import views


urlpatterns = [
    #Todos
    path('todos/completed', views.ToDoCompletedList.as_view()),
    path('todos/', views.ToDoListCreate.as_view()),
    path('todos/<int:pk>', views.ToDoRetrieveDestroy.as_view()),
    path('todos/<int:pk>/complete', views.ToDoComplete.as_view()),

    #Auth
    path('signup', views.signup),
    path('login', views.login),
]

