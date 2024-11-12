from django import forms
from .models import *

class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["drink", "is_suger", "is_milk", "treat"]
        labels = {"drink" : "飲み物", "is_suger" : "砂糖を入れる？", "is_milk" : "ミルクを入れる？", "treat" : "スイーツ"}
    
    def __init__(self, *args, **kwargs):
        # user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['required'] = ''
        
        # self.fields["is_suger"].widget.attrs.pop('required')
        # self.fields["is_milk"].widget.attrs.pop('required')

        self.fields["is_suger"].widget = forms.CheckboxInput(attrs = {'class' : 'check'})
        self.fields["is_milk"].widget = forms.CheckboxInput(attrs = {'class' : 'check'})

        self.fields["drink"].queryset = Drink.objects.filter(is_out_of_order=False)
        self.fields["treat"].queryset = Treat.objects.filter(is_out_of_order=False)

class AddDrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ["name", "yen"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ''

class AddTreatForm(forms.ModelForm):
    class Meta:
        model = Treat
        fields = ["name", "yen"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ''