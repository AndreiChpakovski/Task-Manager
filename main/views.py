from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import Max
from .models import Task, Comment
from .forms import TaskForm


def index(request):
    tasks = Task.objects.filter(is_complete=False).order_by("-id")    # [:numero]  колизество записей что будут появляться
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, "main/index.html", {"title": "Главная Страница", "tasks": tasks, 'comments': comments})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    comments = task.comments.all().order_by('-created_at')
    return render(request, 'main/task_detail.html', {'task': task, 'comments': comments})


def add_comment(request, task_id=True):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        if name and content:
            Comment.objects.create(name=name, content=content)
    return redirect('home')


def about(request):
    tasks = Task.objects.all()
    return render(request, 'main/about.html', {"title": "Все задачи", "tasks": tasks})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    tasks = Task(title=title)
    tasks.save()
    return redirect('about')


def update(request, tasks_id):
    tasks = Task.objects.get(id=tasks_id)
    tasks.is_complete = not tasks.is_complete
    tasks.save()
    return redirect('about')


def delete(request, tasks_id):
    tasks = Task.objects.get(id=tasks_id)
    tasks.delete()
    return redirect('about')




def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была неверной"
    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, "main/create.html", context)




# Create your views here.
