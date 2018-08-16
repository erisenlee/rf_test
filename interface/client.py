import requests
from urllib.parse import urljoin
from common.readConfig import ReadConfig

class Client:
    def __init__(self, base_url=None, login_endpoint=None, username=None, password=None):
        self.host = base_url
        self.login_endpoint=login_endpoint
        self.login_url = None
        self.username = username
        self.password = password
        self.login_status = False
        self.session = requests.Session()

    @classmethod
    def read_config(cls, section, path=None):
        parser = ReadConfig(path)
        instance=cls.__new__(cls)
        parser.update_attr(instance, section)
        setattr(instance, 'login_status', False)
        if hasattr(instance, 'host') and hasattr(instance, 'login_endpoint'):
            setattr(instance,'login_url',urljoin(getattr(instance,'host'),getattr(instance,'login_endpoint')))
        return instance

    def login(self):
        # print(self.login_url)
        self.session.post(self.login_url, data=dict(
            username=self.username, password=self.password))
        self.login_status = True

    def get(self, path=None, url=None, **param):
        resp = None
        self.get_login()
        if url:
            resp = self.session.get(url)
        elif path:
            url, params = self._make_request(path, **param)
            resp = self.session.get(url, params=params)
        else:
            raise ValueError('path or url is needed')
        if resp.status_code == 200:
            return resp.json()

    def post(self, path=None, url=None, **data):
        resp = None
        self.get_login()
        if url:
            data=dict(**data)
            resp = self.session.post(url,data=data)
        elif path:
            url, data = self._make_request(path, **data)
            resp = self.session.post(url, data=data)
        else:
            raise ValueError('path or url is needed')
        if resp.status_code == 200:
            return resp.json()
        
    def _make_request(self, path, **data):

        if path:
            url = urljoin(self.host, path)
            data = dict(**data)
            return url, data
        else:
            raise ValueError('path is empty')
    def get_login(self):
        if self.login_status == False:
            self.login()


if __name__ == '__main__':
    # url = 'http://fns.livejx.cn'

    s = Client.read_config('Client')
    # r = s.get(path='/fns/staff/staffList', pag=1, rows=10)
    # l='http://fns.livejx.cn/fns/pointDaily/pointDailyList?beginDate=2018-07-03+00:00:00&endDate=2018-07-03+23:59:59&operatorIds=01a68837571b4eee9719113835fedefa&pointIds=&pointTypes='
    # l='http://10.16.21.41:8080/fns/operator/operatorList?page=1&rows=10'
    # r = s.get(url=l)
    # r=s.post(url=
    print(s.__dict__)
