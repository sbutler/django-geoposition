from django import forms
from django.utils.translation import ugettext_lazy as _

from .widgets import GeopositionWidget
from . import Geoposition


class GeopositionField(forms.MultiValueField):
    default_error_messages = {
        'invalid': _('Enter a valid geoposition.')
    }

    def __init__(self, *args, **kwargs):
        fields = (
            forms.DecimalField(label=_('Latitude')),
            forms.DecimalField(label=_('Longitude')),
        )
        if not 'widget' in kwargs:
            kwargs['widget'] = GeopositionWidget([f.widget for f in fields])
        if 'initial' in kwargs:
            kwargs['initial'] = Geoposition(*kwargs['initial'].split(','))
        super(GeopositionField, self).__init__(fields, **kwargs)

    def widget_attrs(self, widget):
        classes = widget.attrs.get('class', '').split()
        classes.append('geoposition')
        return {'class': ' '.join(classes)}

    def compress(self, value_list):
        if value_list:
            return value_list
        return ""
