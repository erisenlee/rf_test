import pymysql
import pandas as pd
from common.readConfig import ReadConfig
from common.baseClass import Structure
from common.log import get_log
pymysql.install_as_MySQLdb()

logger=get_log()

class Db(Structure):
    _fields=['host','port','user','password','db']
    # def __init__(self, host, port, user, password, db):
    #     self.host = host
    #     self.port = port
    #     self.user = user
    #     self.password = password
    #     self.db=db
        
    @classmethod
    def read_config(cls, section, path=None):
        instance = cls.__new__(cls)
        
        parser = ReadConfig(path)
        parser.update_attr(instance, section)
        return instance

    def connect(self):
        try:
            con= pymysql.connect(
                host =self.host,
                port=int(self.port),
                user=self.user,
                password=self.password,
                db=self.db,
                cursorclass=pymysql.cursors.DictCursor)
            logger.info('='*20+'Connect db success.'+'='*20)
            return con
        except Exception as e:
            logger.error(e)

    def query(self, sql):
        con=self.connect()
        try:
            with con.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()
                return result
        finally:
            con.close()

    def get_df(self, sql):
        dict_data = self.query(sql)
        if dict_data:
            return pd.DataFrame(dict_data)



if __name__ == '__main__':
    # from config import HOST, USERNAME, PASSWORD, PORT, DB

    # def main(sql):
        # # con = Db(host=HOST, port=PORT, user=USERNAME, password=PASSWORD, db=DB)
        # result = con.get_df(sql)
        # return result

    sql = """SELECT
	*
    FROM
	t_waybill AS a
    WHERE
	a.finish_time >= '2018-07-30 00:00:00'
    AND a.finish_time <= '2018-07-30 23:59:59'
    AND a.point_name = '蜂鸟BOD（金牛万达站）'
    """
    # df = main(sql)
    # is_positive = df['user_rate'] == '非常满意'
    # print(df[is_positive].shape)
    d = Db.read_config('Db')
    r=d.query(sql)
    print(d.__dict__)
    print(r)