from unittest import TestCase

from Common.Assertion import Assertion


class AssTest(TestCase):

    def test_assert(self):
        big = {"code": 1, "msg": "OK",
               "body": {"id": 2727, "name": "宁志龙-2018.01.22.06.00.48.048-自动测试测试职位-签约客户公司-自动化测试预埋数据",
                        "projectId": "nu4j9djvq08a",
                        "resumeId": 18455, "resume": {
                       "basic": {"id": 18455, "name": "宁志龙", "gender": 2, "mobile": "15507784016",
                                 "email": "ppnvxv1t@0355.net",
                                 "birthday": "2014-11-09T06:00:48+08:00", "currentLocationCode": 310000,
                                 "startedWorkAt": "2014-11-09T06:00:48+08:00", "orgName": "火今夫力5匹文仓qNF4气反劝人书sGW",
                                 "position": "软件测试工程师火今夫力5匹文仓qNF4气反劝人书sGW", "annualSalary": 100000.0,
                                 "annualSalaryType": 1,
                                 "degree": 2, "skills": [], "certificates": [], "langs": [], "expectLocations": [],
                                 "expectSalary": 200000.0, "expectSalaryType": 1, "expectIndustries": [],
                                 "leftReason": "A不止X订V车扎无匹五木区Iv丰孔贝H刀丹反以z少匹1中专六kX计q允艺n九t牙太五以凤卜爪文文为M内予S心仅贝vprN以dd介一办尤八厂计艺凤认天牛w以凶yG予乏夫LAm88J手天仅五什无力手九四n 职业前景/潜在升职机会",
                                 "dimissionPeriod": "10",
                                 "evaluate": "A不止X订V车扎无匹五木区Iv丰孔贝H刀丹反以z少匹1中专六kX计q允艺n九t牙太五以凤卜爪文文为M内予S心仅贝vprN以dd介一办尤八厂计艺凤认天牛w以凶yG予乏夫LAm88J手天仅五什无力手九四n 第一个测试",
                                 "schoolCode": 322003600, "schoolName": "江苏理工学院", "schoolTypes": [], "seniority": 3,
                                 "age": 3,
                                 "works": []}, "resumeExperiences": [
                           {"id": 709, "resumeId": 342, "startedAt": "2014-11-09T06:00:48+08:00", "onJob": 1,
                            "orgName": "火今夫力5匹文仓qNF4气反劝人书sGW", "industries": [],
                            "position": "软件测试工程师火今夫力5匹文仓qNF4气反劝人书sGW",
                            "description": ""}], "resumeProjects": [
                           {"id": 714, "resumeId": 342, "startedAt": "2014-11-09T06:00:48+08:00", "onPro": 1,
                            "name": "火今夫力5匹文仓qNF4气反劝人书sGW 基线/客户项目团队 软件测试工程师",
                            "orgName": "火今夫力5匹文仓qNF4气反劝人书sGW Google TV - Android K/L/M/N  GTVfamily-2.5years",
                            "description": "火今夫力5匹文仓qNF4气反劝人书sGW Google Chromecast/Chromecast Ultra  LinuxSDK-1.5years在客户与公司之间建立有效的沟通桥梁,并提供及时的协助并处理来自客户项目的请求."}],
                       "resumeEducations": [{"id": 306, "resumeId": 342, "startedAt": "2014-11-09T06:00:48+08:00",
                                             "endedAt": "2014-11-09T06:00:48+08:00", "schoolCode": 322003600,
                                             "schoolName": "江苏理工学院", "schoolTypes": [], "degree": 2, "major": 12107}]},
                        "language": 1}}
        assert Assertion.jsonContain({"A": "A", "B": "B"}, {"A": "A"})
        assert not Assertion.jsonContain(big, {"name": "宁志龙2"})
        assert Assertion.jsonContain(big, {"name": "宁志龙"})
        assert Assertion.jsonContain(big, {"id": 709})
