import allure
from selene import browser, have, query, be, command


class HomePage:

    @allure.step('Открываем главную страницу')
    def open_home_page(self):
        browser.open('')
        browser.element(css_or_xpath_or_by="/html/body/div[3]/div[2]/div/div[2]/span").click()
        assert browser.get(query.url) == 'https://t1.ru/'

    @allure.step('Проверка хэдера')
    def check_header_content(self):
        browser.open('')
        browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[1]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('О Холдинге Т1'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Решения'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[2]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('ИТ-решения'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Продукты'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[3]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('IT-продукты'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Центры компетенций'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[4]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Центры компетенций'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Проекты'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[5]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('IT-проекты'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Закупки'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[6]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Некоммерческие закупки'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Мероприятия'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[7]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Мероприятия'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Карьера'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[8]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Работа в T1'))
        browser.driver.back()
        browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[9]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Пресс-центр'))

    @allure.step('Проверка строки поиска')
    def search(self):
        browser.open('')
        if browser.element('[class ="b-block-cookie-notice__text"]'):
            browser.element('[class ="b-block-cookie-notice__text"]').click()
        browser.element('[class="b-header__search"]').click()
        browser.element('[name="q"]').click()
        browser.element('[name="q"]').type('2024').press_enter()
        browser.element('[class="b-layout__main-content"]').should(have.text('2024'))
        browser.driver.back()

    @allure.step('Проверка обратной связи')
    def feedback(self):
        browser.open('')
        browser.element(css_or_xpath_or_by="/html/body/div[3]/div[2]/div/div[2]/span").click()
        browser.element('[class="b-header__button"]').should(have.text('Написать нам'))
        browser.element('[class="b-header__button"]').click()
        browser.element('[id="cboxLoadedContent"]').should(have.text('Написать нам'))
        browser.element('[id="cboxClose"]').click()

    @allure.step('Проверка заявки на открытые школы')
    def check_open_school(self):
        browser.open('')
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/a/div/div/video").click()
        browser.element('[class ="b-layout__main-content"]').should(have.text('Открытые школы T1'))
        browser.element('[class ="link btn-blue js-link"]').should(
            have.text('Подать заявку'))
        browser.element('[class = "b-career-form__btn btn-white js-b-form-submit"]').perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element('[id="form"]').should(have.text('Подать заявку'))
        browser.driver.back()

    @allure.step('Проверка футера')
    def check_footer(self):
        browser.open('')
        browser.element("a[href='https://habr.com/ru/company/T1Holding/']").should(
            be.visible)
        browser.element("a[href='https://t.me/T1Holding']").should(
            be.visible)
        browser.element('[id="footer-tel"]').should(have.text('+7 495 727-09-85'))
        browser.element('[id="footer-mail"]').should(have.text('info@t1.ru'))

    @allure.step('Проверка элемента презентации')
    def check_presentation(self):
        browser.open('')
        browser.element(css_or_xpath_or_by="/html/body/div[3]/div[2]/div/div[2]/span").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").should(
            have.text('Презентация о холдинге'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").click()
        browser.element('[class ="b-form__title c-h3"]').should(have.text('Презентация о Холдинге Т1'))
        browser.element('[id="tao-form-PresentDownload"]').should(have.text('Скачать презентацию'))
        browser.driver.back()

    @allure.step('Проверка спектра решений')
    def check_solutions(self):
        browser.open('')
        browser.element(css_or_xpath_or_by="/html/body/div[3]/div[2]/div/div[2]/span").click()
        browser.element('[class = "h3"]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element("a[href*='/solutions/services/oblachnye-servisy/']").should(
            have.text('Облачные сервисы'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[4]").click()
        browser.element('[class ="b-layout__main-content"]').should(have.text('Облачные сервисы'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/vychislitelnye-kompleksy-i-khranilishcha-dannykh/']").should(
            have.text('Вычислительные комплексы и хранилища данных'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[1]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Вычислительные комплексы и хранилища данных'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/zakaznaya-razrabotka-po/']").should(
            have.text('Заказная разработка ПО'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[2]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Заказная разработка ПО'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/avtomatizatsiya-i-robotizatsiya-biznes-protsessov/']").should(
            have.text('Автоматизация и роботизация бизнес-процессов'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[10]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Автоматизация и роботизация бизнес-процессов'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/servisy-i-autsorsing/']").should(
            have.text('Сервисы и ИТ-аутсорсинг'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[5]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Сервисы и ИТ-аутсорсинг'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/tsifrovoy-i-it-konsalting/']").should(
            have.text('Цифровой и ИТ-консалтинг'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[8]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Цифровой и ИТ-консалтинг'))
        browser.driver.back()
        browser.element('[class = "h3"]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element("a[href*='/solutions/services/informatsionnaya-bezopasnost/']").should(
            have.text('Информационная безопасность'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[9]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Информационная безопасность'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/upravlenie-it-infrastrukturoy/']").should(
            have.text('Управление ИТ-инфраструктурой'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[12]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Управление ИТ-инфраструктурой'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/inzhenernaya-infrastruktura-tsod/']").should(
            have.text('Инженерная инфраструктура, ЦОД'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[7]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Инженерная инфраструктура, ЦОД'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/setevye-i-kommunikatsionnye-resheniya/']").should(
            have.text('Сетевые и коммуникационные решения'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[6]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Сетевые и коммуникационные решения'))
        browser.driver.back()
        browser.element("a[href*='/solutions/services/promyshlennyy-inzhiniring-i-iot/']").should(
            have.text('Промышленный инжиниринг и IoT'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[3]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(
            have.text('Промышленный инжиниринг и IoT'))
        browser.driver.back()


home_page = HomePage()
