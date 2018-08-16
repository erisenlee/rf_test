from interface.client import Client
from database.db import Db
from common.utils import TestCase
from common.logger import Log

class GetOperatorList(TestCase):
    def setUp(self):
        super().setUp('Client','Db')
        self.url = 'http://10.16.21.41:8080/fns/operator/operatorList?page=1&rows=10'
        # self.client = Client()
        # self.client.read_config('Client')
        # self.db = Db.read_config('Db')
        self.sql = 'SELECT * FROM t_operator as a'
        
    def test_operator_success(self):
        """运营商获取成功"""
        resp = self.client.get(url=self.url)
        self.logger.info('geet success!')
        rows=self.db.query(self.sql)

        self.assertEqual(len(resp['rows']),len(rows))

    def test_operator_fail(self):
        """运营商获取失败"""
        resp = False
        self.assertEqual(resp,True)
    def test_operator_error(self):
        """运营商获取错误"""
        self.assertRaises(TypeError)

# class SelectOperatorByCityIds(unittest.TestCase):
#     def setUp
class StaffList(TestCase):
    def setUp(self):
        super().setUp('Client', 'Db')
        self.url = 'http://10.16.21.41:8080/fns/staff/staffList?page=1&rows=10'
    def test_staff(self):
        """骑手数量"""
        resp=self.client.get(url=self.url)
        self.assertEqual(resp['total'],6871)

if __name__ == '__main__':
    from unittest import defaultTestLoader
    s = defaultTestLoader.loadTestsFromTestCase(GetOperatorList)