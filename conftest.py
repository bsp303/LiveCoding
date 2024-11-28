import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.page_load_strategy = "normal"
    # Указываем что браузер запускается в фоновом режиме
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-cache")  # отключение кэша (все страницы загружаются с нуля)
    options.add_argument("--window-size=1920,1080")
    # Указываем что браузер запускается в полноразмерном режиме
    # options.add_argument("--incognito")  # режим инкогнито
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()
