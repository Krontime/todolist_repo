from django.conf.urls import url, include
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', get_todo_page, name="todo_index"),
    url(r'delete/(\d+)$', delete_todo_item, name="delete_todo"),
    url(r'toggle/(\d+)$', toggle_todo_item, name="toggle_todo"),
    url(r'edit/(\d+)$', edit_todo_item, name="edit_todo"),
]
