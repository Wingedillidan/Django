from django.conf.urls import url
from . import views

# initstring = '(?P<question_id>[0-9]+)'


# def urlfunc(pagestring, func, url_name):
#     if not pagestring:
#         regex = r'^' + initstring + '/$'
#     else:
#         regex = r'^' + initstring + '/' + pagestring + '/$'

#     return url(regex, func, name=url_name)

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
        name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # urlfunc('', views.detail, 'detail'),
    # urlfunc('results', views.results, 'results'),
    # urlfunc('vote', views.vote, 'vote'),
    ]
