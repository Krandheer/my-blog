
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<str:slug>/', views.post_detail, name='post_detail'),
   	path('contact/', views.contact_page, name = 'contact_page'),
   	path('about/', views.about_page, name = 'about_page'),
    path('bookshelf/', views.bookshelf_page, name='bookshelf_page'),
    path('s/', views.search, name='search'),
]
