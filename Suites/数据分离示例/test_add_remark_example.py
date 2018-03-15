import os
from unittest import TestCase

from Suites.C.职位备注.test_add_remark import PositionRemarkTest


class PositionRemarkTestOnData(TestCase):

    # 数据分离,根据外部json数据做批量操作
    @staticmethod
    def test_load_json_batch2():
        import json
        f = open(os.path.dirname(os.path.abspath(__file__)) + "/test_data.json", encoding='utf-8')
        datas = json.load(f)
        for i in range(0, len(datas)):
            remark = datas[i]['remark']
            position = datas[i]['position']
            PositionRemarkTest.addPositionRemark(position=position, remark=remark)
            assert PositionRemarkTest.queryPositionRemarks(position, remark=remark)
            # not equal
            print("OK")

