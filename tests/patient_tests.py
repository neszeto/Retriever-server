import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from retrieverapi.models import Patients

class PatientTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'species', 'patients', 'owners', 'medications', 'medical_records', 'medical_record_medications', 'doctors', 'diagnoses']

    def setUp(self):
        self.user = User.objects.last()
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_single_patient(self):
        """
        Ensure we can get single patient.
        """

        # Seed the database with a patient
        patient = Patients()
        patient.name= "Scotty"
        patient.species_id= 2
        patient.sex= "Male"
        patient.breed= "Scottish Terrier"
        patient.age= 2
        patient.color= "Black"
        patient.weight= 18
        patient.deceased= False
        patient.owner_id= 8
        patient.image_url= "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png"

        patient.save()


        # Initiate request and store response
        response = self.client.get(f"/patients/{patient.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["name"], "Scotty")
        self.assertEqual(json_response["sex"], "Male")
        self.assertEqual(json_response["breed"], "Scottish Terrier")
        self.assertEqual(json_response["age"], 2)
        self.assertEqual(json_response["color"], "Black")
        self.assertEqual(json_response["weight"], 18)
        self.assertEqual(json_response["deceased"], False)
        self.assertEqual(json_response["image_url"], "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png")


    def test_updated_patient(self):
        """
        Ensure we can change an existing patient.
        """
        patient = Patients()
        patient.name= "Scotty"
        patient.species_id= 2
        patient.sex= "Male"
        patient.breed= "Scottish Terrier"
        patient.age= 2
        patient.color= "Black"
        patient.weight= 18
        patient.deceased= False
        patient.owner_id= 8
        patient.image_url= "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png"

        patient.save()
        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "name": "Scotty",
            "speciesId": 2,
            "sex": "Male",
            "breed": "Scottish Terrier",
            "age": 5,
            "color": "Black and White",
            "weight": 23,
            "deceased": True,
            "image_url": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png"
        }

        response = self.client.put(f"/patients/{patient.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET game again to verify changes were made
        response = self.client.get(f"/patients/{patient.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["name"], "Scotty")
        self.assertEqual(json_response["sex"], "Male")
        self.assertEqual(json_response["breed"], "Scottish Terrier")
        self.assertEqual(json_response["age"], 5)
        self.assertEqual(json_response["color"], "Black and White")
        self.assertEqual(json_response["weight"], 23)
        self.assertEqual(json_response["deceased"], True)
        self.assertEqual(json_response["image_url"], "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png")