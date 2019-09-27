from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import cms2017
from django.db.models import Q
from .models import SchoolResourcesFilter
from django.core.serializers import serialize
from .models import regions
from djgeojson.views import GeoJSONLayerView
from django.core.cache import cache
from .models import SchoolFilterSmall
from django.db.models import Avg, Sum




class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"


# class RegionsMapView(TemplateView):
#     template_name = "about.html"

def school_list2(request):
    year_list = cms2017.objects.values().order_by('school_nam')
    filtered_qs = SchoolResourcesFilter(request.GET, queryset = year_list)

    paginator = Paginator(filtered_qs.qs, 20)

    page = request.GET.get('page')
    
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)


    return render(
        request, 
        'schools_list.html', 
        {'response': response, 'year_filter': filtered_qs})



def SchoolProfileView(request, school_name, region, district):
    #f = SchoolFilterSmall(request.GET, queryset=DjangoTest.objects.all())
    #context = {'filter': f}
    school = cms2017.objects.filter(Q(school_nam=school_name) & Q(region=region) & Q(district=district))
    print(school)
    return render(request, 'table_creator.html', {'school_id': school})


def FullMapData(request):
    #f = SchoolFilterSmall(request.GET, queryset=DjangoTest.objects.all())
    #context = {'filter': f}
    # f = SchoolFilterSmall(request.GET, queryset=cms2017.objects.all()[0:50])

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            region_choice = form.cleaned_data['region_choice']
            q = cms2017.objects.filter(region=region_choice)

            print("FORM:", form)
            print(region_choice)
    else:
        form = RegionForm()
        print("FORM:", form)
        q = cms2017.objects.filter(region='ARMM')

    return render(request, 'full_map.html', {'filter': q, 'form': form})


def RegionsMapView(request):
    print(regions.objects.all())
    regions_geojson = serialize('geojson', regions.objects.all(), fields=('Region_Nam', 'original_internet_boolean'))
    return render(request, 'regions_map.html', {"regions_geojson": regions_geojson})

    #regions_shp = regions.objects.all()
    #return render(request, 'regions_map.html', {"regions_shp": regions_shp})

from .models import regions2
from .models import districts
from .models import divisions
from .models import regions_simple

from django.http import HttpResponse

def regions_view(request):
    # regions_geojson = serialize('geojson', regions2.objects.all())
    # return HttpResponse(regions_geojson, content_type='json')

    redis_key = 'regions'
    regions = cache.get(redis_key)  # getting value for given key from redis
    if not regions:
        regions = serialize('geojson', regions2.objects.all())
        cache.set(redis_key, regions)  # if not GeoJSON is not in cache set it
    return HttpResponse(regions, content_type='json')


class regions_shp_view(TemplateView):
    template_name = 'regions_polygons.html'



def regions_simple_view(request):
    # regions_geojson = serialize('geojson', regions2.objects.all())
    # return HttpResponse(regions_geojson, content_type='json')

    redis_key = 'RegionsSimple'
    RegionsSimple = cache.get(redis_key)  # getting value for given key from redis
    if not RegionsSimple:
        RegionsSimple = serialize('geojson', regions_simple.objects.all())
        cache.set(redis_key, RegionsSimple)  # if not GeoJSON is not in cache set it
    return HttpResponse(RegionsSimple, content_type='json')


class regions_simple_shp_view(TemplateView):
    template_name = 'regions_simple.html'



def districts_view(request):
    print(districts.objects.all())
    redis_key = 'Districts'
    Districts = cache.get(redis_key)  # getting value for given key from redis
    if not Districts:
        Districts = serialize('geojson', districts.objects.all())
        cache.set(redis_key, Districts)  # if not GeoJSON is not in cache set it
    return HttpResponse(Districts, content_type='json')


class districts_shp_view(TemplateView):
    template_name = 'district_polygons.html'


# def districts_view(request):
#     # print(divsions.objects.all())
#     redis_key = 'Divsions'
#     Divsions = cache.get(redis_key)  # getting value for given key from redis
#     if not Divsions:
#         Divsions = serialize('geojson', divsions.objects.all())
#         cache.set(redis_key, Divsions)  # if not GeoJSON is not in cache set it
#     return HttpResponse(Divsions, content_type='json')


# class districts_shp_view(TemplateView):
#     template_name = 'district_polygons.html'





from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import InputForm
from geo_cms import compute
from geo_cms.CalculateIndex import calculateyo
import os
from .models import IndexInputForm

def IndexCalculator(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.A, form2.b, form2.w, form2.T)
            result = result.replace('static/', '')
    else:
        form = InputForm()

    return render_to_response(request, 'vib1.html',
            {'form': form,
             'result': result,
             })


def sniIndexCalculator(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    print("yo")
    if request.method == 'POST':
        print('heeeerrrreeee')
        form = IndexInputForm(request.POST)
        if form.is_valid():
            print('we here')
            form2 = form.save(commit=False)
            result = calculateyo(form2.Geographic_Breakdown, form2.Remoteness, form2.Percentage_CCT, form2.Water_Access, form2.Internet_Access, form2.Electricity_Access, form2.Student_Teacher_Ratio, form2.Student_Classroom_Ratio,  form2.Accessibility_Category_Weight, form2.Amentities_Category_Weight, form2.Conditions_Category_Weight)
            mean = result.aggregate(Avg('final_index'))
            top_twenty = result.order_by('-final_index')[0:20]
            print('top twenty', top_twenty)
            print("result here:", result)
            #result = result.replace('static/', '')
    else:
        print('aqqqquuuuiiiii')
        form = IndexInputForm()
        form2 = form.save(commit=False)
        result = calculateyo(form2.Geographic_Breakdown, form2.Remoteness, form2.Percentage_CCT, form2.Water_Access, form2.Internet_Access, form2.Electricity_Access, form2.Student_Teacher_Ratio, form2.Student_Classroom_Ratio, form2.Accessibility_Category_Weight, form2.Amentities_Category_Weight, form2.Conditions_Category_Weight)
        mean = result.aggregate(Avg('final_index'))
        top_twenty = result.order_by('-final_index')[0:20]
        print('top_twenty', top_twenty)

    return render(request, 'vib1.html',
            {'form':form, 'result':result, 'mean':mean, 'top':top_twenty})





def map_try_view(request):
    #f = SchoolFilterSmall(request.GET, queryset=DjangoTest.objects.all())
    #context = {'filter': f}
    query = cms2017.objects.all()[0:50]
    return render(request, 'map_try.html', {'query': query})



class DataPage(TemplateView):
    template_name = "opendata.html"




import csv
from django.http import HttpResponse
from djqscsv import render_to_csv_response
from geodjango.forms import SimpleForm
from .models import LalaForm
from itertools import chain
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from geo_cms.DownloadSchoolResourceData import DownloadData


def SchoolResourcesData(request):
    query = cms2017.objects.all()
    # form = SimpleForm(request.POST)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimpleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # columns = form.cleaned_data['columns']
            # remote_query = cms2017.objects.values(columns[0])
            # cct_query = cms2017.objects.values(columns[1])
            # print("COLUMNS:", columns)
            request.session['columns'] = form.cleaned_data['columns']
            return redirect('/OpenData/SchoolResourcesData/csvDownload/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimpleForm()

    return render(request, 'SchoolResourcesData.html', {'query': query, 'form': form})



def csvView(request):
    cols = request.session.get('columns')
    df = DownloadData(cols)
    results = pd.Dataframe()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename.csv'

    df.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
    return response

    # qs = cms2017.objects.all()[0:10]
    # return render_to_csv_response(cms2017.objects.all()[0:500])



from .models import LguSpending, RegionalSpending
from geodjango.forms import RegionForm

def SpecialEdFundView(request):


    # form = SimpleForm(request.POST)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            region_choice = form.cleaned_data['region_choice']
            q = RegionalSpending.objects.using('local').filter(region=region_choice)
            request.session['region_choice'] = form.cleaned_data['region_choice']


            print("FORM:", form)
            print(region_choice)
    else:
        form = RegionForm()
        print("FORM:", form)
        q = RegionalSpending.objects.using('local').filter(region='ARMM')


    # q = RegionalSpending.objects.using('local').filter(region=region_choice)
    ga_sum = q.aggregate(Sum('general_administration'))
    es_sum = q.aggregate(Sum('elementary_school'))
    ss_sum = q.aggregate(Sum('secondary_school'))
    uces_sum = q.aggregate(Sum('university_college_education_school'))
    vct_sum = q.aggregate(Sum('vocational_technical_school'))
    ae_sum = q.aggregate(Sum('adult_education'))
    ess_sum = q.aggregate(Sum('education_subsidiary_services'))
    mdmt_sum = q.aggregate(Sum('manpower_development_mangement_tool'))
    rec_sum = q.aggregate(Sum('maintenance_of_sports_center_athletic_fields_playground'))


    return render(request, 'SpecialEdFundView.html', {'response': q, 'ga_sum': ga_sum,  'es_sum':es_sum,'ss_sum':ss_sum, 'uces_sum':uces_sum,
    'vct_sum':vct_sum, 'ae_sum':ae_sum, 'ess_sum':ess_sum, 'mdmt_sum':mdmt_sum, 'rec_sum':rec_sum, 'form': form})



def SEFcsvView(request):
    # hay = request.session.get('columns')
    # print("CSV VIEW", hay)
    qs = RegionalSpending.objects.using('local').all()
    return render_to_csv_response(qs)


 
#  def MergePage(request):
#      qs = RegionalSpending.objects.using('local').all()
