from django.conf.urls.defaults import *

urlpatterns = patterns('listManager.views',
    (r'^$', 'index'),
    (r'^upload_file/$', 'upload_file'),
    (r'^thanks/$', 'thanks'),
)