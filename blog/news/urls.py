from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('contact',views.contact,name='contact'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('search/', views.search_results, name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 