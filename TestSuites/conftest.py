"""
按目前需要输出接口相关的数据.
"""


def pytest_runtest_setup(item):
    # 每个用例运行之前要运行的代码
    return


def pytest_runtest_teardown(item):
    # 每个测试用例运行之后的测试代码
    from Common.SwaggerURL import SwaggerURL
    print(SwaggerURL.LAST_URL)


def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    这个方法在所有测试完成以后再运行.
    总结时出的文档,最后运行的代码
    1,输入接口覆盖状态到文件.
    """
    from Common.SwaggerURL import SwaggerURL
    # print(SwaggerURL.URL_COUNT)
    SwaggerURL.save_swagger_to_file()
