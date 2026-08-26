TUTORIAL: CRIAR E CENTRALIZAR A BIBLIOTECA E COMANDO CLI (print_text_dgp)
===============================================================================
## 📋 Sumário
1. [ESTRUTURA DA PASTA DO PROJETO LOCAL](#1-ESTRUTURA-DA-PASTA-DO-PROJETO-LOCAL)
2. [PUBLICAR NO GITHUB](#2-PUBLICAR-NO-GITHUB)
3. [INSTALAR E ATUALIZAÇÕES](#3-INSTALAR-E-ATUALIZAÇÕES)
4. [COMO USAR NOS SEUS PROJETOS](#4-COMO-USAR-NOS-SEUS-PROJETOS)
5. [EXEMPLOS DE CÓDIGO DE COMO UTILIZAR](#5-EXEMPLOS-DE-CÓDIGO-DE-COMO-UTILIZAR)

---------------------------------------------------------
## 1. ESTRUTURA DA PASTA DO PROJETO LOCAL
---------------------------------------------------------
Crie uma pasta com o nome print_text_dgp e coloque os dois arquivos dentro dela:
```
print_text_dgp/
    ├── print_text_dgp.py
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE (Opcional)
    ├── .gitignore
    ├── .editorconfig
    ├── requirements-dev.txt
    └── CHANGELOG.md
```
---------------------------------------------------------
## 2. PUBLICAR NO GITHUB
---------------------------------------------------------
Repositório público ou privado no GitHub com o nome print_text_dgp.

URL do repositório: https://github.com/davigopi/print_text_dgp

---------------------------------------------------------
## 3. INSTALAR E ATUALIZAÇÕES
---------------------------------------------------------

Abra o terminal do seu computador, ative o ambiente virtual e, no diretório do repositório print_text_dgp, execute

### A) INSTALAR A FERRAMENTA NO COMPUTADOR
```bash
pip install git+https://github.com/davigopi/print_text_dgp.git
```

### B) ATUALIZAR A FERRAMENTA NO FUTURO

Alterado a version em pyproject.toml:
```bash
pip install --upgrade git+https://github.com/davigopi/print_text_dgp.git
```
Força a atualização:
```bash
pip install --force-reinstall git+https://github.com/davigopi/print_text_dgp.git
```
```bash
pip install --upgrade --no-cache-dir git+https://github.com/davigopi/print_text_dgp.git
```

### C) INSTALAR REQUIREMENTS

```bash
pip install -r venv\Lib\site-packages\print_text_dgp\requirements.txt
```
---------------------------------------------------------
## 4. COMO USAR NOS SEUS PROJETOS
---------------------------------------------------------
- Via importação dentro de scripts Python futuros:
```python
from print_text_dgp import Print_Text_Dgp
```
```python
import print_text_dgp
```
- Via terminal (em qualquer pasta de projeto React Native, Python, etc.):
  Basta abrir o terminal na pasta desejada e digitar:
```bash
python -m print_text_dgp
```
---------------------------------------------------------
## 5. EXEMPLOS DE CÓDIGO DE COMO UTILIZAR
---------------------------------------------------------

### A) Exemplo Básico (Inicialização e Verificação Simples)
```python
import time
from print_text import Print_Text_Dgp

# Instancia a classe responsável por formatar e exibir os logs no console
printer = Print_Text_Dgp()

# Define a estrutura básica do dicionário de estado/log
dict_print = {
    "cabecalho_1": "TAREFA 1",
    "cabecalho_2": "INICIAL",
    "cabecalho_3": "STATUS",
    "cabecalho_4": "OK",
    "cabecalho_5": "INICIO",
    "acao_exe": "EXECUTANDO - ",
    "text": "Iniciando a execução do fluxo simples..."
}

# Atualiza a tela e recebe o dicionário atualizado para manter o estado
dict_print = printer.before_execution(dict_print)
time.sleep(1)
```

### B) Exemplo Avançado (Tratamento de Modais, Loading e Exceções)
```python
import time
from typing import Dict, Any
from print_text import Print_Text_Dgp

def executar_fluxo_com_tratamento():
    printer = Print_Text_Dgp()
    
    # Estrutura inicial do estado
    dict_print: Dict[str, Any] = {
        "cabecalho_1": "AUTOMAÇÃO WEB",
        "cabecalho_2": "PROCESSO PRINCIPAL",
        "cabecalho_3": "ETAPA DE DADOS",
        "cabecalho_4": "EM ANDAMENTO",
        "cabecalho_5": "INICIALIZANDO",
        "acao_exe": "STATUS - ",
        "text": "Iniciando o carregamento da página...",
        "text_log": "",
        "text_log_anterior": ""
    }

    try:
        # Passos de execução normal
        dict_print["cabecalho_5"] = "NAVEGAÇÃO"
        dict_print["text"] = "Acessando URL do sistema..."
        dict_print = printer.before_execution(dict_print)
        time.sleep(1)

        dict_print["cabecalho_5"] = "TRATAMENTO DE MODAL"
        dict_print["text"] = "Verificando presença de modal de aviso..."
        dict_print = printer.before_execution(dict_print)
        time.sleep(1)

        # Simulação de carregamento / loader
        dict_print["cabecalho_5"] = "AGUARDANDO LOADING"
        dict_print["text"] = "Aguardando o descarregamento dos elementos da tela..."
        dict_print = printer.before_execution(dict_print)
        time.sleep(1)

        # Simulação de erro durante o processo
        raise TimeoutError("Tempo limite excedido ao aguardar a confirmação do modal.")

    except Exception as e:
        # Tratamento e atualização dos cabeçalhos em caso de falha
        dict_print["cabecalho_4"] = "FALHA"
        dict_print["cabecalho_5"] = "EXCEÇÃO CAPTURADA"
        dict_print["text"] = f"Erro detectado: {str(e)}"
        dict_print = printer.before_execution(dict_print)

if __name__ == "__main__":
    executar_fluxo_com_tratamento()
```

### C) Exemplo de Execução CLI / Teste Integrado
```bash
# Executar o script diretamente via linha de comando
python print_text.py

# Caso utilize um ambiente virtual (venv)
# No Linux/macOS:
source venv/bin/activate && python print_text.py

# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1; python print_text.py
```
