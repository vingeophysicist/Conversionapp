from django import forms




class LengthConverterForm(forms.Form):
# A tuple is defined to store the units. The      
     MEASUREMENTS = (
        ('centimetre', 'Centimetre'),
        ('metre', 'Metre'),
        ('mile', 'Mile'), 
        ('kilometre','Kilometre'),
        ('inch', 'Inch')
        )
     input_unit = forms.ChoiceField(choices=MEASUREMENTS)
     input_value = forms.DecimalField(decimal_places=3)
     output_unit = forms.ChoiceField(choices=MEASUREMENTS)
     output_value = forms.DecimalField(decimal_places=4, required=False)

class AreaShapeForm(forms.Form):
   area = forms.DecimalField(decimal_places=2)
   breadth = forms.DecimalField(decimal_places=2)
   height = forms.DecimalField(decimal_places=2)