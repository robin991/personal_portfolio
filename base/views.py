from django.shortcuts import render
from .models import project, skill
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

