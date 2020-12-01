from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Post,AccessInfo
import random
from datetime import datetime
from django.shortcuts import redirect


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    return render(request, "index.html", locals())

def mychart(request):
    now = datetime.now()
    return render(request,'mychart.html',locals())
    
def lotto(request):
    lucky = random.randint(1, 42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))
    
    return render(request, "lotto.html", locals())

def showpost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        now = datetime.now()
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

    return render(request, "article.html", locals())
    