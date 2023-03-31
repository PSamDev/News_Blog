from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Category,Comment
from .forms import MessageForm
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone

def home(request):
    first_news=News.objects.first()
    last_news=News.objects.last()
    three_news=News.objects.all().order_by("-post_time")[1:4]
    categories=Category.objects.all().order_by("title")
    news = News.objects.all().filter(post_time__gte=timezone.now()).order_by("-post_time")
    return render(request,'index.html',{
        'first_news':first_news,
        'three_news':three_news,
        'categories':categories,
        'last_news':last_news,
        "news":news,
    })

# All News
def all_news(request):
    all_news=News.objects.all().order_by("-post_time")
    return render(request,'all-news.html',{
        'all_news':all_news,
        
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted and in moderation mode.')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments, 
    })

# Fetch all category
def all_category(request):
    cats=Category.objects.all().order_by("title")
    return render(request,'category.html',{
        'cats':cats
    })


# Fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category).order_by("-post_time")
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

def contact(request):
    if request.method == "POST":
        form = MessageForm (request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Message Submitted")
    else:
        form = MessageForm 
    return render(request, "contact.html", context={"form":form})

def search(request):
    if request.method == "POST":
        searched = request.POST(searched)
        output = News.objects.filter(title__contains="searched")
        return render (request, "search.html", 
                       {"searched":searched,
                        "output":output})
    else:
        return render (request, "search.html")
    
def search_results(request):
    query = request.GET.get('query')
    results = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {'query': query, 'results': results}
    return render(request, 'search_results.html', context)