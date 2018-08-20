from interface.testclass import TestCase
# from common.logger import Log

class GetOperatorList(TestCase):
    def setUp(self):
        super().setUp()
        self.url = 'fns/operator/operatorList'
        self.sql = 'SELECT * FROM t_operator as a'
        
    def test_operator_success(self):
        """运营商获取成功"""
        resp = self.client.get(path=self.url,page=1,rows=10)
        rows=self.db.query(self.sql)

        self.assertEqual(len(resp['rows']),len(rows))

    def test_operator_error(self):
        """运营商获取错误"""
        self.assertRaises(TypeError)

class StaffList(TestCase):
    def setUp(self):
        super().setUp('Client', 'Db')
        self.url = 'http://10.16.21.41:8080/fns/staff/staffList?page=1&rows=10'
    def test_staff(self):
        """骑手数量"""
        resp=self.client.get(url=self.url)
        self.assertEqual(resp['total'],6871)

if __name__ == '__main__':
    import unittest
    suit = unittest.TestSuite()
    suit.addTest(StaffList('test_staff'))
    
