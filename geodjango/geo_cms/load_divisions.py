import os
from django.contrib.gis.utils import LayerMapping
from .models import divisions

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


divisions_shp = os.path.abspath(os.path.join('geodjango', 'data', 'merged', 'divisions_shp.shp'))


def run_divisions(verbose=True):
    lm_d = LayerMapping(divisions, divisions_shp, divisions_mapping,
                      transform=False, encoding='iso-8859-1')

    lm_d.save(strict=True, verbose=verbose)