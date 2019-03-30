from django.test import TestCase
from doctors.forms import *
from users.models import *
from django.test import Client
import datetime
from django.utils import timezone
from doctors.models import *


class Custom_User_Creation_Form_Test(TestCase):
    #    @classmethod
    #    def setUpTestData(cls):
    #        # Set up non-modified objects used by all test methods
    ##        Profile.objects.create(user_id=1, license_no=123, practice_name="health clinic")
    #        CustomUser.objects.create(is_doctor=True)

    # Valid Form Data
    def test_CustomUserCreationForm_valid(self):
        form = CustomUserCreationForm(
            data={
                "first_name": "ammar",
                "last_name": "ahmed",
                "phone_no": 23234323,
                "street": "uni ave",
                "city": "waterloo",
                "state": "ON",
                "postal_code": "N2L3G5",
                "country": "Waterloo",
                "username": "customuser",
                "password1": "ECE651Proj",
                "password2": "ECE651Proj",
            }
        )
        #                                form.save()
        print(form.errors)
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_DoctorSignUpForm_invalid(self):
        form = DoctorSignUpForm(
            data={
                "phone_no": 23234323,
                "street": "uni ave",
                "city": "waterloo",
                "state": "ON",
                "postal_code": "N2L3G5",
                "country": "Waterloo",
                "license_no": 1234,
                "practice_name": "health clinic",
                "username": "doctor",
                "password1": "Ece651proj",
                "password2": "Ece651proj",
            }
        )
        self.assertFalse(form.is_valid())


#

##    # Set up non-modified objects used by all test methods
##    def setUpTestData(cls):
##        Profile.objects.create(user_id = 1,license_no=123, practice_name="health clinic")
##        CustomUser.objects.create(is_doctor= True)
##
##
##    def save_Test(self):
##        form = DoctorSignUpForm()
##        self.assertTrue(form.fields['practice_name'].label == None or form.fields['practice_name'].label == 'practice name')
#
## class DoctorSignUpFormTest(TestCase):
#
##    def test_renew_form_date_field_label(self):
##        form = RenewBookForm()
##        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')
##
##    def test_renew_form_date_field_help_text(self):
##        form = RenewBookForm()
##        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')
##
##    def test_renew_form_date_in_past(self):
##        date = datetime.date.today() - datetime.timedelta(days=1)
##        form = RenewBookForm(data={'renewal_date': date})
##        self.assertFalse(form.is_valid())
##
##    def test_renew_form_date_too_far_in_future(self):
##        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
##        form = RenewBookForm(data={'renewal_date': date})
##        self.assertFalse(form.is_valid())
##
##    def test_renew_form_date_today(self):
##        date = datetime.date.today()
##        form = RenewBookForm(data={'renewal_date': date})
##        self.assertTrue(form.is_valid())
##
##    def test_renew_form_date_max(self):
##        date = timezone.now() + datetime.timedelta(weeks=4)
##        form = RenewBookForm(data={'renewal_date': date})
##        self.assertTrue(form.is_valid())
#
