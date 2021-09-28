from selenium import webdriver
from POM.statistics import StatisticsPage
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chromeOptions = Options()
    chromeOptions.headless = True
    chromeOptions.add_argument("--headless")
    chrome_driver_path = './Resources/chrome_linux/chromedriver'
    context.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chromeOptions)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://mystifying-beaver-ee03b5.netlify.app/')


def after_all(context):
    context.driver.close()


def before_feature(context, feature):
    print("Executing under before_scenario")
    context.stats_page = StatisticsPage(context.driver)
    context.stats_page.clear_filter()
    context.orig_table_data = context.stats_page.get_table_data()
