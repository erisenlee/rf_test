from interface.testclass import TestCase
from common.log import get_log

logger=get_log()


class GetPointList(TestCase):
    def setUp(self):
        super().setUp('Client', 'Db')
        self.url = 'http://10.16.21.41:8080/fns/point/pointList?page=1&rows=10'
    def test_point_total(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp['total'],402)


class RiderRankingList(TestCase):
    def setUp(self):
        super().setUp()
        self.path = 'fns/riderRanking/riderRankingList'
    def test_rider_ranking_list(self):
        """获取骑手排名榜"""
        resp = self.client.post(path=self.path,
                beginDate='2018-07-31 00:00:00',
                endDate='2018-07-31 23:59:59',
                kpiScoreId=0,
                kpiScoreName='综合得分',
                # regionalIds: 
                # provinceIds: 
                # cityIds: 
                # operatorIds: 
                pointIds=17417905
                    
        )
        logger.info(resp['total'])
        self.assertEqual(resp['total'],15)