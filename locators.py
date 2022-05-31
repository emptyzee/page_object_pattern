from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class PageProductLocators():
    ADD_TO_BASKET = (By.CLASS_NAME,"btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class MainPageGuru():
    USER_ID = (By.CSS_SELECTOR,'input[name="uid"]')
    PASSWORD = (By.CSS_SELECTOR,'input[name="password"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR,"input[name='btnLogin']")
    WELCOME_TEXT = (By.CSS_SELECTOR,".heading3:nth-child(3) td")

class DemoShop():
    PRICE_LAPTOP = (By.CSS_SELECTOR,'.item-box:nth-child(3) .price')
    ADD_BUTTON = (By.CSS_SELECTOR,'.item-box:nth-child(3) .button-2')
    BASKET_BUTTON = (By.CSS_SELECTOR,'#topcartlink')
    OPTION1 = (By.CSS_SELECTOR,'[value="2231467"]')

class NewShop():
    BUTTON1 = (By.CSS_SELECTOR,"#homefeatured > .ajax_block_product:nth-child(2) .button:nth-child(1) > span")
    BUTTON2 = (By.CSS_SELECTOR,".button-medium > span")
    BUTTON3 = (By.CSS_SELECTOR,".standard-checkout > span")
    MESS = (By.CSS_SELECTOR,"#layer_cart h2")
    LOGIN_FORM = (By.CSS_SELECTOR,"#create-account_form")
    QUICK_VIEW = (By.CSS_SELECTOR,"#homefeatured > .ajax_block_product:nth-child(1) .replace-2x")
    PLUS = (By.CSS_SELECTOR,".icon-plus")
    SELECTS = (By.CSS_SELECTOR,"#group_1")
    SELECTM = (By.CSS_SELECTOR,"option:nth-child(2)")
    LOGIN = (By.CSS_SELECTOR,".login")
    EMAIL = (By.CSS_SELECTOR,"#email_create")
    SUBMITEMAIL = (By.CSS_SELECTOR,"#SubmitCreate")
    OPTION = (By.CSS_SELECTOR,"[value='1']")
    FIRST_NAME = (By.CSS_SELECTOR,"#customer_firstname")
    LAST_NAME = (By.CSS_SELECTOR,"#customer_lastname")
    PASSWORD = (By.CSS_SELECTOR,"#passwd")
    DAY = (By.CSS_SELECTOR,"#days")
    DAY27 = (By.CSS_SELECTOR,"#days>[value='27']")
    MONTH = (By.CSS_SELECTOR,"#months")
    MONTH4 = (By.CSS_SELECTOR,"#months>[value='4']")
    YEAR = (By.CSS_SELECTOR,"#years")
    YEAR1995 = (By.CSS_SELECTOR,"#years>[value='1995']")
    NEWS = (By.CSS_SELECTOR,"#newsletter")
    FIRSTNAME1 = (By.CSS_SELECTOR,"#firstname")
    LASTNAME1 = (By.CSS_SELECTOR,"#lastname")
    ADRESS = (By.CSS_SELECTOR,"#address1")
    CITY = (By.CSS_SELECTOR,"#city")
    STATE = (By.CSS_SELECTOR,"#id_state")
    STATE1 = (By.CSS_SELECTOR,"#id_state>[value='12']")
    ZIP = (By.CSS_SELECTOR,"#postcode")
    COUNTRY = (By.CSS_SELECTOR,"#id_country")
    COUNTRY1 = (By.CSS_SELECTOR,"#id_country>[value='21']")
    PHONE = (By.CSS_SELECTOR,"#phone_mobile")
    SUBMITREG = (By.CSS_SELECTOR,"#submitAccount")
    # ниже для обращение в CUSTOMER SERVICE - CONTACT US
    CONTACT_LINK = (By.CSS_SELECTOR,"#contact-link")
    SUBJECT_HEAD = (By.CSS_SELECTOR,"#id_contact")
    SUBJECT_HEADVALUE = (By.CSS_SELECTOR,"#id_contact>[value='2']")
    EMAILADRESS = (By.CSS_SELECTOR,"#email")
    IDORDER = (By.CSS_SELECTOR,"#id_order")
    TEXTAREA = (By.CSS_SELECTOR,"#message")
    SUBMITMESS = (By.CSS_SELECTOR,"#submitMessage")
    # ниже использование поиска и добавление в корзину + выбор размера + выбор количества
    SEARCH = (By.CSS_SELECTOR,"#search_query_top")
    SEARCHSUBM = (By.CSS_SELECTOR,".button-search")
    QUICKV = (By.CSS_SELECTOR,".ajax_block_product:nth-child(1) .replace-2x")
    SELECT1 = (By.CSS_SELECTOR,"#group_1")
    SELECTL = (By.CSS_SELECTOR,"#group_1>[value='3']")
    PLUSS1 = (By.CSS_SELECTOR,'.button-plus > span')
    COLOR = (By.CSS_SELECTOR,'#color_15')
    ADDTOCART = (By.CSS_SELECTOR,".exclusive > span")
    CHECKOUT = (By.CSS_SELECTOR,".button-medium:nth-child(2) > span")
    CHECKOUT2 = (By.CSS_SELECTOR,".standard-checkout > span")


class SauceDemo():
    # вход + добавление рюкзана + переход в корзину + чекаут + ввод имени и индекса
    USERNAME = (By.CSS_SELECTOR,"#user-name")
    PASSWORD = (By.CSS_SELECTOR,"#password")
    LOGINBUTTON = (By.CSS_SELECTOR,"#login-button")
    ADDBACKPUCK = (By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack")
    CART = (By.CSS_SELECTOR,"#shopping_cart_container")
    CHECKOUT = (By.CSS_SELECTOR,"#checkout")
    FIRSTNAME = (By.CSS_SELECTOR,"#first-name")
    LASTNAME = (By.CSS_SELECTOR,"#last-name")
    POSTAL = (By.CSS_SELECTOR,"#postal-code")
    CONTINUE = (By.CSS_SELECTOR,"#continue")
    #вход за заблокированого юзера
    ERORMES = (By.CSS_SELECTOR,"div>h3")

class DemoQa():
    FIRSTNAME = (By.CSS_SELECTOR,"#firstName")
    LASTNAME = (By.CSS_SELECTOR,"#lastName")
    EMAIL = (By.CSS_SELECTOR,"#userEmail")
    OPTION = (By.CSS_SELECTOR,".custom-radio:nth-child(1) > .custom-control-label")
    MOBILE = (By.CSS_SELECTOR,"#userNumber")
    DATEOFB = (By.CSS_SELECTOR,"#dateOfBirthInput")
    MONTH = (By.CSS_SELECTOR,".react-datepicker__month-select")
    MONTH3 = (By.CSS_SELECTOR,".react-datepicker__month-select>[value='3']")
    YEAR = (By.CSS_SELECTOR,".react-datepicker__year-select")
    YEAR1995 = (By.CSS_SELECTOR,".react-datepicker__year-select>[value='1995']")
    DAY = (By.CSS_SELECTOR,".react-datepicker__day--027:nth-child(5)")
    HOBBIES = (By.CSS_SELECTOR,".custom-checkbox:nth-child(1) > .custom-control-label")
    ADRESS = (By.CSS_SELECTOR,"#currentAddress")
    STATE = (By.CSS_SELECTOR,"#state")
    STATE1 = (By.CSS_SELECTOR,"#react-select-3-option-0")
    CITY = (By.CSS_SELECTOR,"#city")
    CITY1 = (By.CSS_SELECTOR,"#react-select-4-option-1")
    SUBMIT = (By.CSS_SELECTOR,"#submit") # практика, заполнение формы
    #check box ниже
    CHECKBOX = (By.CSS_SELECTOR,".rct-title")
    #text_box ниже #заполнение формы текстом 
    FULLNAME = (By.CSS_SELECTOR,"#userName")
    EMAIL = (By.CSS_SELECTOR,"#userEmail")
    CURRENTADRES = (By.CSS_SELECTOR,"#currentAddress")
    PERMAMENTADRES = (By.CSS_SELECTOR,"#permanentAddress")
    SUBMITBUTTON = (By.CSS_SELECTOR,"#submit")
    # ниже radiobutton
    YESRADIO = (By.CSS_SELECTOR,"[for = 'yesRadio']")
    IMPRESSIVERADIO = (By.CSS_SELECTOR,"[for='impressiveRadio']")
    # ниже webtables 
    ADDNEWUSER = (By.CSS_SELECTOR,"#addNewRecordButton")
    FIRSTN = (By.CSS_SELECTOR,"#firstName")
    LASTN = (By.CSS_SELECTOR,"#lastName")
    EMAIIIL = (By.CSS_SELECTOR,"#userEmail")
    AGE = (By.CSS_SELECTOR,"#age")
    SALARY = (By.CSS_SELECTOR,"#salary")
    DEPARTMENT = (By.CSS_SELECTOR,"#department")
    SUBMITBUT = (By.CSS_SELECTOR,"#submit")
    # ниже тест click buttons 
    DOUBLECLICK = (By.CSS_SELECTOR,"#doubleClickBtn")
    RIGHTCLICK = (By.CSS_SELECTOR,"#rightClickBtn")
    CLICKME = (By.CSS_SELECTOR,"div >.mt-4:nth-child(3)>button")
    # ниже регистрацию юзера
    NEWUSERBUT = (By.CSS_SELECTOR,"#newUser")
    FN = (By.CSS_SELECTOR,"#firstname")
    LN = (By.CSS_SELECTOR,"#lastname")
    USERNAME = (By.CSS_SELECTOR,"#userName")
    PSW = (By.CSS_SELECTOR,"#password")
    BUTTONREDISTER = (By.CSS_SELECTOR,"#register")
    CAPCHA = (By.CSS_SELECTOR,".recaptcha-checkbox-border")
    #ниже клики по алертам
    USUALALERT = (By.CSS_SELECTOR,"#alertButton")
    ALERTAFTER5SEC = (By.CSS_SELECTOR,"#timerAlertButton")
    CONFIRMALERT = (By.CSS_SELECTOR,"#confirmButton")
    PROMTALERT = (By.CSS_SELECTOR,"#promtButton")
    # ниже модальные окна
    SMALLMODAL = (By.CSS_SELECTOR,"#showSmallModal")
    CLOSESMALLMODAL = (By.CSS_SELECTOR,"#closeSmallModal")
    LARGEMODAL = (By.CSS_SELECTOR,"#showSmallModal")
    CLOSELARGEMODAL = (By.CSS_SELECTOR,"#closeSmallModal")
    # .react-datepicker__week:nth-child(5)>div:nth-child(5) локатор для датапикера 27 апреля
    #ниже датапикер
    SELECTDATECLICK = (By.CSS_SELECTOR,"#datePickerMonthYearInput")
    MONTHCLICK = (By.CSS_SELECTOR,".react-datepicker__month-select")
    MONTHAPRIL = (By.CSS_SELECTOR,".react-datepicker__month-select>[value='3']")
    YEARCLICK = (By.CSS_SELECTOR,".react-datepicker__year-select")
    YEAR195  = (By.CSS_SELECTOR,".react-datepicker__year-select>[value='1995']")
    DAY27 = (By.CSS_SELECTOR,".react-datepicker__week:nth-child(5)>div:nth-child(5)")
    # ниде датапикер с выбором времени
    SELECTDATAANDTIME = (By.CSS_SELECTOR,"#dateAndTimePickerInput")
    MONTHCLI = (By.CSS_SELECTOR,".react-datepicker__month-read-view")
    MONTHAPR = (By.CSS_SELECTOR,".react-datepicker__month-dropdown>div:nth-child(4)")
    DAY277 = (By.CSS_SELECTOR,".react-datepicker__month>div:nth-child(5)>div:nth-child(4)")
    TIME1 = (By.CSS_SELECTOR,".react-datepicker__time-box>.react-datepicker__time-list>.react-datepicker__time-list-item:nth-child(83)")
    # ниже прогресс бар
    STARTBUTTON = (By.CSS_SELECTOR,"#startStopButton")
    PROGGRESBAR = (By.CSS_SELECTOR,"#progressBar")
    # ниже select 
    SELECT1 = (By.CSS_SELECTOR,"#oldSelectMenu")
    # ниже книжный магазин
    LOGIN1 = (By.CSS_SELECTOR,"#userName")
    PASSWORD1 = (By.CSS_SELECTOR,"#password")
    LOGINBUTT = (By.CSS_SELECTOR,"#login")
    GOTOSTORE = (By.CSS_SELECTOR,"#gotoStore")
    ADDBOOK = (By.CSS_SELECTOR,".rt-tr-group>div>div>div>span>a")
    ADDTOBASKET = (By.CSS_SELECTOR,".profile-wrapper>div:nth-child(9)>div:nth-child(2)>#addNewRecordButton")
    #после свитч на алерт и принять
    SWAPTOPROFILE = (By.CSS_SELECTOR,".accordion>div:nth-child(6)>div>ul>li:nth-child(3)")
    DELETEBOOK = (By.CSS_SELECTOR,"#delete-record-undefined>svg>path")
    CONFIRMDELETE = (By.CSS_SELECTOR,"#closeSmallModal-ok")
    # ниже локаторы для явных ожиданий
    ENABLEAFTER5SEC = (By.CSS_SELECTOR,"#enableAfter")
    VISIBLEAFTER5SEC = (By.CSS_SELECTOR,"#visibleAfter")

class PlayGround1():
    # ниже тест клика и ожидания появления текста
    BUTTONTRIGGERAJAX = (By.CSS_SELECTOR,"#ajaxButton")
    CONTENT = (By.CSS_SELECTOR,"#content>p")
     #нажатие на кнопку и принятие алерта
    BLUEBUTTON = (By.CSS_SELECTOR,".class3")
    # ниже динамическая таблица и сравнение
    CHROMECPU = (By.CSS_SELECTOR,"div>div:nth-child(3)>div>span:nth-child(5)")
    CHROMECPU2 = (By.CSS_SELECTOR,".bg-warning")
    # внизу алерты
    SIMPLEALERT = (By.CSS_SELECTOR,"#alertexamples")
    CONFIRMALERT = (By.CSS_SELECTOR,"#confirmexample")
    PROMPTALERT = (By.CSS_SELECTOR,"#promptexample")
    # ниже фейкалертс
    FAKEALERT1 = (By.CSS_SELECTOR,"#fakealert")
    FAKEALERT1ACCEPT = (By.CSS_SELECTOR,"#dialog-ok")
    FAKEALERT2 = (By.CSS_SELECTOR,"#modaldialog")
    # ниже Basic HTML Form Example
    TEXTAREA = (By.CSS_SELECTOR,"tbody>tr:nth-child(3)>td>textarea")
    USERNAME = (By.CSS_SELECTOR,"tbody>tr>td>input")
    PASSWORD = (By.CSS_SELECTOR,"tbody>tr:nth-child(2)>td>input")
    SENDFILE = (By.CSS_SELECTOR,"tbody>tr:nth-child(4)>td>input[type='file']")
    CHECKBOXDIS = (By.CSS_SELECTOR,"tbody>tr:nth-child(5)>td>input:nth-child(4)")
    CHECKBOXTAKE1 = (By.CSS_SELECTOR,"tbody>tr:nth-child(5)>td>input:nth-child(2)")
    RADIOBUTTONS = (By.CSS_SELECTOR,"tbody>tr:nth-child(6)>td>input:nth-child(2)")
    SELECT1 = (By.CSS_SELECTOR,"tbody>tr:nth-child(7)>td>select")
    SELECT2 = (By.CSS_SELECTOR,"tbody>tr:nth-child(8)>td>select")
    SUBMITBUTTON = (By.CSS_SELECTOR,"tbody>tr:nth-child(9)>td>input:nth-child(2)")
    #ниже нажатие кнопок
    ONBLUR = (By.CSS_SELECTOR,"#onblur")
    ONCLICK = (By.CSS_SELECTOR,"#onclick")
    RIGHCLICK = (By.CSS_SELECTOR,"#oncontextmenu")
    DOUBLECLICK = (By.CSS_SELECTOR,"#ondoubleclick")
    ONFOCUS = (By.CSS_SELECTOR,"#onfocus")
    ONKEYDOWN = (By.CSS_SELECTOR,"#onkeydown")
    ONKEYUP = (By.CSS_SELECTOR,"#onkeyup")
    ONKEYPRESS = (By.CSS_SELECTOR,"#onkeypress")
    MOUSEOVER = (By.CSS_SELECTOR,"#onmouseover")
    MOUSELEFT = (By.CSS_SELECTOR,"#onmouseleave")
    MOUSEDOWN = (By.CSS_SELECTOR,"#onmousedown")
    #ниже динамические кнопки с ожиданием
    FIRSTBUTTON = (By.CSS_SELECTOR,"#button00")
    SECONDBUTTON = (By.CSS_SELECTOR,"#button01")
    THRIRDBUTTON = (By.CSS_SELECTOR,"#button02")
    FOURTHBUTTON = (By.CSS_SELECTOR,"#button03")

class XyzBank1():
    MANAGERLOGINBUTTON = (By.CSS_SELECTOR,".center:nth-child(3)>button")
    ADDCUSTOMER = (By.CSS_SELECTOR,".btn-lg")
    FIRSTNAME = (By.CSS_SELECTOR,".marTop>form>div>input")
    LASTNAME = (By.CSS_SELECTOR,".marTop>form>div:nth-child(2)>input")
    POSTCODE = (By.CSS_SELECTOR,".marTop>form>div:nth-child(3)>input")
    ADDBUTTON = (By.CSS_SELECTOR,".marTop>form>button")


class GlobalQa1():
    #тест html формы
    PROFILEPIC = (By.CSS_SELECTOR,".wpcf7>form>p>span>input")
    NAME = (By.CSS_SELECTOR,"#g2599-name")
    EMAIL = (By.CSS_SELECTOR,"#g2599-email")
    SELECTEXP = (By.CSS_SELECTOR,"#g2599-experienceinyears")
    RADIOBUTTON1 = (By.CSS_SELECTOR,"#contact-form-2599>form>div:nth-child(5)>label:nth-child(4)>input")
    RADIOBUTTON2 = (By.CSS_SELECTOR,"#contact-form-2599>form>div:nth-child(6)>label:nth-child(2)>input")
    BUTTONTOALERT = (By.CSS_SELECTOR,"#contact-form-2599>form>button")
    TEXTAREA = (By.CSS_SELECTOR,"#contact-form-2599>form>div:nth-child(12)>textarea")
    SUBMITBUTTON = (By.CSS_SELECTOR,"#contact-form-2599>form>p:nth-child(13)>button")
    #ниже тест обычной регистрации
    REGISTERBUTTON1 = (By.CSS_SELECTOR,".form-actions>a")
    FIRSTNAME = (By.CSS_SELECTOR,"#firstName")
    LASTNAME = (By.CSS_SELECTOR,"#Text1")
    USERNAME = (By.CSS_SELECTOR,"#username")
    PASSWORD = (By.CSS_SELECTOR,"#password")
    REGISTERBUTTON2 = (By.CSS_SELECTOR,".form-actions>button")