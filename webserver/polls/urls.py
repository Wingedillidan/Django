from django.conf.urls import url
from . import views

initstring = '(?P<question_id>[0-9]+)'


def urlfunc(pagestring, func, url_name):
    if not pagestring:
        regex = r'^' + initstring + '/$'
    else:
        regex = r'^' + initstring + '/' + pagestring + '/$'

    return url(regex, func, name=url_name)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    urlfunc('', views.detail, 'detail'),
    urlfunc('results', views.results, 'results'),
    urlfunc('vote', views.vote, 'vote'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results,
    #     name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    ]
