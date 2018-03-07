from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm, EditTodoItemForm


def get_todo_page(request):
    if request.method == "POST":
        print("POST")
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        print("The GET Method Was Used, Please Change to the POST Method")
    
    form = TodoItemForm()
    items = TodoItem.objects.all()
    return render(request, "todoapp/index.html", {'items': items, 'form': form})

def edit_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    
    if request.method == "POST":
        print("POST")
        form = EditTodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
    else:
        print("GET")
    
    form = EditTodoItemForm(instance = item)
    return render(request, "todoapp/todo_item_form.html", {'form': form,})
    
def delete_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.delete()
    return redirect("todo_index")

def toggle_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    if item.done == True:
        item.done = False
    else:
        item.done = True
    item.save()
    return redirect("todo_index")