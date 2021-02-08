from django.shortcuts import render, redirect, get_object_or_404
from . models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from . forms import ContactForm
from django.db.models import Q

# Create your views here.
# request -> django -> response 
# while using get request we get one post/response so not iterable things,
# that response is grabbed from the database
#print("django says", request.method, request.path, request.user)
def homepage(request):
# this will list limited number of post on homepage
	return render(request=request,
				template_name='blog/home.html',
				context= {'posts': Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")[:5]})


# this will list all post on blog
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
	context = {'posts': posts}
	return render(request, 'blog/post_list.html', context)


# this will show the detail of post which will be directed from blog or from homepage
def post_detail(request, slug):
	post = Post.objects.get(slug = slug)
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)


#this will show my reading list
def bookshelf_page(request):
	return render(request, 
				template_name = 'blog/bookshelf_page.html',
				context = {})


# this will take you on a page to contact me
def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form=ContactForm()
	return render(request, 
				template_name = "blog/contact_page.html",
				context = { "form": form})


# this will talk about the website owner
def about_page(request):
	return render(request, 
					template_name = "blog/about_page.html",
					context = {})


# this will help to search the desired post or word on site
def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		lookups = Q(title__icontains = q) | Q(content__icontains = q)
		print(lookups)
		post = Post.objects.filter(lookups).distinct()
		print(post)
		context = {"post": post}
		template_name = 'blog/results.html'
	else:
		context = {}
		template_name = 'blog/base.html'
	return render(request,
		template_name=template_name,
		context=context)
	
