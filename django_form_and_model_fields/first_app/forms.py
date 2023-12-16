from django import forms
from django.core import validators
from first_app.models import UserModel
import datetime

class UserForm(forms.Form):
    name = forms.CharField(label="full name :",max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}), help_text="Name is must")
    age = forms.IntegerField(help_text="Age is must", required = True, widget= forms.NumberInput(attrs= {'placeholder': 'Enter your age'}))
    birth_date = forms.DateField(widget= forms.NumberInput(attrs= {'type': 'date'}))
    email = forms.EmailField(help_text="Email must contain .com ", required = True, widget= forms.EmailInput(attrs= {'placeholder':'Enter your email address'}))
    check = forms.BooleanField(help_text="Confirm your gmail address", label="Confirm")
    Today = forms.DateField(initial= datetime.date.today, disabled= True, required=False)
    JOIN_YEAR = ['2000', '2009', '2010']
    Chose_joining_year = forms.DateField(widget = forms.SelectDateWidget(years= JOIN_YEAR))
    reporting_time = forms.DateTimeField(widget = forms.DateTimeInput(attrs= {'type': 'datetime-local'}))
    CHOICES = [('M','Morning'),('D','Day'),('E','Evening')]
    Shift = forms.ChoiceField(choices= CHOICES ,widget = forms.RadioSelect)
    COLORS = [('R','RED'),('G','GREEN'),('B','BLUE'),('Y','YELLOW'),('O','ORANGE'),('BL','BLACK'),('V','VIOLET'),('W','WHITE')]
    Favorite_colors = forms.MultipleChoiceField(choices= COLORS, widget = forms.CheckboxSelectMultiple)
    height = forms.FloatField(label="Your Height",help_text="Input in meters", required= True)
    about_you = forms.CharField(widget= forms.Textarea(attrs={'placeholder': 'Tell us something shortly about you'}), help_text='Not necessary but recommended', required=False)
    upload_your_picture = forms.ImageField(help_text='Uplooad a photo of you', validators=[validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'], message='only jpg, png and jpeg formats are allowed')], required= True)
    upload_your_CV = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='only can upload pdf files')],required=True)
    # password = forms.PasswordInput()

    def clean_email(self):
        valemail = self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("Please submit a valid mail")
        return valemail
    

class UserStudent(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        labels = {
            'roll': 'Roll Number',
            'name': 'Student Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'confirm': 'Confirmation',
            'registration_no': 'Registration Number',
            'date_of_birth': 'Date of Birth',
            'appointment': 'Appointment Date',
            'graduation_date': 'Graduation Date',
            'photo': 'Profile Photo',
        }
        widgets = {
            'roll': forms.NumberInput(),
            'name': forms.TextInput(),
            'email' : forms.EmailInput(),
            'phone' : forms.NumberInput(),
            'confirm': forms.CheckboxInput(),
            'registration_no' : forms.NumberInput(),
            'waight' : forms.NumberInput(),
            'height': forms.NumberInput(),
            'Current_time' : forms.TimeInput(attrs={'value':datetime.datetime.now().strftime('%H:%M')}),
            'date_of_birth' : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'appointment' : forms.DateInput(attrs={'type': 'date'}),
            'your_opinion' : forms.Textarea(),
            'address' : forms.TextInput(),
            'graduation_date': forms.DateInput(attrs={'type':'date'}),
            'degree' : forms.TextInput(),
            'photo': forms.ClearableFileInput(attrs={'multiple': False}),
        }
        help_texts = {
            'name': 'write full Name in 50 characters',
            'roll': 'Your roll number',
            'email' : 'Your email address',
            'phone' : 'Your phone number',
            'waight' : 'Your waight',
            'height': 'Your height',
            'Current_time' : 'Now',
            'date_of_birth' : 'Put a valid date and year when you were born',
            'appointment' : 'Enter the date you were appointed',
            'your_opinion' : 'Optional',
            'graduation_date' : 'Enter the date you were graduated',
            'degree' : 'Enter the degree you achieved',
            'photo' : 'Upload a photo of you',
        }

        error_messages = {
            'name': {'required': "Name is must "},
            'email' : {'required':'Your email address is must' , 'invalid': 'check the validity again'}
        }
