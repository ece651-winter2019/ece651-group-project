# from django.test import TestCase
# from doctors.forms import DoctorSignUpForm
# from users.models import CustomUser
# from django.test import Client
# import datetime
# from django.utils import timezone
# from doctors.models import Profile
#
#
#
# class Setup_Class(TestCase):
#    def setUp(self):
#        self.user = CustomUser.objects.create(license_no=123, practice_name="health clinic")
#
# class Doctor_SignUp_Form_Test(TestCase):
#
#    # Valid Form Data
#    def test_DoctorSignUpForm_valid(self):
#        form = DoctorSignUpForm(data={'user': "12",'license_no': "123", 'practice_name': "health clinic"})
#        self.assertTrue(form.is_valid())
#
#    # Invalid Form Data
#    def test_DoctorSignUpForm_invalid(self):
#        form = DoctorSignUpForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
#        self.assertFalse(form.is_valid())
#
#
#
#
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
