from django.shortcuts import render,redirect
from .forms import ShortUrlForm
from .models import ShortUrl
import string,random

def index(request):
    shortUrlForm = ShortUrlForm()
    if request.method=="POST":
        shortUrlForm = ShortUrlForm(request.POST or None)
        if shortUrlForm.is_valid():
            shortUrlForm = shortUrlForm.save(commit=False)
            shortUrlForm.shortUrl = generateShortUrl()
            shortUrlForm.save()
            return redirect("detail", shortUrlForm.id)

    return render(request,template_name="index.html",context={"shortUrlForm": shortUrlForm})


def generateShortUrl():
    return ''.join(random.choice(string.ascii_letters)for x in range(16))

def detail(request,id):
    getdata = ShortUrl.objects.get(id=id)
    return render(request,template_name="view.html",context={"getData":getdata})

def redirectToUrl(request,shortUrl):
    data = ShortUrl.objects.get(shortUrl=shortUrl)
    return redirect(data.longUrl)