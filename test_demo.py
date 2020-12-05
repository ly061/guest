import pytest
import allure
import requests


@pytest.mark.demo
@allure.feature("request demo feature")
@pytest.mark.parametrize('status_code', [200, 300, 400])
def test_demo1(status_code):
    with allure.step("访问百度"):
        r = requests.get("https://www.baidu.com")
        assert r.status_code == status_code

