from django.test import TestCase, Client, RequestFactory
from api.views import DateTimeFilter, all_patient_records
from patients.models import Record as PatientRecord
from patients.models import Profile as PatProfile, Record
from doctors.models import Profile as DocProfile
from users.models import CustomUser
from api.serializers import RecordsSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient
from rest_framework.authtoken.models import Token
import json

# include an appropriate Authorization: header on all requests.
# token = Token.objects.get(user__username='test')
client = APIClient()


class AllPatientRecordTest(APITestCase):
    def setUp(self):
        # create user credentials
        self.username = "test"
        self.password = "test"

        self.user = CustomUser.objects.create_user(self.username, None, self.password)
        # create user account for patient
        self.user.is_doctor = False
        self.user.is_patient = True
        self.user.first_name = "test"
        self.user.last_name = "patient"
        self.user.phone_no = "555"
        self.user.street = "test"
        self.user.city = "test"
        self.user.state = "test"
        self.user.postal_code = "test"
        self.user.country = "test"

        # create dictionary of patient data to be posted
        self.record = [
            {
                "bp_diastolic": 70,
                "bp_systolic": 165,
                "heart_rate": 60,
                "weight": 180,
                "height": "180",
            },
            {
                "bp_diastolic": 123,
                "bp_systolic": 100,
                "heart_rate": 66,
                "weight": 180,
                "height": "180",
            },
            {
                "bp_diastolic": 70,
                "bp_systolic": 1200,
                "heart_rate": 60,
                "weight": 180,
                "height": "180",
            },
            {
                "bp_diastolic": 800,
                "bp_systolic": 1200,
                "heart_rate": 60,
                "weight": 180,
                "height": "180",
            },
        ]

        # Bypass authentication needed
        self.client.force_authenticate(user=self.user)

        # Post test data
        posted_data = self.client.post(
            "/api/patientrecords", self.record, format="json"
        )
        # Confirm it was created
        self.assertEqual(posted_data.status_code, status.HTTP_201_CREATED)
        # Remove authentication bypass
        self.client.force_authenticate(user=None)

        # create token for test user
        self.token = Token.objects.create(user=self.user)
        # self.api_authentication()

    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_token_received(self):
        # store reponse from api call
        response = client.post(
            "/api/token-auth", {"username": "test", "password": "test"}, format="json"
        )

        # check if response went well
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # check if correct token was given
        self.assertEqual(response.data, {"token": self.token.key})

    def test_record_multiple_patient_data(self):
        # Need to force authenticate to get past IsPatientUser check using the client requests
        self.client.force_authenticate(user=self.user)
        data = [
            {
                "bp_systolic": "180",
                "bp_diastolic": "180",
                "heart_rate": "60",
                "weight": "180",
                "height": "180",
            },
            {
                "bp_systolic": "180",
                "bp_diastolic": "180",
                "heart_rate": "60",
                "weight": "180",
                "height": "180",
            },
        ]
        response = self.client.post("/api/patientrecords", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Record.objects.count(), 6)

    def test_record_single_patient_data(self):
        # Need to force authenticate to get past IsPatientUser check using the client requests
        self.client.force_authenticate(user=self.user)
        data = {
            "bp_systolic": "180",
            "bp_diastolic": "180",
            "heart_rate": "60",
            "weight": "180",
            "height": "180",
        }
        response = self.client.post("/api/patientrecords", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Record.objects.count(), 5)

    def test_record_patient_data_invalid_request(self):
        # Need to force authenticate to get past IsPatientUser check using the client requests
        self.client.force_authenticate(user=self.user)
        data = {
            "bp_systoli": "180",
            "bp_diastolic": "180",
            "heart_rate": "60",
            "weight": "180",
            "height": "180",
        }
        response = self.client.post("/api/patientrecords", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_record_patient_data_not_a_user(self):
        data = {
            "bp_systolic": "180",
            "bp_diastolic": "180",
            "heart_rate": "60",
            "weight": "180",
            "height": "180",
        }
        response = self.client.post("/api/patientrecords", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_record_patient_data_no_appropriate_permissions(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        data = {
            "bp_systolic": "180",
            "bp_diastolic": "180",
            "heart_rate": "60",
            "weight": "180",
            "height": "180",
        }
        response = self.client.post("/api/patientrecords", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_patient_data_patient_user(self):
        self.client.force_authenticate(user=self.user)
        # data = self.record
        # self.client.post('/api/patientrecords',data,format='json')
        response = self.client.get("/api/patientrecords")
        print(response.data)
        print(self.record)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data,self.record)

    # def test_all_patient_records(self):
    #     self.user=1
    #     self.id=11
    #     # get API response
    #     response = client.get(reverse("api/patientrecords"))
    #     # get data from database
    #     user = self.request.user
    #     records = PatientRecord.objects.filter(user_id=user)
    #     if type(records.data) == list:
    #         for d in records:
    #             d["user"] = userid
    #         serializer = RecordsSerializer(data=records, many=True)
    #     else:
    #         records["user"] = userid
    #         serializer = RecordsSerializer(data=records)
    #     self.assertEqual(response.data,serializer.data)
