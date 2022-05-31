import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pages.playground import PlayGround
from pages.base_page import BasePage



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="my options: type1 or type 2")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()  #pytest -v -m smoke --tb=line --language=en test_main_page.py  zapusk testa


def test_data_ajax(browser): # тест клика и ожидания появления текста
    link = "http://uitestingplayground.com/ajax"
    page1 = PlayGround(browser,link)
    page1.open()
    page1.data_ajax()

 
def test_class_attribute(browser): #нажатие на кнопку и принятие алерта
    link = "http://uitestingplayground.com/classattr"
    page2 = PlayGround(browser,link)
    page2.open()
    page2.class_attribute()


def test_alerts_acceptions(browser):# тест принятия алертов 
    link = "https://testpages.herokuapp.com/styled/alerts/alert-test.html"
    page3 = PlayGround(browser,link)
    page3.open()
    page3.alerts_confirm()


def test_fake_alerts(browser):# тест фейковых алертов
    link = "https://testpages.herokuapp.com/styled/alerts/fake-alert-test.html"
    page4 = PlayGround(browser,link)
    page4.open()
    page4.fake_alerts()


def test_html_basic_form(browser): # заполнение html формы 
    link = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"
    page5 = PlayGround(browser,link)
    page5.open()
    page5.basic_html_form()



def test_buttons_click(browser):# тест нажатия кнопок
    link = "https://testpages.herokuapp.com/styled/events/javascript-events.html"
    page6 = PlayGround(browser,link)
    page6.open()
    page6.buttons_click()


def test_dynamic_buttons(browser):#динамические кнопки с ожиданием
    link = "https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html"
    page7 = PlayGround(browser,link)
    page7.open()
    page7.dynamic_button()


@pytest.mark.smoke
def test_dynamic_ec_located(browser):# ожидание и клик по кнопке
    link = "https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html"
    page8 = PlayGround(browser,link)
    page8.open()
    page8.dynamic_ec_located()

