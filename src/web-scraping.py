from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import zipfile
import wget


# Constantes
OUTPUT = 'downloaded_pdfs'
ZIP = os.path.join(OUTPUT, 'pdfs.zip')  
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Funções de download e zip
def save_pdf_from_link(download_link, filename):
    wget.download(download_link, filename)

def create_zip_archive(zip_filename, downloaded_files):
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        for file in downloaded_files:
            zip_file.write(file, os.path.basename(file))

def main(): 
    # Selenium em modo headless (sem abrir janela)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    # Criar pasta de downloads
    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)

    downloaded_files = []

    try:
        # Acessar a página
        driver.get(URL)

        # Encontrar todos os links de PDFs com "Anexo" no href
        links = driver.find_elements(
            By.CSS_SELECTOR, 
            'a[href*="Anexo"][href$=".pdf"]'  # CSS Selector para links que contenham "Anexo" e terminem com .pdf
        )

        # Extrair URLs e fazer download
        for link in links:
            pdf_url = link.get_attribute("href")
            filename = os.path.join(OUTPUT, os.path.basename(pdf_url))
            save_pdf_from_link(pdf_url, filename)
            downloaded_files.append(filename)

        # Criar ZIP
        create_zip_archive(ZIP, downloaded_files)

    except Exception as e:
        print("Erro:", e)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()