from django.contrib import admin
from django.contrib.gis import admin
from .models import regions
from .models import cms2017
from .models import regions2
from .models import districts
from .models import regions_simple

# Register your models here.
admin.site.register(regions, admin.OSMGeoAdmin)
admin.site.register(cms2017, admin.OSMGeoAdmin)
admin.site.register(regions2, admin.OSMGeoAdmin)
admin.site.register(districts, admin.OSMGeoAdmin)
admin.site.register(regions_simple, admin.OSMGeoAdmin)