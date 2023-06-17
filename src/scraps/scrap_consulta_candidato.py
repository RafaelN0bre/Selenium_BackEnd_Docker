from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without a GUI)

def set_chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

# Create a new instance of the Chrome driver
navegador = webdriver.Chrome(options=set_chrome_options())


# navegador.get(os.getenv("RESULT_URL"))
navegador.get("https://security.cebraspe.org.br/ConsultaOnline/UNB_23_ACESSOENEM/1983/7d6638f3-928d-46f4-b7bd-9ace99ad2b70/Consulta")

def send_name(name):
    actions = ActionChains(navegador)

    nomeConsultaInput = navegador.find_element(By.ID, "NomeConsulta")

    nomeConsultaInput.clear()
    actions.click(nomeConsultaInput).send_keys(name).send_keys(Keys.RETURN).perform()

def consulta_candidato(name):
    
    send_name(name)
    html = navegador.page_source
    if '<h2 style="text-align:center; margin-top:50px">Nenhum candidato encontrado</h2>' in html:
        return False
    else:
        return True
