from django.test import TestCase, Client
from api.views import *
from users.models import *
from doctors.models import *
from patients.models import *
from api.serializers import *
from django.urls import reverse
from rest_framework import status

# # initialize the APIClient app
# client = Client()


# class AllPatientRecordTest(TestCase):
#     def setUp(self):
#         CustomUser.objects.create(
#             is_doctor=True,
#             is_patient=False,
#             first_name="Doctor",
#             last_name="Test",
#             phone_no="test",
#             street="test",
#             city="test",
#             state="test",
#             postal_code="test",
#             country="test",
#         )
#         CustomUser.objects.create(
#             is_doctor=False,
#             is_patient=True,
#             first_name="Doctor",
#             last_name="Test",
#             phone_no="test",
#             street="test",
#             city="test",
#             state="test",
#             postal_code="test",
#             country="test",
#         )

#     def test_all_patient_records(self):
#         # get API response
#         response = client.get(reverse("api/"))
