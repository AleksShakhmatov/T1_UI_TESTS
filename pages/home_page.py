import allure
from selene import browser, have, be, query, command


class MainPage:

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        browser.open('')
        assert browser.get(query.url) == 'https://t1.ru/'

    @allure.step('Проверка хэдера')
    def test_check_header_content(self):
        browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[1]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('О Холдинге Т1'))
        browser.element('[class="b-header__menu"]').should(have.text('Решения'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[2]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Решения'))
        browser.element('[class="b-header__menu"]').should(have.text('Продукты'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[3]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Продукты'))
        browser.element('[class="b-header__menu"]').should(have.text('Центры компетенций'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[4]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Центры компетенций'))
        browser.element('[class="b-header__menu"]').should(have.text('Закупки'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[5]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Закупки'))
        browser.element('[class="b-header__menu"]').should(have.text('Мероприятия'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[6]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Мероприятия'))
        browser.element('[class="b-header__menu"]').should(have.text('Карьера'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[7]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Карьера'))
        browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[9]/a").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]").should(have.text('Пресс-центр'))

    @allure.step('Проверка...')
    def test_search(self):
        browser.element('[class="b-header__search"]').click()
        browser.element('[name="q"]').click()
        browser.element('[name="q"]').type('2024').press_enter()
        browser.element('[class="b-layout__main-content"]').should(have.text('2024'))

    @allure.step('Проверка...')
    def test_feedback(self):
        browser.element('[class="b-header__button"]').should(have.text('Написать нам'))
        browser.element('[class="b-header__button"]').click()
        browser.element('[id="cboxLoadedContent"]').should(have.text('Написать нам'))
        browser.element('[id="cboxClose"]').click()

    @allure.step('Проверка...')
    def check_present(self):
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").should(
            have.text('Презентация о Холдинге Т1'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").click()
        browser.element('[class ="b-form__title c-h3"]').should(have.text('Презентация о Холдинге Т1'))
        browser.element('[id="tao-form-PresentDownload"]').should(have.text('Скачать презентацию'))
        browser.element('[id="cboxClose"]').click()

    @allure.step('Проверка...')
    def check_present(self):
        browser.element('[class="b-block-services__items"]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[4]").should(
            have.text('Облачные сервисы'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[2]/div/map/area[4]").click()
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/h1").should(have.text('Облачные сервисы'))
        browser.open('')
        assert browser.get(query.url) == 'https://t1.ru/'

    @allure.step('Проверка...')
    def check_present(self):
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/a/div/div/video").click()
        browser.element('[class ="breadcrumbs"]').should(have.text('Открытые школы T1'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/main/div[2]/div/div[2]/a").should(
            have.text('Подать заявку'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/main/div[2]/div/div[2]/a").click()
        browser.element('[class ="b-block-career-form-new__title"]').should(have.text('Подать заявку'))
        browser.open('')
        assert browser.get(query.url) == 'https://t1.ru/'

    @allure.step('Проверка...')
    def check_present(self):
        (browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[7]/a").
         perform(command.js.scroll_into_view).should(be.visible))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[7]/a").should(have.text('Мероприятия'))
        browser.all('[class ="b-block-events-main__items"]').should(
            have.size(3))

    @allure.step('Проверка хэдера')
    def check_futter(self):
        browser.element('[class="b-footer__top-bottom]').perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element(
            '[class ="b-socialsitem .b-socialsitem--tm a[href="https://habr.com/ru/company/T1Holding/"]').should(
            be.visible)
        browser.element('[class ="b-socials__item .b-socials__item--hr a[href="https://t.me/T1Holding"]').should(
            be.visible)
        browser.element('[id="footer-tel"]').should(have.text('+7 495 727-09-85'))
        browser.element('[id="footer-mail"]').should(have.text('info@t1.ru'))
        browser.element('[class ="b-block-career-form-new__title"]').should(have.text('*'))
        browser.element('[class ="b-block-career-form-new__title"]').click()
        browser.element('[colorbox-content--values"]').should(
            have.text('Осуществляя взаимодействие с Т1 по электронной почте'))


main_page = MainPage()

''' 
@allure.step('В виджете главной страницы во вкладке "Поясняем" отображается три статьи')
    def is_three_articles_in_new_tab(self):
        browser.element('[class="main-widget-inner main-widget-popular main-widget-questions"]').perform(
            command.js.scroll_into_view)
        browser.all('.main-widget-inner.main-widget-news .main-widget-post').should(
            have.size(3))

    @allure.step('Клик по вкладке "Задачи" на виджете')
    def click_on_popular_tab(self):
        browser.element('[class="main-widget-tab tab-popular tab-questions"]').click()
        browser.element('[class="main-widget main-widget-popular--active"]').should(be.enabled)

    @allure.step('Клик по вкладке "Полезное" на виджете')
    def click_on_news_tab(self):
        browser.element('[class="main-widget-tab tab-news"]').click()
        browser.element('[class="main-widget main-widget-news--active"]').should(be.enabled)

    @allure.step('Клик по кнопке закрытия блокирующего виджета')
    def close_block_widget(self):
        if browser.element('[class="adfox-bottom adfox-bottom-link__desk"]').wait_until(be.visible):
            browser.element('[class="adfox-bottom-close"]').click()

    @allure.step('Виджет "Python для новичков" отображается на странице')
    def widget_python_for_inners_is_visible(self):
        browser.element('[class="b-python-inner"]').perform(
            command.js.scroll_into_view).should(be.visible)
        browser.element('[class="b-python-title"]').should(have.text('Python с нуля'))

    @allure.step('Клик по виджету "Python для новичков"')
    def click_widget_python_for_inners(self):
        browser.element('[class="b-python-btn"]').perform(
            command.js.scroll_into_view).should(be.visible).click()

    @allure.step('Переход на новую вкладку')
    def switch_browser_tab(self):
        tabs = browser.driver.window_handles
        browser.driver.switch_to.window(tabs[1])

    @allure.step('Открылась новая вкладка, проверка заголовка статьи')
    def assert_widget_python_for_inners_title(self):
        browser.element('[class="mastrids-title"]').should(have.text('Язык программирования Python'))

    @allure.step('Скролл страницы к виджету подписки на рассылку')
    def subscribe_widget_is_visible(self):
        browser.element('[class="main-subscribe"]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element('[class="main-subscribe__title"]').should(
            have.text('Один мальчик подписался на рассылку Кода и постепенно стал программистом'))

    @allure.step('Ввод электронной почты в поле email')
    def type_email_field_in_subscribe_widget(self, email):
        browser.element('[class="main-subscribe__input"]').should(be.blank).type(email)

    @allure.step('Клик по чек боксу согласия на обработку персональных данных')
    def click_check_box_personal_data_agree(self):
        browser.element('[class="main-subscribe-checkbox"]').click()

    @allure.step('Проверка активности кнопки "Отправить"')
    def shoud_be_check_box_personal_data_agree_is_active(self):
        browser.element('[class="main-subscribe-checkbox main-subscribe-checkbox--active"]').perform(
            command.js.scroll_into_view).should(be.enabled)

    @allure.step('Скролл страницы к кнопке "Что там дальше?"')
    def scroll_to_load_more_button(self):
        browser.element('[class="alm-load-more-btn more "]').perform(command.js.scroll_into_view).should(be.visible)
        browser.element('[class="alm-load-more-btn more "]').should(have.text('Что там дальше?'))

    @allure.step('Клик по кнопке "Что там дальше?"')
    def click_load_more_button(self):
        browser.element('[class="alm-load-more-btn more "]').click()

    @allure.step('Проверка отображения дополнительных статей(12шт.)')
    def check_load_more_articles(self):
        browser.all('.alm-reveal .post').should(have.size(12))


main_page = MainPage()


'''
