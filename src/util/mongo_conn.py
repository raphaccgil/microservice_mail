"""
Routine to manipulate from mongoDB
"""

from pymongo import MongoClient, errors, DESCENDING
from pprint import pprint

class MongoConn:
    """
    Prepare to collect mongoDB info
    """

    def __init__(self):
        """
        Load parameter
        """
        self.cliente = ""
        self.banco = ""
        self.album = ""

    def mongodb_conn(self, base, collection, stringconn):
        """
        :param base: Database to collect
        :param collection: Collection used on mongoDB
        :param stringconn: string of connection
        :return: if ok, return value
        """
        try:
            self.cliente = MongoClient(stringconn)
            self.banco = self.cliente[base]
            self.album = self.banco[collection]
            return 0
        except errors.ConnectionFailure:
            return 1

    def insert_data(self, sample):
        """
        :param sample: json list with data
        :return: status of insertion
        """
        try:
            self.album.insert_one(sample)
            self.cliente.close()
            return 0
        except:
            self.cliente.close()
            return 1

    def check_act_sensor(self, name_user, name_id, time_unix):
        """
        Collect the values only higher than a defined value
        :return: If has, at least, one element
        """
        val = []
        try:
            values = self.album.find({'name_patient': name_user,
                                        'id_patient': int(name_id),
                                        'datetime_int': {'$gte': time_unix}}).limit(1)
            try:
                print('OK')
                print(values[0])
                flag = 0
                val.append(flag)
                val.append(values[0]['game_selection'])
            except:
                print('ERRO1')
                flag = 1
                val.append(flag)
        except:
            flag = 2
            val.append(flag)
            print('Error')

        return val


