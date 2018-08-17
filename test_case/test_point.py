from interface.testclass import TestCase


class GetPointList(TestCase):
    def setUp(self):
        super().setUp('Client', 'Db')
        self.url = 'http://10.16.21.41:8080/fns/point/pointList?page=1&rows=10'
    def test_point_total(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp['total'],402)
