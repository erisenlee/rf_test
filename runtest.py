import unittest
import sys,time
from common.HTMLTestReportCN import HTMLTestRunner
from common.sendMail import mail
from common.log import get_log

sys.path.append('./test_case')

test_dir = './test_case'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

def run():
    logger = get_log()
    logger.info('='*20+'Run test start!'+'='*20)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_name='./report/report_'+now+'.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(f, title='测试报告')
        runner.run(discover)
    logger.info('='*20+'Run test end!'+'='*20)
    mail('TestResult')


if __name__ == '__main__':
    run()
