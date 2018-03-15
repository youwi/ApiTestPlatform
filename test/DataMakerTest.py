import random
from unittest import TestCase

from Common.utils.DataMaker import DataMaker


class DataMakerTest(TestCase):

    @staticmethod
    def test_daa():
        print(DataMaker.string(20))
        print(DataMaker.iso_date_random())
        print(DataMaker.iso_date())
        print(DataMaker.telephone())

    @staticmethod
    def test_tid():
        list_data = range(0, 100)
        list_out = []
        for i in list_data:
            list_out.append(DataMaker.tid())

        print(list_out)

    @staticmethod
    def test_tid2():
        list_data = range(0, 100)
        list_out = []
        for i in list_data:
            list_out.append(DataMaker.tid() + str(random.randint(0, 100)))

        print(list_out)
