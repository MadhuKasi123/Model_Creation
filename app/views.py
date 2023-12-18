from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def dispaly_topics(request):

     QLTO=Topic.objects.all()
     QLTO=Topic.objects.all().order_by('-topic_name')
     QLTO=Topic.objects.filter(topic_name='cricket')
     d={'topics': QLTO}
     return render(request,'display_topics.html',d)


def dispaly_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by('name')
    d={'topics':QLWO}
    return render(request,'dispaly_webpage.html',d)


def display_access(request):
     QLAO=AcessRecord.objects.all()
     QLAO=AcessRecord.objects.all().order_by(Length('author'))
     
     d={'topics':QLAO}
     return render(request,'display_access.html',d)


def insert_topic(request):
     tn=input('enter topic : ')
     Nto=Topic.objects.get_or_create(topic_name=tn)[0]
     Nto.save()
     QLIO=Topic.objects.all()
     d={'topics':QLIO}
     return render(request,'display_topics.html',d)


def insert_webpage(request):
     tn=input('enter : ')
     n=input('name: ')
     u=input('url: ')
     e=input('email: ')
     TO=Topic.objects.get(topic_name=tn)
     NWO=Webpage.objects.get_or_create(topicname=TO,name=n,url=u,Email=e)[0]
     NWO.save()
     QLWO=Webpage.objects.all()
     d={'topics':QLWO}
     return render(request,'dispaly_webpage.html',d)

def insert_acess(request):
     pk=int(input('enter pk value:- '))
     d=input('enter:- ')
     a=input('enter:- ')
     To=Webpage.objects.get(pk=pk)
     Ao=AcessRecord.objects.get_or_create(name=To,date=d,author=a)[0]
     Ao.save()
     Qlto=AcessRecord.objects.all()
     d={'topics':Qlto}
     return render(request,'display_topics.html',d)