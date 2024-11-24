from django.shortcuts import render, get_object_or_404, redirect
from .models import Renters
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

