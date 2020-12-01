from django.urls import path

from . import views

urlpatterns = [
    path('',views.GreetingView.as_view(),name ='card'),
    # path('',views.home,name ='home'),
    # path('card',views.card,name='card'),
    path('about',views.about,name ='about'),
    path('services',views.services,name = 'services'),
    path('contacts',views.contacts,name = 'contacts'),
    
]
