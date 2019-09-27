from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class cms2017(models.Model):
    field_1 = models.BigIntegerField()
    X = models.BigIntegerField()
    school_yea = models.BigIntegerField()
    school_id = models.IntegerField(blank=True)
    cluster = models.BigIntegerField()
    remoteness = models.FloatField()
    total_reci = models.BigIntegerField()
    cct_percen = models.FloatField()
    comments = models.CharField(max_length=254)
    original_w = models.CharField(max_length=254)
    nowater = models.BigIntegerField()
    original_i = models.CharField(max_length=254)
    no_interne = models.BigIntegerField()
    noelec = models.BigIntegerField()
    original_e = models.CharField(max_length=254)
    instructio = models.BigIntegerField()
    student_cl = models.FloatField()
    total_teac = models.BigIntegerField()
    student_te = models.FloatField()
    remotene_1 = models.FloatField()
    cct_perc_1 = models.FloatField()
    nowater_sc = models.BigIntegerField()
    no_inter_1 = models.BigIntegerField()
    noelec_sca = models.BigIntegerField()
    scr_s = models.FloatField()
    str_s = models.FloatField()
    remotene_2 = models.FloatField()
    cct_perc_2 = models.FloatField()
    electricit = models.FloatField()
    water_bool = models.FloatField()
    internet_b = models.FloatField()
    str_s2 = models.FloatField()
    scr_s2 = models.FloatField()
    accessibil = models.FloatField()
    amenities = models.FloatField()
    conditions = models.FloatField()
    shi_score = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    school_nam = models.CharField(max_length=254, primary_key=True)
    region = models.CharField(max_length=254)
    division = models.CharField(max_length=254)
    province = models.CharField(max_length=254)
    municipali = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    total_fema = models.BigIntegerField()
    total_male = models.BigIntegerField()
    total_enro = models.BigIntegerField()
    ds_total = models.BigIntegerField()
    cp_total = models.BigIntegerField()
    dcm_total = models.BigIntegerField()
    drcpau_tot = models.BigIntegerField()
    dh_total = models.BigIntegerField()
    autism_tot = models.BigIntegerField()
    wcg_total = models.BigIntegerField()
    eb_total = models.BigIntegerField()
    hi_total = models.BigIntegerField()
    id_total = models.BigIntegerField()
    li_total = models.BigIntegerField()
    md_total = models.BigIntegerField()
    pd_total = models.BigIntegerField()
    shp_total = models.BigIntegerField()
    speech_tot = models.BigIntegerField()
    vi_total = models.BigIntegerField()
    ii_total = models.BigIntegerField()
    p_total = models.BigIntegerField()
    pwd_total = models.BigIntegerField()
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'cms2017'




class regions(models.Model):
    Region_Nam = models.CharField(max_length=80, blank=True, primary_key=True)
    Shape_Leng = models.FloatField()
    Shape_Area = models.FloatField()
    X = models.IntegerField()
    unnm_0 = models.FloatField(db_column='Unnamed..0')
    school_year = models.FloatField()
    school_id = models.FloatField()
    remoteness_index = models.FloatField()
    total_recieving_cct = models.FloatField()
    cct_percentage = models.FloatField()
    original_water_boolean = models.FloatField()
    nowater = models.FloatField()
    original_internet_boolean = models.FloatField()
    no_internet = models.FloatField()
    noelec = models.FloatField()
    original_electricity_boolean = models.FloatField()
    instructional_rooms = models.FloatField(db_column = "instructional__rooms_")
    student_classroom_ratio = models.FloatField()
    total_teachers = models.FloatField()
    student_teacher_ratio = models.FloatField()
    remoteness_index_scaled = models.FloatField()
    cct_percentage_scaled = models.FloatField()
    nowater_scaled = models.FloatField()
    no_internet_scaled = models.FloatField()
    noelec_scaled = models.FloatField()
    student_classroom_ratio_scaled = models.FloatField()
    student_teacher_ratio_scaled = models.FloatField()
    remoteness_index_scaled2 = models.FloatField()
    cct_percentage_scaled2 = models.FloatField()
    electricity_boolean_reversed_scaled2 = models.FloatField()
    water_boolean_reversed_scaled2 = models.FloatField()
    internet_boolean_reversed_scaled2 = models.FloatField()
    student_teacher_ratio_scaled2 = models.FloatField()
    student_classroom_ratio_scaled2 = models.FloatField()
    accessibility = models.FloatField()
    amenities = models.FloatField()
    conditions = models.FloatField()
    shi_score = models.FloatField()
    longitude = models.FloatField()
    total_female = models.FloatField()
    total_male = models.FloatField()
    total_enrollment = models.FloatField()
    ds_total = models.FloatField()
    cp_total = models.FloatField()
    dcm_total = models.FloatField()
    drcpau_total = models.FloatField()
    dh_total = models.FloatField()
    autism_total = models.FloatField()
    wcg_total = models.FloatField()
    eb_total = models.FloatField()
    hi_total = models.FloatField()
    id_total = models.FloatField()
    li_total = models.FloatField()
    md_total = models.FloatField()
    pd_total = models.FloatField()
    shp_total = models.FloatField()
    speech_total = models.FloatField()
    vi_total = models.FloatField()
    ii_total = models.FloatField()
    p_total = models.FloatField()
    pwd_total = models.FloatField()
    geom = models.PolygonField()

    class Meta:
        managed = False
        db_table = 'regions'



##FILTER MODELS##
import django_filters

class SchoolResourcesFilter(django_filters.FilterSet):
    school_yea = django_filters.NumberFilter()
    school_nam = django_filters.CharFilter(field_name = 'school_nam', lookup_expr = 'icontains')
    region = django_filters.CharFilter(field_name = 'region', lookup_expr = 'icontains')
    district = django_filters.CharFilter(field_name = 'district', lookup_expr = 'icontains')
    division = django_filters.CharFilter(field_name = 'division', lookup_expr = 'icontains')
    province = django_filters.CharFilter(field_name = 'province', lookup_expr = 'icontains')

    class Meta:
        model = cms2017
        fields = ['school_yea', 'school_nam', 'region', 'district', 'division', 'province']# This is an auto-generated Django model module created by ogrinspect.


from django.contrib.gis.db import models


class regions2(models.Model):
    regn_nm = models.CharField(max_length=80, null=True, blank=True)
    shp_lng = models.FloatField(null=True, blank=True)
    shap_ar = models.FloatField(null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    unnm_0 = models.FloatField(null=True, blank=True)
    schl_yr = models.FloatField(null=True, blank=True)
    schol_d = models.FloatField(null=True, blank=True)
    rmtnss_field = models.FloatField(null=True, blank=True)
    ttl_rc_field = models.FloatField(null=True, blank=True)
    cct_prc = models.FloatField(null=True, blank=True)
    orgnl_w_field = models.FloatField(null=True, blank=True)
    nowater = models.FloatField(null=True, blank=True)
    orgnl_n_field = models.FloatField(null=True, blank=True)
    n_ntrnt = models.FloatField(null=True, blank=True)
    noelec = models.FloatField(null=True, blank=True)
    orgnl_l_field = models.FloatField(null=True, blank=True)
    inst_field = models.FloatField(null=True, blank=True)
    stdnt_c_field = models.FloatField(null=True, blank=True)
    ttl_tch = models.FloatField(null=True, blank=True)
    stdnt_t_field = models.FloatField(null=True, blank=True)
    rmtns_field = models.FloatField(null=True, blank=True)
    cct_pr_field = models.FloatField(null=True, blank=True)
    nwtr_sc = models.FloatField(null=True, blank=True)
    n_ntrn_field = models.FloatField(null=True, blank=True)
    nlc_scl = models.FloatField(null=True, blank=True)
    stdnt_c_field = models.FloatField(null=True, blank=True)
    stdnt_t_field = models.FloatField(null=True, blank=True)
    rmtn_2 = models.FloatField(null=True, blank=True)
    cct_p_2 = models.FloatField(null=True, blank=True)
    elc_2 = models.FloatField(null=True, blank=True)
    wtr_2 = models.FloatField(null=True, blank=True)
    int_2 = models.FloatField(null=True, blank=True)
    stdnt_t_2 = models.FloatField(null=True, blank=True)
    stdnt_c_2 = models.FloatField(null=True, blank=True)
    accssbl = models.FloatField(null=True, blank=True)
    amenits = models.FloatField(null=True, blank=True)
    condtns = models.FloatField(null=True, blank=True)
    shi_scr = models.FloatField(null=True, blank=True)
    longitd = models.FloatField(null=True, blank=True)
    ttl_fml = models.FloatField(null=True, blank=True)
    totl_ml = models.FloatField(null=True, blank=True)
    ttl_nrl = models.FloatField(null=True, blank=True)
    ds_totl = models.FloatField(null=True, blank=True)
    cp_totl = models.FloatField(null=True, blank=True)
    dcm_ttl = models.FloatField(null=True, blank=True)
    drcp_tt = models.FloatField(null=True, blank=True)
    dh_totl = models.FloatField(null=True, blank=True)
    atsm_tt = models.FloatField(null=True, blank=True)
    wcg_ttl = models.FloatField(null=True, blank=True)
    eb_totl = models.FloatField(null=True, blank=True)
    hi_totl = models.FloatField(null=True, blank=True)
    id_totl = models.FloatField(null=True, blank=True)
    li_totl = models.FloatField(null=True, blank=True)
    md_totl = models.FloatField(null=True, blank=True)
    pd_totl = models.FloatField(null=True, blank=True)
    shp_ttl = models.FloatField(null=True, blank=True)
    spch_tt = models.FloatField(null=True, blank=True)
    vi_totl = models.FloatField(null=True, blank=True)
    ii_totl = models.FloatField(null=True, blank=True)
    p_total = models.FloatField(null=True, blank=True)
    pwd_ttl = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(geography=True, srid=4326)

    def __str__(self):
        return '{}'.format(self.regn_nm)

    def __unicode__(self):
        return '{}'.format(self.regn_nm)


# Auto-generated `LayerMapping` dictionary for regions2 model
regions2_mapping = {
    'regn_nm': 'Regn_Nm',
    'shp_lng': 'Shp_Lng',
    'shap_ar': 'Shap_Ar',
    'x': 'X',
    'unnm_0': 'Unnm__0',
    'schl_yr': 'schl_yr',
    'schol_d': 'schol_d',
    'rmtnss_field': 'rmtnss_',
    'ttl_rc_field': 'ttl_rc_',
    'cct_prc': 'cct_prc',
    'orgnl_w_field': 'orgnl_w_',
    'nowater': 'nowater',
    'orgnl_n_field': 'orgnl_n_',
    'n_ntrnt': 'n_ntrnt',
    'noelec': 'noelec',
    'orgnl_l_field': 'orgnl_l_',
    'inst_field': 'inst___',
    'stdnt_c_field': 'stdnt_c_',
    'ttl_tch': 'ttl_tch',
    'stdnt_t_field': 'stdnt_t_',
    'rmtns_field': 'rmtns__',
    'cct_pr_field': 'cct_pr_',
    'nwtr_sc': 'nwtr_sc',
    'n_ntrn_field': 'n_ntrn_',
    'nlc_scl': 'nlc_scl',
    'stdnt_c_field': 'stdnt_c__',
    'stdnt_t_field': 'stdnt_t__',
    'rmtn_2': 'rmtn__2',
    'cct_p_2': 'cct_p_2',
    'elc_2': 'elc___2',
    'wtr_2': 'wtr___2',
    'int_2': 'int___2',
    'stdnt_t_2': 'stdnt_t__2',
    'stdnt_c_2': 'stdnt_c__2',
    'accssbl': 'accssbl',
    'amenits': 'amenits',
    'condtns': 'condtns',
    'shi_scr': 'shi_scr',
    'longitd': 'longitd',
    'ttl_fml': 'ttl_fml',
    'totl_ml': 'totl_ml',
    'ttl_nrl': 'ttl_nrl',
    'ds_totl': 'ds_totl',
    'cp_totl': 'cp_totl',
    'dcm_ttl': 'dcm_ttl',
    'drcp_tt': 'drcp_tt',
    'dh_totl': 'dh_totl',
    'atsm_tt': 'atsm_tt',
    'wcg_ttl': 'wcg_ttl',
    'eb_totl': 'eb_totl',
    'hi_totl': 'hi_totl',
    'id_totl': 'id_totl',
    'li_totl': 'li_totl',
    'md_totl': 'md_totl',
    'pd_totl': 'pd_totl',
    'shp_ttl': 'shp_ttl',
    'spch_tt': 'spch_tt',
    'vi_totl': 'vi_totl',
    'ii_totl': 'ii_totl',
    'p_total': 'p_total',
    'pwd_ttl': 'pwd_ttl',
    'geom': 'MULTIPOLYGON',
}



# class regions3(models.Model):
#     region_nam = models.CharField(max_length=254)
#     shape_leng = models.FloatField()
#     shape_area = models.FloatField()
#     geom = models.PolygonField()


# # Auto-generated `LayerMapping` dictionary for regions3 model
# regions3_mapping = {
#     'region_nam': 'Region_Nam',
#     'shape_leng': 'Shape_Leng',
#     'shape_area': 'Shape_Area',
#     'geom': 'POLYGON',
# }# This is an auto-generated Django model module created by ogrinspect.
# from django.contrib.gis.db import models


class districts(models.Model):
    dstrc_n = models.CharField(max_length=80)
    shp_lng = models.FloatField(null=True, blank=True)
    shap_ar = models.FloatField(null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    unnm_0 = models.FloatField(null=True, blank=True)
    schl_yr = models.FloatField(null=True, blank=True)
    schol_d = models.FloatField(null=True, blank=True)
    rmtnss_field = models.FloatField(null=True, blank=True)
    ttl_rc_field = models.FloatField(null=True, blank=True)
    cct_prc = models.FloatField(null=True, blank=True)
    orgnl_w_field = models.FloatField(null=True, blank=True)
    nowater = models.FloatField(null=True, blank=True)
    orgnl_n_field = models.FloatField(null=True, blank=True)
    n_ntrnt = models.FloatField(null=True, blank=True)
    noelec = models.FloatField(null=True, blank=True)
    orgnl_l_field = models.FloatField(null=True, blank=True)
    inst_field = models.FloatField(null=True, blank=True)
    stdnt_c_field = models.FloatField(null=True, blank=True)
    ttl_tch = models.FloatField(null=True, blank=True)
    stdnt_t_field = models.FloatField(null=True, blank=True)
    rmtns_field = models.FloatField(null=True, blank=True)
    cct_pr_field = models.FloatField(null=True, blank=True)
    nwtr_sc = models.FloatField(null=True, blank=True)
    n_ntrn_field = models.FloatField(null=True, blank=True)
    nlc_scl = models.FloatField(null=True, blank=True)
    stdnt_t_field = models.FloatField(null=True, blank=True)
    stdnt_c_field = models.FloatField(null=True, blank=True)
    rmtn_2 = models.FloatField(null=True, blank=True)
    cct_p_2 = models.FloatField(null=True, blank=True)
    elc_2 = models.FloatField(null=True, blank=True)
    wtr_2 = models.FloatField(null=True, blank=True)
    int_2 = models.FloatField(null=True, blank=True)
    stdnt_t_2 = models.FloatField(null=True, blank=True)
    stdnt_c_2 = models.FloatField(null=True, blank=True)
    accssbl = models.FloatField(null=True, blank=True)
    amenits = models.FloatField(null=True, blank=True)
    condtns = models.FloatField(null=True, blank=True)
    shi_scr = models.FloatField(null=True, blank=True)
    longitd = models.FloatField(null=True, blank=True)
    ttl_fml = models.FloatField(null=True, blank=True)
    totl_ml = models.FloatField(null=True, blank=True)
    ttl_nrl = models.FloatField(null=True, blank=True)
    ds_totl = models.FloatField(null=True, blank=True)
    cp_totl = models.FloatField(null=True, blank=True)
    dcm_ttl = models.FloatField(null=True, blank=True)
    drcp_tt = models.FloatField(null=True, blank=True)
    dh_totl = models.FloatField(null=True, blank=True)
    atsm_tt = models.FloatField(null=True, blank=True)
    wcg_ttl = models.FloatField(null=True, blank=True)
    eb_totl = models.FloatField(null=True, blank=True)
    hi_totl = models.FloatField(null=True, blank=True)
    id_totl = models.FloatField(null=True, blank=True)
    li_totl = models.FloatField(null=True, blank=True)
    md_totl = models.FloatField(null=True, blank=True)
    pd_totl = models.FloatField(null=True, blank=True)
    shp_ttl = models.FloatField(null=True, blank=True)
    spch_tt = models.FloatField(null=True, blank=True)
    vi_totl = models.FloatField(null=True, blank=True)
    ii_totl = models.FloatField(null=True, blank=True)
    p_total = models.FloatField(null=True, blank=True)
    pwd_ttl = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(geography=True, srid=4326)

    def __str__(self):
        return '{}'.format(self.dstrc_n)

    def __unicode__(self):
        return '{}'.format(self.dstrc_n)


# Auto-generated `LayerMapping` dictionary for regions2 model
districts_mapping = {
    'dstrc_n': 'Dstrc_N',
    'shp_lng': 'Shp_Lng',
    'shap_ar': 'Shap_Ar',
    'x': 'X',
    'unnm_0': 'Unnm__0',
    'schl_yr': 'schl_yr',
    'schol_d': 'schol_d',
    'rmtnss_field': 'rmtnss_',
    'ttl_rc_field': 'ttl_rc_',
    'cct_prc': 'cct_prc',
    'orgnl_w_field': 'orgnl_w_',
    'nowater': 'nowater',
    'orgnl_n_field': 'orgnl_n_',
    'n_ntrnt': 'n_ntrnt',
    'noelec': 'noelec',
    'orgnl_l_field': 'orgnl_l_',
    'inst_field': 'inst___',
    'stdnt_c_field': 'stdnt_c_',
    'ttl_tch': 'ttl_tch',
    'stdnt_t_field': 'stdnt_t_',
    'rmtns_field': 'rmtns__',
    'cct_pr_field': 'cct_pr_',
    'nwtr_sc': 'nwtr_sc',
    'n_ntrn_field': 'n_ntrn_',
    'nlc_scl': 'nlc_scl',
    'stdnt_c_field': 'stdnt_c__',
    'stdnt_t_field': 'stdnt_t__',
    'rmtn_2': 'rmtn__2',
    'cct_p_2': 'cct_p_2',
    'elc_2': 'elc___2',
    'wtr_2': 'wtr___2',
    'int_2': 'int___2',
    'stdnt_t_2': 'stdnt_t__2',
    'stdnt_c_2': 'stdnt_c__2',
    'accssbl': 'accssbl',
    'amenits': 'amenits',
    'condtns': 'condtns',
    'shi_scr': 'shi_scr',
    'longitd': 'longitd',
    'ttl_fml': 'ttl_fml',
    'totl_ml': 'totl_ml',
    'ttl_nrl': 'ttl_nrl',
    'ds_totl': 'ds_totl',
    'cp_totl': 'cp_totl',
    'dcm_ttl': 'dcm_ttl',
    'drcp_tt': 'drcp_tt',
    'dh_totl': 'dh_totl',
    'atsm_tt': 'atsm_tt',
    'wcg_ttl': 'wcg_ttl',
    'eb_totl': 'eb_totl',
    'hi_totl': 'hi_totl',
    'id_totl': 'id_totl',
    'li_totl': 'li_totl',
    'md_totl': 'md_totl',
    'pd_totl': 'pd_totl',
    'shp_ttl': 'shp_ttl',
    'spch_tt': 'spch_tt',
    'vi_totl': 'vi_totl',
    'ii_totl': 'ii_totl',
    'p_total': 'p_total',
    'pwd_ttl': 'pwd_ttl',
    'geom': 'MULTIPOLYGON',
}



class divisions(models.Model):
    divsn_n = models.CharField(max_length=80)
    shp_lng = models.FloatField(null=True, blank=True)
    shap_ar = models.FloatField(null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    unnm_0 = models.FloatField(null=True, blank=True)
    schl_yr = models.FloatField(null=True, blank=True)
    schol_d = models.FloatField(null=True, blank=True)
    rmtnss_field = models.FloatField(null=True, blank=True)
    ttl_rc_field = models.FloatField(null=True, blank=True)
    cct_prc = models.FloatField(null=True, blank=True)
    orgnl_w_field = models.FloatField(null=True, blank=True)
    nowater = models.FloatField(null=True, blank=True)
    orgnl_n_field = models.FloatField(null=True, blank=True)
    n_ntrnt = models.FloatField(null=True, blank=True)
    noelec = models.FloatField(null=True, blank=True)
    orgnl_l_field = models.FloatField(null=True, blank=True)
    inst_field = models.FloatField(null=True, blank=True)
    stdnt_c_field = models.FloatField(null=True, blank=True)
    ttl_tch = models.FloatField(null=True, blank=True)
    stdnt_t_field = models.FloatField(null=True, blank=True)
    rmtns_field = models.FloatField(null=True, blank=True)
    cct_pr_field = models.FloatField(null=True, blank=True)
    nwtr_sc = models.FloatField(null=True, blank=True)
    n_ntrn_field = models.FloatField(null=True, blank=True)
    nlc_scl = models.FloatField(null=True, blank=True)
    stdnt_c_field = models.FloatField(null=True, blank=True)
    stdnt_t_field = models.FloatField(null=True, blank=True)
    rmtn_2 = models.FloatField(null=True, blank=True)
    cct_p_2 = models.FloatField(null=True, blank=True)
    elc_2 = models.FloatField(null=True, blank=True)
    wtr_2 = models.FloatField(null=True, blank=True)
    int_2 = models.FloatField(null=True, blank=True)
    stdnt_t_2 = models.FloatField(null=True, blank=True)
    stdnt_c_2 = models.FloatField(null=True, blank=True)
    accssbl = models.FloatField(null=True, blank=True)
    amenits = models.FloatField(null=True, blank=True)
    condtns = models.FloatField(null=True, blank=True)
    shi_scr = models.FloatField(null=True, blank=True)
    longitd = models.FloatField(null=True, blank=True)
    ttl_fml = models.FloatField(null=True, blank=True)
    totl_ml = models.FloatField(null=True, blank=True)
    ttl_nrl = models.FloatField(null=True, blank=True)
    ds_totl = models.FloatField(null=True, blank=True)
    cp_totl = models.FloatField(null=True, blank=True)
    dcm_ttl = models.FloatField(null=True, blank=True)
    drcp_tt = models.FloatField(null=True, blank=True)
    dh_totl = models.FloatField(null=True, blank=True)
    atsm_tt = models.FloatField(null=True, blank=True)
    wcg_ttl = models.FloatField(null=True, blank=True)
    eb_totl = models.FloatField(null=True, blank=True)
    hi_totl = models.FloatField(null=True, blank=True)
    id_totl = models.FloatField(null=True, blank=True)
    li_totl = models.FloatField(null=True, blank=True)
    md_totl = models.FloatField(null=True, blank=True)
    pd_totl = models.FloatField(null=True, blank=True)
    shp_ttl = models.FloatField(null=True, blank=True)
    spch_tt = models.FloatField(null=True, blank=True)
    vi_totl = models.FloatField(null=True, blank=True)
    ii_totl = models.FloatField(null=True, blank=True)
    p_total = models.FloatField(null=True, blank=True)
    pwd_ttl = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(geography=True, srid=4326)

    def __str__(self):
        return '{}'.format(self.divsn_n)

    def __unicode__(self):
        return '{}'.format(self.divsn_n)


# Auto-generated `LayerMapping` dictionary for divisions model
divisions_mapping = {
    'divsn_n': 'Divsn_N',
    'shp_lng': 'Shp_Lng',
    'shap_ar': 'Shap_Ar',
    'x': 'X',
    'unnm_0': 'Unnm__0',
    'schl_yr': 'schl_yr',
    'schol_d': 'schol_d',
    'rmtnss_field': 'rmtnss_',
    'ttl_rc_field': 'ttl_rc_',
    'cct_prc': 'cct_prc',
    'orgnl_w_field': 'orgnl_w_',
    'nowater': 'nowater',
    'orgnl_n_field': 'orgnl_n_',
    'n_ntrnt': 'n_ntrnt',
    'noelec': 'noelec',
    'orgnl_l_field': 'orgnl_l_',
    'inst_field': 'inst___',
    'stdnt_c_field': 'stdnt_c_',
    'ttl_tch': 'ttl_tch',
    'stdnt_t_field': 'stdnt_t_',
    'rmtns_field': 'rmtns__',
    'cct_pr_field': 'cct_pr_',
    'nwtr_sc': 'nwtr_sc',
    'n_ntrn_field': 'n_ntrn_',
    'nlc_scl': 'nlc_scl',
    'stdnt_c_field': 'stdnt_c__',
    'stdnt_t_field': 'stdnt_t__',
    'rmtn_2': 'rmtn__2',
    'cct_p_2': 'cct_p_2',
    'elc_2': 'elc___2',
    'wtr_2': 'wtr___2',
    'int_2': 'int___2',
    'stdnt_t_2': 'stdnt_t__2',
    'stdnt_c_2': 'stdnt_c__2',
    'accssbl': 'accssbl',
    'amenits': 'amenits',
    'condtns': 'condtns',
    'shi_scr': 'shi_scr',
    'longitd': 'longitd',
    'ttl_fml': 'ttl_fml',
    'totl_ml': 'totl_ml',
    'ttl_nrl': 'ttl_nrl',
    'ds_totl': 'ds_totl',
    'cp_totl': 'cp_totl',
    'dcm_ttl': 'dcm_ttl',
    'drcp_tt': 'drcp_tt',
    'dh_totl': 'dh_totl',
    'atsm_tt': 'atsm_tt',
    'wcg_ttl': 'wcg_ttl',
    'eb_totl': 'eb_totl',
    'hi_totl': 'hi_totl',
    'id_totl': 'id_totl',
    'li_totl': 'li_totl',
    'md_totl': 'md_totl',
    'pd_totl': 'pd_totl',
    'shp_ttl': 'shp_ttl',
    'spch_tt': 'spch_tt',
    'vi_totl': 'vi_totl',
    'ii_totl': 'ii_totl',
    'p_total': 'p_total',
    'pwd_ttl': 'pwd_ttl',
    'geom': 'MULTIPOLYGON',
}






####FILTERS####
import django_filters

class SchoolFilterSmall(django_filters.FilterSet):

    school_name = django_filters.CharFilter(field_name = 'school_nam', lookup_expr = 'icontains')
    # region = django_filters.CharFilter(field_name = 'region')
    # total_enrollment = django_filters.NumberFilter()
    total_enro__gt = django_filters.NumberFilter(field_name = 'total_enro', lookup_expr = 'gt')
    total_enro__lt = django_filters.NumberFilter(field_name = 'total_enro', lookup_expr = 'lt')

    class Meta:
        model = cms2017
        fields = ['school_nam', 'total_enro']




####COMPUTATIONS####
from django.db import models
from django.forms import ModelForm
from math import pi

class Input(models.Model):
    A = models.FloatField(
        verbose_name=' amplitude (m)', default=1.0)
    b = models.FloatField(
        verbose_name=' damping coefficient (kg/s)', default=0.0)
    w = models.FloatField(
        verbose_name=' frequency (1/s)', default=2*pi)
    T = models.FloatField(
        verbose_name=' time interval (s)', default=18)

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['A', 'b', 'w', 'T']


class IndexInput(models.Model):
    Geographic_Breakdown = models.CharField(default = 'School', max_length=20)
    Remoteness = models.FloatField(default = .6)
    Percentage_CCT = models.FloatField(default = .4)
    Water_Access = models.FloatField(default = .4)
    Internet_Access = models.FloatField(default = .3)
    Electricity_Access = models.FloatField(default = .3)
    Student_Teacher_Ratio = models.FloatField(default = .5)
    Student_Classroom_Ratio = models.FloatField(default = .5)
    Accessibility_Category_Weight = models.FloatField(default = .35)
    Amentities_Category_Weight = models.FloatField(default = .35)
    Conditions_Category_Weight = models.FloatField(default = .30)


    # def _get_index(self):
    #     return (self.Remoteness * )

class IndexInputForm(ModelForm):
    class Meta:
        model = IndexInput
        fields = ['Geographic_Breakdown', 'Remoteness', 'Percentage_CCT', 'Water_Access', 'Internet_Access', 'Electricity_Access', 'Student_Teacher_Ratio', 'Student_Classroom_Ratio', 'Accessibility_Category_Weight', 'Amentities_Category_Weight', 'Conditions_Category_Weight']# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class regions_simple(models.Model):
    regn_nm = models.CharField(max_length=80)
    shp_lng = models.FloatField()
    shap_ar = models.FloatField()
    x = models.IntegerField()
    unnm_0 = models.FloatField()
    schl_yr = models.FloatField()
    schol_d = models.FloatField()
    rmtnss_field = models.FloatField()
    ttl_rc_field = models.FloatField()
    cct_prc = models.FloatField()
    orgnl_w_field = models.FloatField()
    nowater = models.FloatField()
    orgnl_n_field = models.FloatField()
    n_ntrnt = models.FloatField()
    noelec = models.FloatField()
    orgnl_l_field = models.FloatField()
    inst_field = models.FloatField()
    stdnt_c_field = models.FloatField()
    ttl_tch = models.FloatField()
    stdnt_t_field = models.FloatField()
    rmtns_field = models.FloatField()
    cct_pr_field = models.FloatField()
    nwtr_sc = models.FloatField()
    n_ntrn_field = models.FloatField()
    nlc_scl = models.FloatField()
    stdnt_c_field = models.FloatField()
    stdnt_t_field = models.FloatField()
    rmtn_2 = models.FloatField()
    cct_p_2 = models.FloatField()
    elc_2 = models.FloatField()
    wtr_2 = models.FloatField()
    int_2 = models.FloatField()
    stdnt_t_2 = models.FloatField()
    stdnt_c_2 = models.FloatField()
    accssbl = models.FloatField()
    amenits = models.FloatField()
    condtns = models.FloatField()
    shi_scr = models.FloatField()
    longitd = models.FloatField()
    ttl_fml = models.FloatField()
    totl_ml = models.FloatField()
    ttl_nrl = models.FloatField()
    ds_totl = models.FloatField()
    cp_totl = models.FloatField()
    dcm_ttl = models.FloatField()
    drcp_tt = models.FloatField()
    dh_totl = models.FloatField()
    atsm_tt = models.FloatField()
    wcg_ttl = models.FloatField()
    eb_totl = models.FloatField()
    hi_totl = models.FloatField()
    id_totl = models.FloatField()
    li_totl = models.FloatField()
    md_totl = models.FloatField()
    pd_totl = models.FloatField()
    shp_ttl = models.FloatField()
    spch_tt = models.FloatField()
    vi_totl = models.FloatField()
    ii_totl = models.FloatField()
    p_total = models.FloatField()
    pwd_ttl = models.FloatField()
    geom = models.MultiPolygonField(geography=True, srid=4326)

    def __str__(self):
        return '{}'.format(self.regn_nm)

    def __unicode__(self):
        return '{}'.format(self.regn_nm)


# Auto-generated `LayerMapping` dictionary for regions_simple model
regions_simple_mapping = {
    'regn_nm': 'Regn_Nm',
    'shp_lng': 'Shp_Lng',
    'shap_ar': 'Shap_Ar',
    'x': 'X',
    'unnm_0': 'Unnm__0',
    'schl_yr': 'schl_yr',
    'schol_d': 'schol_d',
    'rmtnss_field': 'rmtnss_',
    'ttl_rc_field': 'ttl_rc_',
    'cct_prc': 'cct_prc',
    'orgnl_w_field': 'orgnl_w_',
    'nowater': 'nowater',
    'orgnl_n_field': 'orgnl_n_',
    'n_ntrnt': 'n_ntrnt',
    'noelec': 'noelec',
    'orgnl_l_field': 'orgnl_l_',
    'inst_field': 'inst___',
    'stdnt_c_field': 'stdnt_c_',
    'ttl_tch': 'ttl_tch',
    'stdnt_t_field': 'stdnt_t_',
    'rmtns_field': 'rmtns__',
    'cct_pr_field': 'cct_pr_',
    'nwtr_sc': 'nwtr_sc',
    'n_ntrn_field': 'n_ntrn_',
    'nlc_scl': 'nlc_scl',
    'stdnt_c_field': 'stdnt_c__',
    'stdnt_t_field': 'stdnt_t__',
    'rmtn_2': 'rmtn__2',
    'cct_p_2': 'cct_p_2',
    'elc_2': 'elc___2',
    'wtr_2': 'wtr___2',
    'int_2': 'int___2',
    'stdnt_t_2': 'stdnt_t__2',
    'stdnt_c_2': 'stdnt_c__2',
    'accssbl': 'accssbl',
    'amenits': 'amenits',
    'condtns': 'condtns',
    'shi_scr': 'shi_scr',
    'longitd': 'longitd',
    'ttl_fml': 'ttl_fml',
    'totl_ml': 'totl_ml',
    'ttl_nrl': 'ttl_nrl',
    'ds_totl': 'ds_totl',
    'cp_totl': 'cp_totl',
    'dcm_ttl': 'dcm_ttl',
    'drcp_tt': 'drcp_tt',
    'dh_totl': 'dh_totl',
    'atsm_tt': 'atsm_tt',
    'wcg_ttl': 'wcg_ttl',
    'eb_totl': 'eb_totl',
    'hi_totl': 'hi_totl',
    'id_totl': 'id_totl',
    'li_totl': 'li_totl',
    'md_totl': 'md_totl',
    'pd_totl': 'pd_totl',
    'shp_ttl': 'shp_ttl',
    'spch_tt': 'spch_tt',
    'vi_totl': 'vi_totl',
    'ii_totl': 'ii_totl',
    'p_total': 'p_total',
    'pwd_ttl': 'pwd_ttl',
    'geom': 'MULTIPOLYGON',
}




from django import forms




class Lala(models.Model):
    SR_ColumnVariables = [
        ('remoteness', 'Remoteness Index'),
        ('total_reci', "Total Number of Learners Receiving CCT's"),
        ('cct_percen', "Percentage of Students Recieving CCT's"),
        ('original_w', "Water Access"),
        ('original_i', "Internet Access"),
        ('original_e', "Electricty Access"),
        ('total_enro', "Total Number of Learners with Gender Distribution"),
        ('pwd_total', "Total Number of Learners With Disability"),
    ]
    priority = models.CharField(max_length=1, choices=SR_ColumnVariables)


class LalaForm(forms.ModelForm):
    class Meta:
        model = cms2017
        fields = ['remoteness', 'total_reci', 'cct_percen','original_w', 'original_i', 'original_e', 'total_enro', 'pwd_total']


    








#### FROM LOCAL POSTGRES DATABASE ####
class LguSpending(models.Model):
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    lgu = models.TextField(db_column='LGU', blank=True, primary_key=True)  # Field name made lowercase.
    delete = models.FloatField(blank=True, null=True)
    general_administration = models.FloatField(db_column='GENERAL.ADMINISTRATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elementary_school = models.FloatField(db_column='ELEMENTARY.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secondary_school = models.FloatField(db_column='SECONDARY.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    university_college_education_school = models.FloatField(db_column='UNIVERSITY.COLLEGE.EDUCATION.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vocational_technical_school = models.FloatField(db_column='VOCATIONAL...TECHNICAL.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adult_education = models.FloatField(db_column='ADULT.EDUCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_subsidiary_services = models.FloatField(db_column='EDUCATION.SUBSIDIARY.SERVICES', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manpower_development_mangement_tool = models.FloatField(db_column='MANPOWER.DEVELOPMENT.MANGEMENT.TOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maintenance_of_sports_center_athletic_fields_playground = models.FloatField(db_column='MAINTENANCE.OF.SPORTS.CENTER..ATHLETIC.FIELDS..PLAYGROUND', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_amortization_domestic_debt_service_principal_field = models.FloatField(db_column='LOAN.AMORTIZATION.DOMESTIC.DEBT.SERVICE.PRINCIPAL.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    interest_payment_domestic_debt_service_interest_field = models.FloatField(db_column='INTEREST.PAYMENT.DOMESTIC.DEBT.SERVICE.INTEREST.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    others = models.FloatField(db_column='OTHERS', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lgu_spending'


class ProvincialSpending(models.Model):
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    province = models.TextField(db_column='Province', blank=True, primary_key=True)  # Field name made lowercase.
    delete = models.FloatField(blank=True, null=True)
    general_administration = models.FloatField(db_column='GENERAL.ADMINISTRATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elementary_school = models.FloatField(db_column='ELEMENTARY.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secondary_school = models.FloatField(db_column='SECONDARY.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    university_college_education_school = models.FloatField(db_column='UNIVERSITY.COLLEGE.EDUCATION.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vocational_technical_school = models.FloatField(db_column='VOCATIONAL...TECHNICAL.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adult_education = models.FloatField(db_column='ADULT.EDUCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_subsidiary_services = models.FloatField(db_column='EDUCATION.SUBSIDIARY.SERVICES', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manpower_development_mangement_tool = models.FloatField(db_column='MANPOWER.DEVELOPMENT.MANGEMENT.TOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maintenance_of_sports_center_athletic_fields_playground = models.FloatField(db_column='MAINTENANCE.OF.SPORTS.CENTER..ATHLETIC.FIELDS..PLAYGROUND', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_amortization_domestic_debt_service_principal_field = models.FloatField(db_column='LOAN.AMORTIZATION.DOMESTIC.DEBT.SERVICE.PRINCIPAL.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    interest_payment_domestic_debt_service_interest_field = models.FloatField(db_column='INTEREST.PAYMENT.DOMESTIC.DEBT.SERVICE.INTEREST.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    others = models.FloatField(db_column='OTHERS', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincial_spending'


class RegionalSpending(models.Model):
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, primary_key=True)  # Field name made lowercase.
    delete = models.FloatField(blank=True, null=True)
    general_administration = models.FloatField(db_column='GENERAL.ADMINISTRATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elementary_school = models.FloatField(db_column='ELEMENTARY.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secondary_school = models.FloatField(db_column='SECONDARY.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    university_college_education_school = models.FloatField(db_column='UNIVERSITY.COLLEGE.EDUCATION.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vocational_technical_school = models.FloatField(db_column='VOCATIONAL...TECHNICAL.SCHOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adult_education = models.FloatField(db_column='ADULT.EDUCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    education_subsidiary_services = models.FloatField(db_column='EDUCATION.SUBSIDIARY.SERVICES', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manpower_development_mangement_tool = models.FloatField(db_column='MANPOWER.DEVELOPMENT.MANGEMENT.TOOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maintenance_of_sports_center_athletic_fields_playground = models.FloatField(db_column='MAINTENANCE.OF.SPORTS.CENTER..ATHLETIC.FIELDS..PLAYGROUND', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_amortization_domestic_debt_service_principal_field = models.FloatField(db_column='LOAN.AMORTIZATION.DOMESTIC.DEBT.SERVICE.PRINCIPAL.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    interest_payment_domestic_debt_service_interest_field = models.FloatField(db_column='INTEREST.PAYMENT.DOMESTIC.DEBT.SERVICE.INTEREST.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    others = models.FloatField(db_column='OTHERS', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regional_spending'




