from django.test import TestCase
from doctors.models import Profile

# Create your tests here.


class ProfileModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Profile.objects.create(license_no=123, practice_name="health clinic")

    def test_practice_name_label(self):
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field("practice_name").verbose_name
        self.assertEquals(field_label, "practice name")

    def test_license_no_label(self):
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field("license_no").verbose_name
        self.assertEquals(field_label, "license number")

    def test_practice_name_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field("practice_name").max_length
        self.assertEquals(max_length, 20)


#    def test_get_absolute_url(self):
#        profile = Profile.objects.get(id=1)
#        # This will also fail if the urlconf is not defined.
#        self.assertEquals(profile.get_absolute_url(), 'profile/')
