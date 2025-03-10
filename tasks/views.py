from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Task
from .forms import TaskForm, SearchForm

def task_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    sort_by = request.GET.get('sort', 'due_date')
    
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    if status_filter:
        if status_filter == 'completed':
            tasks = tasks.filter(completed=True)
        elif status_filter == 'not_completed':
            tasks = tasks.filter(completed=False)
        elif status_filter in ['Overdue', 'Due Today', 'Upcoming']:
            tasks = tasks.filter(status=status_filter)
    
    if sort_by == 'title':
        tasks = tasks.order_by('title')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    elif sort_by == 'status':
        tasks = tasks.order_by('status')
    elif sort_by == 'created_at':
        tasks = tasks.order_by('-created_at')  
    
    context = {
        'tasks': tasks,
        'search_query': search_query,
        'status_filter': status_filter,
        'sort_by': sort_by,
    }
    
    return render(request, 'tasks/task_list.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))
