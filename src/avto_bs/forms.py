from django import forms
from .models import z_avtomodel, z_avtobrand

class CarModelForm(forms.ModelForm):
    class Meta:
        model = z_avtomodel
        fields = ['Name', 'BrandID']

    def __init__(self, *args, **kwargs):
        super(CarModelForm, self).__init__(*args, **kwargs)
        self.fields['BrandID'].queryset = z_avtobrand.objects.all()