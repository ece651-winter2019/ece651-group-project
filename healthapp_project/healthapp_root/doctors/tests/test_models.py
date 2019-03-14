from django.test import TestCase
from doctors.models import Profile
from users.models import CustomUser
# Create your tests here.


class ProfileModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Profile.objects.create(license_no=123, practice_name="health clinic")
        CustomUser.objects.create(is_doctor= True)

    def test_practice_name_label(self):
        # Get a profile object to test
        profile = Profile.objects.get(user_id=1)
        # Get the metadata for the required field and use it to query the required field data
        field_label = profile._meta.get_field("practice_name").verbose_name
        # Compare the value to the expected result
        self.assertEquals(field_label, "practice name")

    def test_license_no_label(self):
        profile = Profile.objects.get(user_id=1)
        field_label = profile._meta.get_field("license_no").verbose_name
        self.assertEquals(field_label, "license no")

    def test_practice_name_max_length(self):
        profile = Profile.objects.get(user_id=1)
        max_length = profile._meta.get_field("practice_name").max_length
        self.assertEquals(max_length, 20)


