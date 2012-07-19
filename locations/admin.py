from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from locations.models import Location


class LocationAdminForm(forms.ModelForm):
    latitude = forms.FloatField(
        min_value=-90,
        max_value=90,
        help_text=_("Values from -90 to 90 degrees"),
        required=False
    )
    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        help_text =_("Values from -180 to 180 degrees"),
        required=False
    )
    
    class Meta:
        model = Location
        exclude = ('coordinates',)


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm


admin.site.register(Location, LocationAdmin)