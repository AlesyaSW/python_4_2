import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def browser_size():
    browser.config.window_height = 1000
    browser.config.window_width = 1000
    browser.open('https://google.com')

@pytest.fixture(scope="function")
def clear_field():
    yield
    browser.element('[name="q"]').clear()


