# Extração de dados API

## Sobre o Projeto
Este repositório faz parte de uma **LIVE do YouTube**. 


### Pré-requisitos

1. **VSCode:** 
   - Editor de código utilizado no workshop. [Instruções de instalação](https://code.visualstudio.com/).

2. **Git e GitHub:**
   - Instale o Git: [Instruções de instalação](https://git-scm.com/).
   - Crie uma conta no GitHub: [Guia de criação de conta](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account).

3. **Pyenv:**
   - Gerenciador de versões do Python. [Instruções de instalação](https://github.com/pyenv/pyenv).
   - Versão usada neste projeto: **Python 3.12.1**.
     - **Usuários Windows:** Recomenda-se assistir este [tutorial no YouTube](https://www.youtube.com/).

4. **Poetry:**
   - Gerenciador de dependências. [Instruções de instalação](https://python-poetry.org/docs/).
     - **Usuários Windows:** Este [vídeo no YouTube](https://www.youtube.com/) cobre instalação de Python, Poetry e VSCode.
     - Alternativamente, use: `pip install poetry`.

---

## Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gustavobi4yourdata/yt-Etl-Project-Api-Extract.git
   cd yt-Etl-Project-Api-Extract
   ```

2. **Configure a versão correta do Python com Pyenv:**
   ```bash
   pyenv install 3.12.1
   pyenv local 3.12.1
   ```

3. **Configure o Poetry para usar o Python 3.12.1 e ative o ambiente virtual:**
   ```bash
   poetry env use 3.12.1
   poetry shell
   ```

4. **Instale as dependências do projeto:**
   ```bash
   poetry install
   ```

5. **Sobe container postgreSQL**
   ```bash
   docker compose up -d
   ```

6. **Execute pipeline:**
   ```bash
   python src/extract_api.py
   ```

7. **Execute o streamlit dashboard:**
   ```bash
   cd app
   streamlit run dashboad_01.py 
   ```

---

## Agredecimetos

- **Jornada de Dados - Luciano Galvão**:
https://suajornadadedados.com.br
