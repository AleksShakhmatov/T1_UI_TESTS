import time

import allure
from selene import browser, have, query, be, command


class HomePage:

    @allure.step('Открываем главную страницу')
    def open_home_page(self):
        browser.open('')
        assert browser.get(query.url) == 'https://t1.ru/'

    @allure.step('Проверка хэдера')
    def check_header_content(self):
        browser.open('')
        browser.element(".b-menu-header__link[href='/about/']").should(have.text('Холдинг'))
        browser.element(".b-menu-header__link[href='/about/']").click()
        browser.element(".b-layout__main-content").should(have.text('О Холдинге Т1'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/solutions/']").should(have.text('Решения'))
        browser.element(".b-menu-header__link[href='/solutions/']").click()
        browser.element(".b-layout__main-content").should(have.text('ИТ-решения'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/products/']").should(have.text('Продукты'))
        browser.element(".b-menu-header__link[href='/products/']").click()
        browser.element(".b-layout__main-content").should(have.text('IT-продукты'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/competencies/']").should(have.text('Центры компетенций'))
        browser.element(".b-menu-header__link[href='/competencies/']").click()
        browser.element(".b-layout__main-content").should(have.text('Центры компетенций'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/projects/']").should(have.text('Проекты'))
        browser.element(".b-menu-header__link[href='/projects/']").click()
        browser.element(".b-layout__main-content").should(have.text('IT-проекты'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/purchases/']").should(have.text('Закупки'))
        browser.element(".b-menu-header__link[href='/purchases/']").click()
        browser.element(".b-layout__main-content").should(have.text('Некоммерческие закупки'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/events/']").should(have.text('Мероприятия'))
        browser.element(".b-menu-header__link[href='/events/']").click()
        browser.element(".b-layout__main-content").should(have.text('Мероприятия'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/career/']").should(have.text('Карьера'))
        browser.element(".b-menu-header__link[href='/career/']").click()
        browser.element(".b-layout__main-content").should(have.text('Работа в T1'))
        browser.driver.back()
        browser.element(".b-menu-header__link[href='/news/']").should(have.text('Пресс-центр'))
        browser.element(".b-menu-header__link[href='/news/']").click()
        browser.element(".b-layout__main-content").should(have.text('Пресс-центр'))

    @allure.step('Проверка строки поиска')
    def search(self):
        browser.open('')
        browser.element(".b-header__search").click()
        browser.element('[name="q"]').click()
        browser.element('[name="q"]').type('2024').press_enter()
        browser.element(".b-layout__main-content").should(have.text('2024'))

    @allure.step('Проверка обратной связи')
    def feedback(self):
        browser.open('')
        browser.element(".b-header__button").should(have.text('Написать нам'))
        browser.element(".b-header__button").click()
        browser.element("#cboxLoadedContent").should(have.text('Написать нам'))
        browser.element("#cboxClose").click()

    @allure.step('Проверка заявки на открытые школы')
    def check_open_school(self):
        browser.open('')
        browser.element(".b-block-video").click()
        browser.element(".b-layout__main-content").should(have.text('Открытые школы T1'))
        browser.element(".b-block-banner__content").should(
            have.text('Подать заявку'))
        browser.element(".b-career-form__btn").perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element("#form").should(have.text('Подать заявку'))

    @allure.step('Проверка элемента презентации')
    def check_presentation(self):
        browser.open('')
        browser.element(".c-large-button").perform(command.js.scroll_into_view).should(be.visible)
        browser.element(".c-large-button").should(have.text('Презентация о холдинге'))
        browser.element(".c-large-button").click()
        browser.element(".b-form__title").should(have.text('Презентация о Холдинге Т1'))
        browser.element("#tao-form-PresentDownload").should(have.text('Скачать презентацию'))

    @allure.step('Проверка спектра решений')
    def check_solutions(self):
        browser.open('')
        browser.element(".b-block-services__items").perform(command.js.scroll_into_view).should(be.visible)
        browser.element("[data-id='1']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Вычислительные комплексы и хранилища данных'))
        browser.driver.back()
        browser.element("[data-id='2']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Заказная разработка ПО'))
        browser.driver.back()
        browser.element("[data-id='4']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(have.text('Облачные сервисы'))
        browser.driver.back()
        browser.element("[data-id='12']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Большие данные, клиентский опыт и AI/ML'))
        browser.driver.back()
        browser.element("[data-id='11']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Автоматизация и роботизация бизнес-процессов'))
        browser.driver.back()
        browser.element("[data-id='5']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Сервисы и ИТ-аутсорсинг'))
        browser.driver.back()
        browser.element("[data-id='9']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Цифровой и ИТ-консалтинг'))
        browser.driver.back()
        browser.element("[data-id='10']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Информационная безопасность'))
        browser.driver.back()
        browser.element("[data-id='13']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Управление ИТ-инфраструктурой'))
        browser.driver.back()
        browser.element("[data-id='8']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Инженерная инфраструктура, ЦОД'))
        browser.driver.back()
        browser.element("[data-id='6']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Сетевые и коммуникационные решения'))
        browser.driver.back()
        browser.element("[data-id='3']").perform(command.js.click)
        browser.element(".b-layout__main-content").should(
            have.text('Промышленный инжиниринг и IoT'))

    @allure.step('Проверка соцсетей')
    def check_social_network(self):
        browser.open('')
        browser.element(".b-socials").perform(command.js.scroll_into_view).should(be.visible)
        browser.element("a[href='https://habr.com/ru/company/T1Holding/']").should(
            be.visible)
        browser.element("a[href='https://t.me/T1Holding']").should(
            be.visible)
        browser.element("#footer-tel").should(have.text('+7 495 727-09-85'))
        browser.element("#footer-mail").should(have.text('info@t1.ru'))

    @allure.step('Проверка футера')
    def check_footer(self):
        browser.open('')
        browser.element(".b-footer__bottom").perform(command.js.scroll_into_view).should(be.visible)
        browser.element("a[href*='https://www.e-disclosure.ru/portal/company.aspx?id=38924']").should(
            have.text('Раскрытие информации на сайте агентства «Интерфакс»'))
        browser.element("a[href*='/compliance/']").should(have.text('Комплаенс'))
        browser.element("a[href*='/documents/personal_data_politics/']").should(
            have.text('Политика по обработке персональных данных'))
        browser.element("a[href*='/documents/license_agreement/']").should(have.text(
            'Пользовательское соглашение при использовании сайта'))
        browser.element("a[href*='/it-accreditation/']").should(have.text('ИТ-аккредитация'))
        browser.element(".b-footer__bottom").should(have.text('Холдинг Т1 © 2011–2025'))
        browser.element(".b-footer__copyright-lebedev-logo").should(have.attribute('href', "https://www.artlebedev.ru/"))
        browser.element(".b-footer__bottom-right").should(have.text('Задизайнено в Студии Артемия Лебедева'))
        browser.element("a[href*='https://www.artlebedev.ru/t1/site2/']").should(have.text('Информация о сайте'))
        browser.element(".b-footer__copyright-techart").should(have.text('Web-дизайн, разработка сайта — Текарт'))


home_page = HomePage()
