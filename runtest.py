import unittest
import sys,time
from common.HTMLTestReportCN import HTMLTestRunner

sys.path.append('./test_c')

test_dir = './test_c'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*')

def run():
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_name='./report/'+now+'.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(f, title='测试报告')
        runner.run(discover)

if __name__ == '__main__':
    from common.logger import Log
    log = Log()
    log.info('start test...')
    run()
    log.info('end test')