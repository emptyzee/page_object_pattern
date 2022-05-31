import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import PlayGround1
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType

class PlayGround(BasePage):
    def data_ajax(self): # тест клика и ожидания появления текста
        buttontriggerajax = self.browser.find_element(*PlayGround1.BUTTONTRIGGERAJAX).click()
        waitfortext = WebDriverWait(self.browser, 16).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content>p")))
        content = self.browser.find_element(*PlayGround1.CONTENT).text
        assert "Data load" in content, f"not here"

    def class_attribute(self): #нажатие на кнопку и принятие алерта
        bluebutton = self.browser.find_element(*PlayGround1.BLUEBUTTON).click()
        alertwait = WebDriverWait(self.browser, 6).until(
            EC.alert_is_present())
        usualalert = self.browser.switch_to.alert.accept()

    def dynamic_table(self): # не работает
        chromecpu1 = self.browser.find_element(*PlayGround1.CHROMECPU).text
        chromecpu2 = self.browser.find_element(*PlayGround1.CHROMECPU2).text
        assert chromecpu1 in chromecpu2, f"not here"

    def alerts_confirm(self):# тест принятия алертов 
        self.browser.execute_script("window.scrollBy(0, 100);")
        simplealert = self.browser.find_element(*PlayGround1.SIMPLEALERT).click()
        alertwait = WebDriverWait(self.browser, 2).until(
            EC.alert_is_present())
        simplealertaccept = self.browser.switch_to.alert.accept()
        confirmalert = self.browser.find_element(*PlayGround1.CONFIRMALERT).click()
        confirmalertwait = WebDriverWait(self.browser, 2).until(
            EC.alert_is_present())
        confirmalertaccept = self.browser.switch_to.alert.accept()
        time.sleep(3)
        promptalertclick = self.browser.find_element(*PlayGround1.PROMPTALERT).click()
        prompalertwait = WebDriverWait(self.browser, 2).until(
            EC.alert_is_present())
        promptalert = self.browser.switch_to.alert
        promptalert.send_keys("123")
        promptalert.accept()
        time.sleep(5)

    def fake_alerts(self): # тест фейковых алертов
        fakealert1click = self.browser.find_element(*PlayGround1.FAKEALERT1).click()
        waitforfakealert1 = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#dialog-ok")))
        fakealert1accept = self.browser.find_element(*PlayGround1.FAKEALERT1ACCEPT).click()
        fakealert2 = self.browser.find_element(*PlayGround1.FAKEALERT2).click()
        waitforfakealert2 = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#dialog-ok")))
        fakealert2accept = self.browser.find_element(*PlayGround1.FAKEALERT1ACCEPT).click()
        time.sleep(3)

    @allure.feature("Check_html_form") # декоратор, отметка в коде при помощи которых будут генериться отчёты,заголовок отчёта
    @allure.story("Проверяем заполнение хтмл формы") # этот аллюр конкретизирует наши действия в отчёте
    @allure.severity("Blocker") # важность теста
    def basic_html_form(self): # заполнение html формы 
        self.browser.execute_script("window.scrollBy(0, 150);")
        username = self.browser.find_element(*PlayGround1.USERNAME).send_keys("Alex")
        password = self.browser.find_element(*PlayGround1.PASSWORD).send_keys("fannye1")
        textarea = self.browser.find_element(*PlayGround1.TEXTAREA)
        textarea.clear() # очистка поля
        textarea.click() # нажатие на поле
        textarea.send_keys("123456") # и отправка своих значений
        #send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE) второй вариант очистки поля
        sendfiles = self.browser.find_element(*PlayGround1.SENDFILE).send_keys("C:/Users/emptyzee/Desktop/пуккее.jpg")
        checkbox1 = self.browser.find_element(*PlayGround1.CHECKBOXDIS).click()
        checkbox2 = self.browser.find_element(*PlayGround1.CHECKBOXTAKE1).click()
        radio = self.browser.find_element(*PlayGround1.RADIOBUTTONS).click()
        select1 = Select(self.browser.find_element(*PlayGround1.SELECT1))
        select1.select_by_value("ms2") #select_by_visible_text можно выбрать по видимому тексту
        select2 = Select(self.browser.find_element(*PlayGround1.SELECT2))
        select2.select_by_value("dd5")
        time.sleep(5)
        submitbutton = self.browser.find_element(*PlayGround1.SUBMITBUTTON).click()
        with allure.step("Делаем скриншот"):
            allure.attach(self.browser.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)#делаем скриншот данным методом
        time.sleep(5)

    @allure.feature("Buttons_click_check")
    @allure.story("Тестируем нажатие кнопок")
    @allure.severity("Critical")
    def buttons_click(self): # тест нажатия кнопок
        onblur = self.browser.find_element(*PlayGround1.ONBLUR).click()
        achains = ActionChains(self.browser)
        onclick = self.browser.find_element(*PlayGround1.ONCLICK)
        achains.double_click(onclick).perform()
        righclick = self.browser.find_element(*PlayGround1.RIGHCLICK)
        achains.context_click(righclick).perform()
        doubleclick = self.browser.find_element(*PlayGround1.DOUBLECLICK)
        achains.double_click(doubleclick).perform()
        onfocus = self.browser.find_element(*PlayGround1.ONFOCUS).click()
        self.browser.execute_script("window.scrollBy(0, 250);")
        onkeydown = self.browser.find_element(*PlayGround1.ONKEYDOWN)
        onkeydown.click()
        onkeydown.send_keys(Keys.ENTER)
        onkeyup = self.browser.find_element(*PlayGround1.ONKEYUP)
        onkeyup.click()
        onkeyup.send_keys(Keys.ENTER)
        self.browser.execute_script("window.scrollBy(0, 150);")
        onkeypress = self.browser.find_element(*PlayGround1.ONKEYPRESS)
        onkeypress.click()
        onkeypress.send_keys(Keys.ENTER)
        mouseover = self.browser.find_element(*PlayGround1.MOUSEOVER).click()
        self.browser.execute_script("window.scrollBy(0, 150);")
        mouseleave = self.browser.find_element(*PlayGround1.MOUSELEFT).click()
        mouseover = self.browser.find_element(*PlayGround1.MOUSEOVER).click()
        mousedown = self.browser.find_element(*PlayGround1.MOUSEDOWN).click()
        time.sleep(5)


    @allure.feature("dynamic_button_waits")
    @allure.story("Нажатие кнопок с ожиданием их появления")
    @allure.severity("Critical")
    def dynamic_button(self): #динамические кнопки с ожиданием
        firstbutton = self.browser.find_element(*PlayGround1.FIRSTBUTTON).click()
        secondbuttonwait = WebDriverWait(self.browser, 6).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#button01")))
        secondbuttonclick = self.browser.find_element(*PlayGround1.SECONDBUTTON).click()
        thirdbuttonwait = WebDriverWait(self.browser, 6).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#button02")))
        thirdbutton = self.browser.find_element(*PlayGround1.THRIRDBUTTON).click()
        fourthbuttonwait = WebDriverWait(self.browser, 6).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#button03")))
        fourthbuttonclick = self.browser.find_element(*PlayGround1.FOURTHBUTTON).click()

    @allure.feature("dynamic_button_waits2")
    @allure.story("Нажатие кнопок с ожиданием их доступности")
    @allure.severity("Critical")
    def dynamic_ec_located(self): # ожидание и клик по кнопке
        firstbutton = self.browser.find_element(*PlayGround1.FIRSTBUTTON).click()
        secondbuttonwait = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button01")))
        secondbuttonclick = self.browser.find_element(*PlayGround1.SECONDBUTTON).click()
        thirdbuttonwait = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button02")))
        thirdbutton = self.browser.find_element(*PlayGround1.THRIRDBUTTON).click()
        fourthbuttonwait = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button03")))
        fourthbuttonclick = self.browser.find_element(*PlayGround1.FOURTHBUTTON).click()
        time.sleep(5) # ещё можно добавить assert self.browser.title == "Google" чтобы просто проверить, что мы на нужном сайте
         
