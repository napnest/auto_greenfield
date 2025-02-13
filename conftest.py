import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# инициализирует драйвер для тестов
@pytest.fixture(scope="function", autouse=True) # будет использоваться автоматически для каждого теста
# и будет создавать экземпляр драйвера (открывать браузер) для каждого теста отдельно
def driver(request):
    options = Options()
    options.add_argument("--headless") # чтобы запускать тесты в ci, докере и т. д.
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver # создает объект драйвера внутри тестовых классов
    yield driver # возвращаем драйвер
    driver.quit()
    