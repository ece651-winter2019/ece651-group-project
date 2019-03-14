from django.test import TestCase
from doctors.forms import DoctorSignUpForm
from users.models import CustomUser
import datetime
from django.utils import timezone


class DoctorSignUpFormTest(TestCase):
    def setUpTestData(cls):


    def save_Test(self):


#class DoctorSignUpFormTest(TestCase):
#    def setUpTestData(cls):
#        # Set up non-modified objects used by all test methods
#        Profile.objects.create(license_no=123, practice_name="health clinic")
#        CustomUser.objects.create(is_doctor= True)
#
#    def test_renew_form_date_field_label(self):
#        form = RenewBookForm()
#        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')
#
#    def test_renew_form_date_field_help_text(self):
#        form = RenewBookForm()
#        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')
#
#    def test_renew_form_date_in_past(self):
#        date = datetime.date.today() - datetime.timedelta(days=1)
#        form = RenewBookForm(data={'renewal_date': date})
#        self.assertFalse(form.is_valid())
#
#    def test_renew_form_date_too_far_in_future(self):
#        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
#        form = RenewBookForm(data={'renewal_date': date})
#        self.assertFalse(form.is_valid())
#
#    def test_renew_form_date_today(self):
#        date = datetime.date.today()
#        form = RenewBookForm(data={'renewal_date': date})
#        self.assertTrue(form.is_valid())
#
#    def test_renew_form_date_max(self):
#        date = timezone.now() + datetime.timedelta(weeks=4)
#        form = RenewBookForm(data={'renewal_date': date})
#        self.assertTrue(form.is_valid())
