from unittest import TestCase
from app import app

class ConvertTestCase(TestCase):

    def test_converter(self):
        with app.test_client() as client:
            response = client.post('/convert', data=dict(from='USD', to='EUR', amount='100'))
            self.assertEqual(response.status_code, 200)
            result = response.get_data(as_text=True)
            self.assertEqual(result, 'EUR 83.90')
