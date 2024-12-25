from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Worker

class WorkerAPITestCase(APITestCase):

    def setUp(self):
        self.worker1 = Worker.objects.create(name='vimal raj', email='vimalraj@gmail.com', role='devops')
        self.worker2 = Worker.objects.create(name='prasanna', email='prasanna@gmail.com', role='Developer')
        self.worker_list_url = reverse('worker-list')  
        self.worker_url1 = reverse('worker-detail', kwargs={'pk': self.worker1.pk})  
        self.worker_url2 = reverse('worker-detail', kwargs={'pk': self.worker2.pk})  

    def test_create_worker(self):
        data = {'name': 'venkatesh', 'email': 'venkatesh@gmail.com', 'role': 'Manager'}
        response = self.client.post(self.worker_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['name'], 'venkatesh')
        self.assertEqual(response.data['data']['role'], 'Manager')

    def test_get_worker(self):
        response = self.client.get(self.worker_url1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'vimal raj')
        self.assertEqual(response.data['data']['email'], 'vimalraj@gmail.com')

    def test_update_worker(self):
        updated_data = {'name': 'vimal raj', 'email': 'vimalraj@gmail.com', 'role': 'Developer'}
        response = self.client.put(self.worker_url1, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'vimal raj')
        self.assertEqual(response.data['data']['role'], 'Developer')

    def test_delete_worker(self):
        response = self.client.delete(self.worker_url1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_invalid_worker(self):
        data = {'name': '', 'email': '', 'role': ''}
        response = self.client.post(self.worker_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_non_existent_worker(self):
        response = self.client.get(reverse('worker-detail', kwargs={'pk': 88}))  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_non_existent_worker(self):
        updated_data = {'name': 'kamal', 'email': 'kamal@gmailcom', 'role': 'Manager'}
        response = self.client.put(reverse('worker-detail', kwargs={'pk': 99}), updated_data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_worker(self):
        updated_data = {'role': 'Lead Developer'}
        response = self.client.patch(self.worker_url2, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['role'], 'Lead Developer')

    def test_search_worker(self):
        response = self.client.get(self.worker_list_url, {'search': 'prasanna'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)  

    def test_filter_worker_by_role(self):
        response = self.client.get(self.worker_list_url, {'role': 'Developer'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['data']), 0)  
