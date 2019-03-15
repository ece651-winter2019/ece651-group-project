from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.

class URLTester(TestCase) :
    def testingPatientRecord(self):
        response = self.client.get("patientrecords")
        self.assertEqual(response.status_code, 200)
    def testingPatientRecordID(self):
        pk = input("Hey type a patient key")
        resp = self.client.get("patientrecords/" + pk)
        self.assertEqual(resp.status_code, 200)
    def testingPatientUsername(self):
        username = input("Type a username")
        resp = self.client.get("patientrecords/" + username)
        self.assertEqual(resp.status_code, 200)
        pass
