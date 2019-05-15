from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
import json


class BaseTest(APITestCase):
    def setUp(self):
        new_user = {
            "email": "trevor@zone.code",
            "password": "zonecode123",
            "profile": {
                "first_name": "Zee",
                "other_names": "Zonecc",
                "year_of_birth": "1998-07-03 08:00",
                "bio": "Django Training developer upcoming",
                "gender": 1
            }
        }

        new_user_response = self.client.post(
            "/users/new/", new_user, format="json")


class UserTests(BaseTest):
    def test_add_new_user(self):
        """
        Tests adding of a new member to the group
        """

        response = self.client.post(
            '/users/new/',
            {
                "email": "trevzee@zonecc.com",
                "password": "zonec124",
                "profile": {
                    "first_name": "Zee",
                    "other_names": "Zonecc",
                    "year_of_birth": "1998-07-03 08:00",
                    "bio": "Django Training developer upcoming",
                    "gender": 1
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        response = self.client.post(
            '/users/login/',
            {
                "email": "trevor@zone.code",
                "password": "zonecode123",
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_login_credentions(self):
        wrong_email = {
            'email': 'email@gmail.com',
            'password': 'zonecode123',
        }

        wrong_password = {
            "email": "trevor@zone.code",
            "password": "zonee123",
        }

        response_1 = self.client.post(
            '/users/login/',
            wrong_email,
            format='json'
        )

        response_2 = self.client.post(
            '/users/login/',
            wrong_password,
            format='json'
        )

        self.assertEqual(response_1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_view_all_users_not_authenticated(self):
        login = self.client.post(
            '/users/login/',
            {
                "email": "trevor@zone.code",
                "password": "zonecode123",
            },
            format='json'
        )

        token = login.data['token']

        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_view_all_users(self):
        login = self.client.post(
            '/users/login/',
            {
                "email": "trevor@zone.code",
                "password": "zonecode123",
            },
            format='json'
        )

        token = login.data['token']

        response = self.client.get(
            "/users/", HTTP_AUTHORIZATION='Bearer '+token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
