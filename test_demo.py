import pytest
import allure
import requests


@pytest.mark.demo
@allure.feature("request demo feature")
def test_demo():
    with allure.step("访问百度"):
        r = requests.get("https://www.baidu.com")

