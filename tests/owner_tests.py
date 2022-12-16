import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from retrieverapi.models import Owners

class OwnerTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'species', 'patients', 'owners', 'medications', 'medical_records', 'medical_record_medications', 'doctors', 'diagnoses']

    def setUp(self):
        self.user = User.objects.last()
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_single_owner(self):
        """
        Ensure we can get single patient.
        """

        # Seed the database with a owner
        owner = Owners()
        owner.name= "Laura Davis"
        owner.phone_number= "520-194-4829"
        owner.email= "lauradavis@gmail.com"
        owner.address= "390 Maple St, Nashville, TN 37206"  
        
        owner.save()


        # Initiate request and store response
        response = self.client.get(f"/owners/{owner.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["name"], "Laura Davis")
        self.assertEqual(json_response["phone_number"], "520-194-4829")
        self.assertEqual(json_response["email"], "lauradavis@gmail.com")
        self.assertEqual(json_response["address"], "390 Maple St, Nashville, TN 37206")
        
    def test_create_owner(self):
        """
        Ensure we can create a new game.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/owners"

        # Define the request body
        data = {
            "name": "Laura Davis",
            "phoneNumber": "520-194-4829",
            "email": "lauradavis@gmail.com",
            "address": "390 Maple St, Nashville, TN 37206",
            
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["name"], "Laura Davis")
        self.assertEqual(json_response["phone_number"], "520-194-4829")
        self.assertEqual(json_response["email"], "lauradavis@gmail.com")
        self.assertEqual(json_response["address"], "390 Maple St, Nashville, TN 37206")
    
    def test_updated_owner(self):
        """
        Ensure we can change an existing patient.
        """
        owner = Owners()
        owner.name= "Laura Davis"
        owner.phone_number= "520-194-4829"
        owner.email= "lauradavis@gmail.com"
        owner.address= "390 Maple St, Nashville, TN 37206"  
        
        owner.save()
        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "name": "Laura Davis",
            "phoneNumber": "520-194-4829",
            "email": "lauradavis@gmail.com",
            "address": "390 Maple St, Nashville, TN 37206",
            
        }

        response = self.client.put(f"/owners/{owner.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET game again to verify changes were made
        response = self.client.get(f"/owners/{owner.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["name"], "Laura Davis")
        self.assertEqual(json_response["phone_number"], "520-194-4829")
        self.assertEqual(json_response["email"], "lauradavis@gmail.com")
        self.assertEqual(json_response["address"], "390 Maple St, Nashville, TN 37206")
  
