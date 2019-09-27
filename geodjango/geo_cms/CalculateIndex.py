from geo_cms.models import cms2017
from geo_cms.models import regions2
import pandas as pd
from django_pandas.io import read_frame
import seaborn as sns
import os, time, glob
import matplotlib.pyplot as plt
import time
from django.forms import model_to_dict
from django.db.models import Count, F, Value
from django.db.models import IntegerField, FloatField
from django.db.models.functions import Cast


def calculateyo(Geographic_Breakdown, Remoteness, Percentage_CCT, Water_Access, Internet_Access, Electricity_Access, Student_Teacher_Ratio, Student_Classroom_Ratio, Accessibility_Category_Weight, Amentities_Category_Weight, Conditions_Category_Weight):
    if Geographic_Breakdown == 'School':

        start = time.time()
        ##CASTING##
        print('casting')
        mod = cms2017.objects.annotate(remote_int=Cast('remotene_1', FloatField()))
        mod = mod.annotate(cct_int=Cast('cct_perc_1', FloatField()))
        mod = mod.annotate(wat_int=Cast('nowater_sc', FloatField()))
        mod = mod.annotate(int_int=Cast('no_inter_1', FloatField()))
        mod = mod.annotate(elec_int=Cast('noelec_sca', FloatField()))
        mod = mod.annotate(scr_int=Cast('student_cl', FloatField()))
        mod = mod.annotate(str_int=Cast('student_te', FloatField()))

        ##ANNOTATING##
        print('annotating')
        mod = mod.annotate(remote_int=F('remote_int') * Remoteness)
        mod = mod.annotate(cct_int=F('cct_int') * Percentage_CCT)
        mod = mod.annotate(wat_int=F('wat_int') * Water_Access)
        mod = mod.annotate(int_int=F('int_int') * Internet_Access)
        mod = mod.annotate(elec_int=F('elec_int') * Electricity_Access)
        mod = mod.annotate(scr_int=F('scr_int') * Student_Classroom_Ratio)
        mod = mod.annotate(str_int=F('str_int') * Student_Teacher_Ratio)

        ##FINAL CATEGORY CALCULATION##
        mod = mod.annotate(final_access=(F('remote_int') + F('cct_int')) * Accessibility_Category_Weight)
        mod = mod.annotate(final_amenity=(F('wat_int') + F('int_int') + F('elec_int')) * Amentities_Category_Weight)
        mod = mod.annotate(final_condit=(F('scr_int') + F('str_int')) * Conditions_Category_Weight)

        ##FINAL INDEX CALCULATOR##
        mod = mod.annotate(final_index=(F('final_access') + F('final_amenity') + F('final_condit')))


        for obj in mod[0:10]:
            print("rem", obj.remote_int)
            # print("cct", obj.cct_int)
            print('water', obj.wat_int)
            print("scr", obj.scr_int)
            print("str", obj.str_int)
            print("final_access", obj.final_access)
            print("final_amenity", obj.final_amenity)
            print("final_condit", obj.final_condit)
            print("final_index", obj.final_index)

        end = time.time()
        print("SQL QUERY TIME", (end-start))

        return mod

    if Geographic_Breakdown == 'Region':
        df = pd.DataFrame(list(regions2.objects.all().values('rmtnss_field', 'cct_prc', 'orgnl_w_field', 'orgnl_n_field', 'orgnl_l_field', 'orgnl_l_field', 'stdnt_c_field', 'stdnt_t_field')))
        
        print("THIS RIGHT HERE", df)

        print(df.dtypes)

        df['remotness_calculated'] = df['rmtnss_field'] * Remoteness
        df['cct_calculated'] = df['cct_prc'] * Percentage_CCT
        df['water_calculated'] = df['orgnl_w_field'] * Water_Access
        df['internet_calculated'] = df['orgnl_n_field'] * Internet_Access
        df['electricity_calculated'] = df['orgnl_l_field'] * Electricity_Access
        df['str_calculated'] = df['stdnt_c_field'] * Student_Teacher_Ratio
        df['scr_calculated'] = df['stdnt_t_field'] * Student_Classroom_Ratio

        df['index'] = df['remotness_calculated'] + df['cct_calculated'] + df['water_calculated'] + df['internet_calculated'] + df['electricity_calculated'] + df['str_calculated'] + df['scr_calculated']
        print(df['index'])
        return(df['index'].mean())


# if __name__ == '__main__':
#     print(calculateyo(Geographic_Breakdown, Remoteness, Percentage_CCT, Water_Access, Internet_Access, Electricity_Access, Student_Teacher_Ratio, Student_Classroom_Ratio))



