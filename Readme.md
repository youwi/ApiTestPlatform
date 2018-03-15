
# Readme
demo edition,注:开源的只是纯代码,删除了很多敏感内容,等有空再补充.

    python3.4+  先安装python3
    pytest      配置测试主工具为pytest(Pycharm--Tools/Python integrated /Default test tool)
    venv        使用虚拟环境,pip安装不影响全局. (命令: python3 -m venv venv)
    init        安装依赖包(pip install -r package.cfg)
    

# how do it
   为什么用纯代码来做接口测试呢? 
   接口测试中有几个避不开的问题:
   - 参数传递(接口依赖)
   - Cookie/Header信息需要预处理
   - 分页接口结果是变动的/循环变量
   - 条件分支
   - 外部数据来源(如短信需要直接从数据库中获取)
   - 随机数据/格式化数据
   最后还是得使用代码来写
   
   庞大的工作量--维护工程量太大


# TODO

   - html的测试报告
   - http/数据库 通用测试工具
   - 基础测试用例
   - 示例测试用例
   - assert tools (json 包/并/异/或)
   - 邮件报告
   - 自动调度(周期执行)
   - web服务查看测试报告
   - 调试日志优化(http-log,栈信息)
   - 文档生成工具(pydoc/sphinx都不合要求)
   - 用例生成工具
   - 性能测试兼容性
   - 背景浏量测试方案
   - xml/yaml标准化
   
  
# files

    ├── Readme.md    
    ├── Reports      # test reports
    ├── Suites       # test suites
    ├── package.log  # requirements log
    ├── runner.py    # test engine runner
    ├── server.py    # flask main app
    └── templates    # flask  htmls
    base on pytest test framework.

# test suite/case example
        
    class ExampleTest(TestCase):

        def setup_class(self):
            LoginGo.login_c("", "")
            return
    
        @staticmethod
        def test_short():
            data = {
                "startedAt": "2017-12-25T00:00:00+08:00",
                "endedAt": "2018-01-08T00:00:00+08:00",
                "uid": 149984216387509
            }
    
            json = POST("/todo/list", data)
            assert jsonContain(json, {"code": 0})

    
# run tests

    pytest
    pytest --html="Reports/report-`date +%Y-%m-%d`.html"
    pytest --junitxml="Reports/report-`date +%Y-%m-%d`.xml"
    pytest --html="Reports/report-`date +%Y-%m-%d`.html" --junitxml="Reports/report-`date +%Y-%m-%d`.xml"


# init dev env
    
    python3 -m venv venv
    source venv/bin/active

# install requirements
  
    pip install -r package.cfg
    
    --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org
    
# dump requirements

    pip freeze > package.cfg


