from django.forms import ModelForm,DateField,ChoiceField,Select,HiddenInput
from django.forms.widgets import SelectDateWidget,RadioSelect
from .models import formsyat
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.auth.models import User


time = [('0','00:00'),('1','01:00'),('2','02:00'),('3','03:00'),('4','04:00'),('5','05:00'),('6','06:00'),('7','07:00'),('8','08:00'),('9','09:00'),('10','10:00'),('11','11:00'),('12','12:00'),('13','13:00'),('14','14:00'),('15','15:00'),('16','16:00'),('17','17:00'),('18','18:00'),('19','19:00'),('20','20:00'),('21','21:00'),('22','22:00'),('23','23:00')]

class formf(ModelForm):
    class Meta:
        model = formsyat
        fields = ['Day','From','To']
        widgets = {
            'Day' : SelectDateWidget(),
            'From' : Select(choices=time),
            'To' : Select(choices=time),
        }

