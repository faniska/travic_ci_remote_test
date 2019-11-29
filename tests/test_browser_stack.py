import os

import pytest
from selenium import webdriver


@pytest.fixture()
def remote_driver():
    desired_cap = {
        'browser': 'Edge',
        'browser_version': '18.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768',
        'name': 'Bstack-[Python] Sample Test'
    }

    username = os.environ["BROWSERSTACK_USERNAME"]
    access_key = os.environ["BROWSERSTACK_ACCESS_KEY"]

    return webdriver.Remote(
        command_executor=f'http://{username}:{access_key}@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap
    )


def test_google_via_bs(remote_driver):
    remote_driver.get("http://www.google.com/")
    if "Google" not in remote_driver.title:
        raise Exception("Unable to load google page!")
    elem = remote_driver.find_element_by_name("q")
    elem.send_keys("Remote Test Tools")
    elem.submit()
    print(remote_driver.title)
    remote_driver.quit()
