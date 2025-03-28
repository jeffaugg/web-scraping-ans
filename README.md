# PDF Downloader com Selenium

Este projeto tem como objetivo acessar uma página do governo, identificar links de arquivos PDF (especificamente aqueles que possuem "Anexo" no href e terminam com `.pdf`), realizar o download desses arquivos e compactá-los em um arquivo ZIP. O projeto utiliza Selenium em modo headless para o web scraping, o módulo `wget` para efetuar os downloads e a biblioteca `zipfile` do Python para criar o arquivo ZIP.

## Sumário

- [Tecnologias e Dependências](#tecnologias-e-dependências)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
    - [Execução Local](#execução-local)
    - [Execução via Docker](#execução-via-docker)
- [Uso e Funcionamento](#uso-e-funcionamento)
- [Considerações Finais](#considerações-finais)

## Tecnologias e Dependências

- **Linguagem:** Python 3.9 ou superior
- **Web Scraping:** Selenium
- **Navegador:** Google Chrome (executado em modo headless)
- **Download de Arquivos:** Módulo `wget`
- **Compactação:** Biblioteca `zipfile` do Python
- **Containerização:** Docker e Docker Compose

### Dependências Python

As principais dependências estão listadas no arquivo `requirements.txt`:

- `selenium`
- `wget`

## Estrutura do Projeto

```plaintext
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── src
│   └── web-scraping.py  # Script principal de scraping e download
└── downloaded_pdfs            # Pasta onde os PDFs baixados e o arquivo ZIP serão armazenados
```

## Instalação e Configuração

### Execução Local

Para rodar o projeto localmente, siga os passos abaixo:

1. **Pré-requisitos:**
     - Python 3.9 ou superior
     - Google Chrome instalado

2. **Clone o repositório e acesse o diretório:**

     ```bash
     git clone https://github.com/jeffaugg/web-scraping-ans
     cd web-scraping-ans
     ```

3. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux/macOS
     venv\Scripts\activate     # Windows
     ```

4. **Instale as dependências:**

     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     ```

5. **Execute o script:**

     ```bash
     python src/web-scraping.py
     ```

### O script realiza as seguintes etapas:

- Inicializa o Selenium em modo headless.
- Cria a pasta para armazenar os PDFs.
- Acessa a URL configurada e busca links de PDFs.
- Realiza o download dos arquivos.
- Compacta os arquivos baixados em um arquivo `pdfs.zip`.

### Execução via Docker

Se você não possui o Google Chrome instalado ou prefere isolar o ambiente, utilize o Docker:

1. **Pré-requisitos:**
     - Docker e Docker Compose instalados na máquina

2. **Construa a imagem Docker:**

     ```bash
     docker-compose build
     ```

3. **Inicie o container:**

     ```bash
     docker-compose up
     ```

     Para rodar em modo detach (segundo plano), utilize:

     ```bash
     docker-compose up -d
     ```

4. **Os arquivos baixados serão salvos na pasta local `./downloaded_pdfs`, mapeada para o diretório `/app/downloaded_pdfs` dentro do container.**



## Uso e Funcionamento

- **Selenium Headless:** O Selenium é configurado para rodar sem abrir uma janela do navegador, utilizando as opções `--headless=new` e `--no-sandbox`.
- **Download dos PDFs:** A função `save_pdf_from_link` utiliza o módulo `wget` para baixar os arquivos PDF dos links identificados.
- **Criação do ZIP:** Após o download, a função `create_zip_archive` cria um arquivo ZIP contendo todos os PDFs baixados.
- **Tratamento de Erros:** O script possui tratamento básico de exceções, exibindo mensagens de erro e garantindo que o driver seja encerrado corretamente.