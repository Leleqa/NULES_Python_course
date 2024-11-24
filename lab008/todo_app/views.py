from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .models import Renters
from .forms import TodoForm
from .forms import RentersForm

def renters_list(request):
    renters = Renters.objects.all()
    return render(request, 'renters_list.html', {'renters': renters})

def renters_create(request):
    if request.method == 'POST':
        form = RentersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('renters_list')
    else:
        form = RentersForm()
    return render(request, 'renters_create.html', {'form': form})

def renters_update(request, pk):
    renters = get_object_or_404(Renters, pk=pk)
    if request.method == 'POST':
        form = RentersForm(request.POST, instance=renters)
        if form.is_valid():
            form.save()
            return redirect('renters_list')
    else:
        form = RentersForm(instance=renters)
    return render(request, 'renters_update.html', {'form': form})

def renters_delete(request, pk):
    renters = get_object_or_404(Renters, pk=pk)
    if request.method == 'POST':
        renters.delete()
        return redirect('renters_list')
    return render(request, 'renters_delete.html', {'renters': renters})

# # Todo List View
# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, 'todo_list.html', {'todos': todos})

# # Todo Create View

# def todo_create(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForm()
#     return render(request, 'todo_create.html', {'form': form})

# # Todo Update View
# def todo_update(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'todo_update.html', {'form': form})

# # Todo Delete View
# def todo_delete(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     if request.method == 'POST':
#         todo.delete()
#         return redirect('todo_list')
#     return render(request, 'todo_delete.html', {'todo': todo})
