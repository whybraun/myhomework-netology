from unittest import TestCase
import requests

class TestYandexDiskAPI(TestCase):
    def setUp(self):
        self.base_url = 'https://cloud-api.yandex.net/v1/disk'
        self.token = 'YOUR_TOKEN'
        self.folder_path = '/test_folder'
        self.headers = {'Authorization': f'OAuth {self.token}'}
    
    def tearDown(self):
        response = requests.delete(
            f'{self.base_url}/resources',
            headers=self.headers,
            params={'path': self.folder_path}
        )
        self.assertEqual(response.status_code, 204)

    def test_create_folder_positive(self):
        response = requests.put(
            f'{self.base_url}/resources',
            headers=self.headers,
            params={'path': self.folder_path}
        )
        self.assertEqual(response.status_code, 201)

        response = requests.get(
            f'{self.base_url}/resources',
            headers=self.headers,
            params={'path': self.folder_path}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue('test_folder' in response.json().get('_embedded', {}).get('items', {}))
