from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Post

import random 

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    
    return render(request,'index.html',locals())

def lotto(request):
    lottos = list()
    lucky = random.randint(1,42)
    for i in range(6):
        lottos.append(random.randint(1,42))
    return render(request,'lotto.html',locals())