from django.test import TestCase
from patients.forms import PatientSignUpForm
from users.models import CustomUser
from django.test import Client
import datetime
from django.utils import timezone
from patients.models import Profile as PatProfile
from doctors.models import Profile as DocProfile


class Patient_SignUp_Form_Test(TestCase):
    #    @classmethod
    #    def setUpTestData(cls):
    #        # Set up non-modified objects used by all test methods
    ##        Profile.objects.create(user_id=1, license_no=123, practice_name="health clinic")
    #        CustomUser.objects.create(is_doctor=True)

    # Valid Form Data
    def test_PatientSignUpForm_valid(self):
        form = PatientSignUpForm(
            data={
                "doctor": DocProfile.objects.first().pk,
                "dob": "12/12/2000",
                "sex": "Male",
                "contact_firstname": "ammar",
                "contact_lastname": "ahmed",
                "contact_relationship": "Friend",
                "contact_phone": 32423442,
                "first_name": "ammar",
                "last_name": "ahmed",
                "phone_no": 23234323,
                "street": "uni ave",
                "city": "waterloo",
                "state": "ON",
                "postal_code": "N2L3G5",
                "country": "Waterloo",
                "username": "patient",
                "password1": "ECE651project",
                "password2": "ECE651project",
            }
        )
        print(form.errors)
        self.assertTrue(form.is_valid())

    # Invalid Form Data (signing up without having a doctor id)
    def test_PatientSignUpForm_invalid(self):
        form = PatientSignUpForm(
            data={
                "doctor": "",
                "dob": "12/12/2000",
                "sex": "Male",
                "contact_firstname": "ammar",
                "contact_lastname": "ahmed",
                "contact_relationship": "Friend",
                "contact_phone": 32423442,
                "first_name": "ammar",
                "last_name": "ahmed",
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
        print(form.errors)
        self.assertFalse(form.is_valid())


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
