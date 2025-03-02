import allure
from allure_commons.types import Severity
from selene import have, browser


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "AleksSH")
@allure.feature("Работа элементов сайта")
@allure.story("Ключевые проверки")
def test_check_header_content():
    with allure.step("Окрыть сайт"):
        browser.open('')
    with allure.step("Наличие страницы холдинга"):
        browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
    with allure.step("Наличие страницы решений"):
        browser.element('[class="b-header__menu"]').should(have.text('Решения'))
    with allure.step("Наличие страницы продуктов"):
        browser.element('[class="b-header__menu"]').should(have.text('Продукты'))
    with allure.step("Наличие страницы центра компетенций"):
        browser.element('[class="b-header__menu"]').should(have.text('Центры компетенций'))
    with allure.step("Наличие страницы закупок"):
        browser.element('[class="b-header__menu"]').should(have.text('Закупки'))
    with allure.step("Наличие страницы мероприятий"):
        browser.element('[class="b-header__menu"]').should(have.text('Мероприятия'))
    with allure.step("Наличие страницы карьеры (ваканский)"):
        browser.element('[class="b-header__menu"]').should(have.text('Карьера'))
    with allure.step("Наличие страницы пресс-центра"):
        browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))


def test_search():
    with allure.step("Окрыть сайт"):
        browser.open('')
    with allure.step("Открыть строку поиска"):
        browser.element('[class="b-header__search"]').click()
    with allure.step("Активировать курсов в поле поиска"):
        browser.element('[name="q"]').click()
    with allure.step("Ввести данные"):
        browser.element('[name="q"]').type('2024').press_enter()
    with allure.step("Проверить введенные данные"):
        browser.element('[class="b-layout__main-content"]').should(have.text('2024'))


def test_feedback():
    with allure.step("Окрыть сайт"):
        browser.open('')
    with allure.step("Проверить наименование кнопки"):
        browser.element('[class="b-header__button"]').should(have.text('Написать нам'))
    with allure.step("Кликнуть по кнопке"):
        browser.element('[class="b-header__button"]').click()
    with allure.step("Проверка заголовка открывшейся формы"):
        browser.element('[id="cboxLoadedContent"]').should(have.text('Написать нам'))
    with allure.step("Закрыть форму"):
        browser.element('[id="cboxClose"]').click()


def test_holding():
    with allure.step("Окрыть сайт"):
        browser.open('')
    with allure.step("Наличие страницы холдинга"):
        browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
    with allure.step("Переход на страницу"):
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[1]/a").click()
    with allure.step("Проверка заголовка"):
        browser.element('[class="b-layout__main-content"]').should(have.text('О Холдинге Т1'))


def test_center():
    with allure.step("Окрыть сайт"):
        browser.open('')
    with allure.step("Наличие страницы пресс-центра"):
        browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))
    with allure.step("Переход на страницу"):
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[9]/a").click()
    with allure.step("Проверка заголовка"):
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]").should(have.text('Пресс-центр'))
