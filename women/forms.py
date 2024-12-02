from datetime import datetime, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.forms import FileInput, Textarea, DateInput

from .models import Review, Reservation


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message', 'image', 'rating']
        widgets = {
            'message': Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Your Message'
            }),
            'image': FileInput(attrs={'class': 'form-control-file'}),
            'rating': forms.Select(attrs={'class': 'form-control'})
        }




class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'table_number']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select a date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select a time',
                'type': 'time',
            }),
            'table_number': forms.Select(choices=[(i, f'Table {i}') for i in range(1, 21)], attrs={
                'class': 'form-control',
            })
        }

    def clean_time(self):
        time = self.cleaned_data['time']
        if not (time.hour >= 8 and time.hour < 23):
            raise forms.ValidationError("Time should be between 8:00 and 23:00.")
        return time

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.now().date() or date > datetime.now().date()+ timedelta(days=30*6):
            raise forms.ValidationError("Date should be within six months from now.")
        return date
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        table_number = cleaned_data.get('table_number')

        if date and time and table_number:
            start_time = datetime.combine(date, time)
            end_time = start_time + timedelta(hours=1)

            overlapping_reservations = Reservation.objects.filter(
                table_number=table_number,
                date=date,
                time__lt=end_time.time()
            )

            for reservation in overlapping_reservations:
                existing_start_time = datetime.combine(reservation.date, reservation.time)
                existing_end_time = existing_start_time + timedelta(hours=1)

                if start_time < existing_end_time:
                    raise ValidationError(
                        f'Table {table_number} is already booked from '
                        f'{existing_start_time.time()} to {existing_end_time.time()}.'
                    )

        return cleaned_data


