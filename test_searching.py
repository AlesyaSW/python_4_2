from selene.support.shared import browser
from selene import be, have


def test_searching(browser_size, clear_field):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('In ancient Greek mythology and religion'))


def test_neg(browser_size, clear_field):
    browser.element('[name="q"]').type('qwertrewqweqwqwewqwefghjkloiuytrewsdfghjk').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено.'))
