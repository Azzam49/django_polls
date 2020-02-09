from django.urls import path
from . import views

''' 
    Changing this url's to be class-based urls
    # ex: /polls/
    path('', views.pollView, name='index-view'),
    
    # ex : /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
'''

#namespace, to reach this app by url, even if another apps have same views.
# usement on template url : {% url 'polls:detail' question_id %}
app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index-view'),
    
    # ex : /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


#contrling url:

#html link - clicking link passes question.id to the url 
#<a href="/polls/{{ question.id }}/">

#then to

#urls - handles the question.id , passes it to the view and call it
# <int:question_id> , using angle brackets tells that
# question_id is a argument to be passed to the
# view . <int: is a converter to integer.

#view - recives the question.id argument and runs codes
#detail(request=<HttpRequest object>, question_id=34)