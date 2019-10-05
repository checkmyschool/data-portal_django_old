"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from geo_cms import views
from django.urls import path
from djgeojson.views import GeoJSONLayerView
#If you use .models here it will read this in from the app folder but its in in the geo_cms project folder
from geo_cms.models import regions
from geo_cms.views import regions_view, regions_shp_view, districts_view, districts_shp_view, map_try_view, regions_simple_view, regions_simple_shp_view, SchoolResourcesData, csvView, SpecialEdFundView


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^$', views.HomePageView),
    url(r'^sni_method/$', views.SNIMethodView.as_view()),


    path('schools_list/', views.school_list2),
    path('schools_list/<str:school_name>/<str:region>/<str:district>/', views.SchoolProfileView),
    path('regions_map/', views.RegionsMapView),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=regions), name='data'),

    path('full_map/', views.FullMapData),

    path('IndexCalculator/', views.sniIndexCalculator),

    path('OpenData/SchoolResourcesData/', views.SchoolResourcesData),
    path('OpenData/SchoolResourcesData/csvDownload/', views.csvView),

    path('OpenData/SpecialEducationFund/', views.SpecialEdFundView),
    path('OpenData/SpecialEducationFund/csvDownload/', views.SEFcsvView),





    ####REGIONS####
    #Makes the GeoJSON page#
    url(r'^regions2.data/', regions_view, name='RegionPolys'),
    #TemplateView that users see#
    url(r'^regions_hopefully/$', regions_shp_view.as_view()),

    ####REGIONS SIMPLE####
    url(r'^regions_simple.data/', regions_simple_view, name='RegionSimplePolys'),
    url(r'^regions_simple_map/$', regions_simple_shp_view.as_view()),

    url(r'^OpenData/$', views.DataPage.as_view()),


    ####DISTRICTS####
    #Makes the GeoJSON page#
    url(r'^districts.data/', districts_view, name='DistrictPolys'),
    #TemplateView that users see#
    url(r'^districts_map/$', districts_shp_view.as_view()),

    ####DIVISIONS####
    #Makes the GeoJSON page#
    # url(r'^divisions.data/', divisions_view, name='DivisionPolys'),
    #TemplateView that users see#
    # url(r'^districts_map/$', districts_shp_view.as_view()),

    path('map_try/', views.map_try_view),

]
