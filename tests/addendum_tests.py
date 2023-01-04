import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from datetime import date

class AddendumTests(APITestCase):

    fixtures = ['users', 'tokens', 'species', 'patients', 'owners', 'medications', 'medical_records', 'medical_record_medications', 'doctors', 'diagnoses']

    def setUp(self):
        self.user = User.objects.last()
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_addendum(self):

        url = "/addendums"
        data = {
            "medicalRecordId": 1,
            "addendum": "Spelling error on Subjective section",
        }

        response = self.client.post(url, data, format='json')

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["medical_record"], 1)
        self.assertEqual(json_response["addendum"], "Spelling error on Subjective section")
        
