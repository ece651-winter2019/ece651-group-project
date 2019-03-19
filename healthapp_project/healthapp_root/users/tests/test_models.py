from django.test import TestCase

# from doctors.models import Profile
from django.test import Client
from users.models import CustomUser
from django.conf import settings

# Create your tests here.
# settings.configure()


class CustomUserClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        CustomUser.objects.create(
            first_name="Ammar",
            last_name="Ahmed",
            phone_no="2344234",
            street="200 unversity ave",
            city="waterloo",
            state="ON",
            postal_code="N2l4g5",
            country="Canada",
        )

    #        CustomUser.objects.create(is_doctor=True)

    def test_is_doctor_label(self):
        # Get a profile object to test
        custom_user = CustomUser.objects.get(id=1)
        # Get the metadata for the required field and use it to query the required field data
        field_label = custom_user._meta.get_field("is_doctor").verbose_name
        # Compare the value to the expected result
        self.assertEquals(field_label, "is doctor")

    #    def test_is_doctor_valid(self):
    #        custom_user = CustomUser(data={'is_doctor': "True"})
    #        self.assertTrue(custom_user.is_valid())

    #    def test_is_doctor_valid(self):
    #        custom_user = CustomUser.objects.get(id=1)
    #        field_label = custom_user._meta.get_field("is_doctor")
    #        self.assertEquals(field_label, False)

    def test_is_patient_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("is_patient").verbose_name
        self.assertEquals(field_label, "is patient")

    def test_first_name_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("first_name").verbose_name
        self.assertEquals(field_label, "first name")

    def test_first_name_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("first_name").max_length
        self.assertEquals(max_length, 20)

    def test_last_name_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("last_name").verbose_name
        self.assertEquals(field_label, "last name")

    def test_last_name_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("last_name").max_length
        self.assertEquals(max_length, 20)

    def test_phone_no_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("phone_no").verbose_name
        self.assertEquals(field_label, "phone no")

    def test_phone_no_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("phone_no").max_length
        self.assertEquals(max_length, 10)

    def test_street_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("street").verbose_name
        self.assertEquals(field_label, "street")

    def test_street_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("street").max_length
        self.assertEquals(max_length, 20)

    def test_city_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("city").verbose_name
        self.assertEquals(field_label, "city")

    def test_city_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("city").max_length
        self.assertEquals(max_length, 20)

    def test_state_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("state").verbose_name
        self.assertEquals(field_label, "state")

    def test_state_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("state").max_length
        self.assertEquals(max_length, 2)

    def test_postal_code_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("postal_code").verbose_name
        self.assertEquals(field_label, "postal code")

    def test_postal_code_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("postal_code").max_length
        self.assertEquals(max_length, 6)

    def test_country_label(self):
        custom_user = CustomUser.objects.get(id=1)
        field_label = custom_user._meta.get_field("country").verbose_name
        self.assertEquals(field_label, "country")

    def test_country_max_length(self):
        custom_user = CustomUser.objects.get(id=1)
        max_length = custom_user._meta.get_field("country").max_length
        self.assertEquals(max_length, 20)


#    def test_str(self):
#        obj = CustomUser()
