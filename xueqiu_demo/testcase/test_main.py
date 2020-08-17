import pytest
import yaml

from xueqiu_demo.page.app import APP


class TestMain():
    def test_main(self):
        app = APP()
        app.start().main().goto_search()
        # app.start().main().goto_search_yaml()
        # app.start_caps().main().goto_search_yaml()

    path = 'C:/Users/Administrator/PycharmProjects/haige_appium/xueqiu_demo/testcase/test_yaml.yaml'
    @pytest.mark.parametrize('value1,value2',yaml.safe_load(open(path)))
    def test_yaml(self,value1,value2):
        print('value1=',value1)
        print('value2=',value2)









