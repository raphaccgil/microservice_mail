"""
Test mongoDB configuration
"""

from src.util.mongo_conn import MongoConn
import pytest
from datetime import datetime, timedelta
import time
import csv
from pprint import pprint

class TestMongoConn:
    """
    Test mongo class
    """

    def __int__(self):
        self.collect_list = []

    def mongo_conn_test(self):

        flag = MongoConn().mongodb_conn('reahbilitation_db',
                     'sensor_coll',
                     'mongodb://localhost:27017/')
        assert flag == 0

    def mongo_conn_remote_test(self):

        flag = MongoConn().mongodb_conn('reahbilitation_db',
                     'sensor_coll',
                     'mongodb://ec2-3-14-14-152.us-east-2.compute.amazonaws.com:27017/test')
        assert flag == 0


    def insert_data_remote_test(self, list_collect):

        temp_time = datetime.now()
        test_conn =  MongoConn()
        test_conn.mongodb_conn('reahbilitation_db_test',
                     'sensor_coll',
                     'mongodb://ec2-3-14-14-152.us-east-2.compute.amazonaws.com:27017/test')

        values = {}
        z = datetime.now()
        cct = lambda: int(round(time.time() * 1000))
        time.mktime(d.timetuple())
        values['datetime'] = z
        values['datetime_int'] = cct()
        values['pitch'] = 3.11111111111111111
        values['median_pitch'] = 3.11111111111111111
        values['roll'] = 3.11111111111111111
        values['median_roll'] = 3.11111111111111111
        values['yam'] = 3.11111111111111111
        values['game_selection'] = 'Game1'
        values['name_patient'] = 'Carlos'
        values['id_patient'] = 1001

        flag = test_conn.insert_data(values)

        temp_time2 = datetime.now()
        list_collect.append((temp_time-temp_time2).microseconds)
        assert flag == 0
        return list_collect

    def check_act_sensor_test(self):

        test_conn = MongoConn()
        test_conn.mongodb_conn('reahbilitation_db_test',
                     'sensor_coll',
                     'mongodb://ec2-3-14-14-152.us-east-2.compute.amazonaws.com:27017/test')

        time_gen = datetime.now() - timedelta(days=20)
        time_unn = int(time.mktime(time_gen.timetuple())*1000)

        flag = test_conn.check_act_sensor('Carlos', 1001, time_unn)

        assert flag[0] == 0 or flag[0] == 1

if __name__ == "__main__":
    TestMongoConn().check_act_sensor_test()
