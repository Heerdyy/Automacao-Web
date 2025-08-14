from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

upd_navegador = Service(ChromeDriverManager().install()) # váriavel que será instanciada e fará uma checkagem da versão do webdriver do chrome para a utilização e retornará o path do arquivo para o driver caso esteja em uma versão desatualizada
navegador = webdriver.Chrome(service=upd_navegador) # objeto que será utilizado para a interagir com o navegador 

navegador.get('https://practicetestautomation.com/practice-test-login/') # abre o site
navegador.find_element('xpath', '//*[@id="username"]').send_keys('student') # procura o elemento e envia a credencial
navegador.find_element('xpath', '//*[@id="password"]').send_keys('Password123')
navegador.find_element('xpath', '//*[@id="submit"]').click() # procura o elemeto e clicka no button
input()
