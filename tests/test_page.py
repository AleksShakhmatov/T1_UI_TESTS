from allure_commons.types import Severity
from pages.home_page import home_page
import allure


class TestHomePage:

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story("Тест открытия главной страницы")
    def test_open_home_page(self):
        home_page.open_home_page()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story("Тест проверки хэдэра")
    def test_check_header_content(self):
        home_page.check_header_content()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story('Тест поискового поля"')
    def test_search(self):
        home_page.search()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story('Тест обратной связи')
    def test_feedback(self):
        home_page.feedback()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story('Тест спектра решений')
    def test_check_solutions(self):
        home_page.check_solutions()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story('Тест подачи заявки на открытые школы')
    def test_check_open_school(self):
        home_page.check_open_school()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story('Тест футера')
    def test_check_footer(self):
        home_page.check_footer()

    @allure.tag("web")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "AleksSH")
    @allure.feature("Работа элементов сайта")
    @allure.story('Тест элемента презентации')
    def test_check_presentation(self):
        home_page.check_presentation()
