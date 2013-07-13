import logging
from django import forms
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

class GeopositionWidget(forms.MultiWidget):
    def decompress(self, value):
        if value:
            return [value.latitude, value.longitude]
        return [None,None]
    
    def format_output(self, rendered_widgets):
        return render_to_string('geoposition/widgets/geoposition.html', {
            'latitude': {
                'html': rendered_widgets[0],
                'label': _("Latitude"),
            },
            'longitude': {
                'html': rendered_widgets[1],
                'label': _("Longitude"),
            },
        })
    
    class Media:
        js = (
                'geoposition/geoposition.js',
                'https://maps.googleapis.com/maps/api/js?sensor=false',
        )
        css = {
            'all': ('geoposition/geoposition.css',)
        }
