from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


class HotelAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(HotelAdminForm, self).__init__(*args, **kwargs)
        self.fields['rating'].help_text = mark_safe('<span style="color:red">Рейтинг составляется по 5-балльной шкале!</span>')
        self.fields['staff_rating'].help_text = mark_safe('<span style="color:red">Рейтинг составляется по 5-балльной шкале!</span>')

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating > 5:
            raise ValidationError('Рейтинг не может быть больше пяти!')
        return rating

    def clean_staff_rating(self):
        staff_rating = self.cleaned_data['staff_rating']
        if staff_rating > 5:
            raise ValidationError('Рейтинг не может быть больше пяти!')
        return staff_rating

    short_description = forms.CharField(widget=forms.Textarea)

class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Review)
admin.site.register(HotelRoom)
admin.site.register(RoomTypes)
admin.site.register(OurServices)
admin.site.register(Tours)