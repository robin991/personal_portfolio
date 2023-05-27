from django.shortcuts import render, redirect
from .models import project, skill, Message
from .forms import ProjectForm,MessageForm
from django.contrib import messages
# Create your views here.


def homepage(request):
    proj = project.objects.all()
    deatiledskills = skill.objects.exclude(body='')
    skills = skill.objects.filter(body = '')

    form = MessageForm()

    if request.method =="POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You message was successfully sent.')



    context = {'proj':proj,
                'detailedskills' : deatiledskills,
                'skills' : skills ,
                'form' : form
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
    unread_emails = Message.objects.filter(is_read = False).count()
    
    context = { 'inbox' : inbox,
               'unread_emails' : unread_emails

    }
    return render (request, 'base/inbox.html', context)

def messagePage(request, pk):
    message = Message.objects.get(id = pk)
    message.is_read = True # this will set the message read to true once the link is selected.
    message.save() # saving the above true condition
    context = { 'message' : message

    }
    return render (request, 'base/message.html', context)