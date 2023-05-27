from django.shortcuts import render, redirect
from .models import project, skill, Message
from .forms import ProjectForm
# Create your views here.


def homepage(request):
    proj = project.objects.all()
    deatiledskills = skill.objects.exclude(body='')
    skills = skill.objects.filter(body = '')
    context = {'proj':proj,
                'detailedskills' : deatiledskills,
                'skills' : skills
               }
    return render(request,'base/home.html',context )

def projectpage(request, pk):
    projects = project.objects.get(id = pk)
    context = {'projects' : projects
         
    }
    return render (request, 'base/project.html', context)


def addproject(request):
    
    form = ProjectForm()
     
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form' : form}
    return render(request, 'base/project_form.html', context)

def editproject(request, pk ):
    projects = project.objects.get(id=pk)
    form = ProjectForm(instance = projects)
     
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = projects)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/project_form.html', context)

def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')

    context = { 'inbox' : inbox

    }
    return render (request, 'base/inbox.html', context)