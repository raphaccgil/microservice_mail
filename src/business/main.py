"""
Main routine
"""

import os
import configparser
import re
import time
from datetime import datetime, timedelta
from src.business.main_mail import MailPrepare
from src.util.mongo_conn import MongoConn


class MainRout:

    def __init__(self):
        log_file = (os.path.dirname(__file__))
        log_file = re.sub('/business', '', log_file)
        print(log_file)
        for root, dirs, files in os.walk(log_file, topdown=False):
            for name in files:
                if name == 'config.ini':
                    config = configparser.ConfigParser()
                    config.read(os.path.join(root, name))
                    self.userid = config['USER']['USER_ID']
                    self.username = config['USER']['USER_NAME']


    def start(self):
        """
        Run main routine
        :return:
        """
        test_conn = MongoConn()
        test_conn.mongodb_conn('reahbilitation_db_test',
                               'sensor_coll',
                               'mongodb://ec2-3-14-14-152.us-east-2.compute.amazonaws.com:27017/test')
        time_gen = datetime.now() - timedelta(days=40)
        time_unn = int(time.mktime(time_gen.timetuple())*1000)
        flag = test_conn.check_act_sensor(self.username, self.userid, time_unn)
        if flag[0] == 0:
            MailPrepare().send_mail(subject_info='[SISTEMA REABILITAÇÃO REMOTA]',
                                    message_info='Usuário {} está realizando o jogo {} de reabilitação, favor acompanhar'
                                    .format(self.username, flag[1]))

if __name__ == '__main__':
    MainRout().start()