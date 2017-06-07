from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('overview/$', views.overview, name="browse-page"),
    url("search/$", views.get_search_page, name="search-page"),
    url("import/$", views.import_data, name="import-page"),
    url("search/result/", views.search, name="search"),
    url("search/getrecords/(?P<texture>\w+)/(?P<process>\w+)/(?P<start_date_str>\d{4}-\d{1,2}-\d{1,2})/(?P<end_date_str>\d{4}-\d{1,2}-\d{1,2})/$", views.get_records, name="get-records"),
    url("account/login", views.user_login, name="login"),
    url("account/logout", views.user_logout, name="logout"),
    url("import_data", views.import_data, name="import-data")
]