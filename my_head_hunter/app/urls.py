from django.urls import path

from .views import *

urlpatterns = [
    path('', get_vacancies_list),

    path('login/', login_user),
    path('register', register),

    path('edit/employer', edit_employer),
    path('edit/worker', edit_worker),
    path('get/employer/<int:id>', get_employer),
    path('get/worker/<int:id>', get_worker),

    path('create/vacancy', create_vacancy),
    path('get/vacancies', get_vacancies_list),
    path('get/vacancy/<int:id>', get_vacancy),

    path('get/messages//<int:id_emp>/<int:id_work>', get_messages_list),
    path('send/message', send_message)
]
