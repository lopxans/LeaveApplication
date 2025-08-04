from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('update/<int:id>', update, name="update"),
    path('recycle/', recycle, name="recycle"),
    path('delete/soft/<int:id>', soft_delete, name="soft_delete"),
    path('soft/clear', soft_clear_all, name="soft_clear_all"),
    path('delete/hard/<int:id>', delete_hard, name="delete_hard"),
    path('clear/all', clear_all, name="clear_all"),
    path('restore/<int:id>', restore, name="restore"),
    path('restore/all', restore_all, name="restore_all"),

    path('about/', about, name="about"),

    path('contact/', contact, name="contact"),
    path('contact/view/', view_contact, name="view_contact"),
    path('contact/view/recycle/', recycle_contact, name="recycle_contact"),
    path('contact/view/recycle/soft/<int:id>', del_soft_contact, name="del_soft_contact"),
    path('contact/view/recycle/clear1', soft_clear_all_contact, name="soft_clear_all_contact"),
    path('contact/view/recycle/delete/<int:id>', del_contact, name="del_contact"),
    path('contact/view/recycle/delete/', clear_contact, name="clear_contact"),
    path('contact/view/recycle/restore/<int:id>', retore_contact, name="retore_contact"),
    path('contact/view/recycle/restore/', restore_all_contact, name="restore_all_contact"),
]