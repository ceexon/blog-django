from ..users.tests import BaseTest
from rest_framework.views import status


class BlogPostTests(BaseTest):

    def login(self):
        login_user = self.client.post(
            '/users/login/',
            {
                "email": "trevor@zone.code",
                "password": "zonecode123",
            },
            format='json'
        )

        token = login_user.data['token']
        return token

    def login_1(self):
        login_user = self.client.post(
            '/users/login/',
            {
                "email": "trevors@zone.code",
                "password": "zonecode123",
            },
            format='json'
        )

        token = login_user.data['token']
        return token

    def test_get_all_posts(self):
        response = self.client.get('/posts/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_post(self):
        token = self.login()

        response = self.client.post(
            "/posts/new/", self.new_post, HTTP_AUTHORIZATION='Bearer '+token,
            format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_single_1_retrieve_blog(self):
        token = self.login()

        post = self.client.post(
            "/posts/new/", self.new_post, HTTP_AUTHORIZATION='Bearer '+token,
            format='json')

        response = self.client.get(
            "/posts/2/",
        )
        response1 = self.client.get('/users/posts/1/')

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_2_update_blog(self):
        token = self.login()
        token_1 = self.login_1()

        post = self.client.post(
            "/posts/new/", self.new_post, HTTP_AUTHORIZATION='Bearer '+token,
            format='json')

        response = self.client.put(
            '/posts/3/',
            {
                'title': "New blog title",
                "content": "changing the blog content",
                "caption": "new or old caption",
            },
            HTTP_AUTHORIZATION='Bearer '+token,
            format='json'
        )

        response1 = self.client.put(
            '/posts/3/',
            {
                'title': "New blog title",
                "content": "changing the blog content",
                "caption": "new or old caption",
            },
            HTTP_AUTHORIZATION='Bearer '+token_1,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.status_code, status.HTTP_403_FORBIDDEN)

    def test_single_3_delete_blog(self):
        token = self.login()
        token_1 = self.login_1()

        post = self.client.post(
            "/posts/new/", self.new_post, HTTP_AUTHORIZATION='Bearer '+token,
            format='json')

        post1 = self.client.post(
            "/posts/new/", self.new_post, HTTP_AUTHORIZATION='Bearer '+token,
            format='json')

        response = self.client.delete(
            '/posts/4/',
            HTTP_AUTHORIZATION='Bearer '+token_1,
            format='json'
        )

        response1 = self.client.delete(
            '/posts/4/',
            HTTP_AUTHORIZATION='Bearer '+token,
            format='json'
        )

        response2 = self.client.delete(
            '/posts/4/',
            HTTP_AUTHORIZATION='Bearer '+token,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
