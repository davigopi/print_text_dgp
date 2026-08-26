import sys
import os
from typing import Any, Dict

class Print_Text_Dgp:
    def __init__(self, *args, **kwargs):
        self.separador = 80*"_"
        self.dict_print = {}

    def clear_screen(self) -> None:

        # 1. Tenta ANSI
        sys.stdout.write("\033[2J\033[3J\033[H")
        sys.stdout.flush()

        # 2. Limpa usando comando do Windows
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        # 3. Reposiciona o cursor no início
        sys.stdout.write("\033[H")
        sys.stdout.flush()

    def _ensure_value_dict(self) -> None:
        """Garante que todas as chaves existam e contenham apenas valores do tipo string."""
        chaves = ("cabecalho_1", "cabecalho_2", "cabecalho_3", "cabecalho_4", "cabecalho_5",
            "cabecalho_5_anterior", "cabecalho_test", "cabecalho_test_anterior", "cabecalho_anterior",
            "acao_exe", "text", "text_log", "text_log_anterior"
        )
        for chave in chaves:
            valor = self.dict_print.get(chave)
            self.dict_print[chave] = "" if valor is None else str(valor)

    def before_execution(self, dict_print: Dict[str, Any]) -> Dict:
        self.dict_print = dict_print
        self._ensure_value_dict()

        self.dict_print["cabecalho_test"] = (
            self.dict_print["acao_exe"] + 
            self.dict_print["cabecalho_1"] + 
            self.dict_print["cabecalho_3"] + 
            self.dict_print["cabecalho_2"] + 
            self.dict_print["cabecalho_4"]
        )

        if self.dict_print["cabecalho_test_anterior"] and self.dict_print["cabecalho_test"] != self.dict_print["cabecalho_test_anterior"]:
            self.dict_print["text_log_anterior"] = self.dict_print["text_log"]
            self.dict_print["cabecalho_anterior"] = (
                self.dict_print["cabecalho_test_anterior"] + self.dict_print["cabecalho_5_anterior"]
            )
            self.dict_print["text_log"] = ""

        self.dict_print["cabecalho_test_anterior"] = self.dict_print["cabecalho_test"]

        if self.dict_print["text"]:
            if (self.dict_print["cabecalho_5_anterior"] and 
                self.dict_print["cabecalho_5_anterior"] != self.dict_print["cabecalho_5"] and 
                self.dict_print["text_log"]):
                self.dict_print["text_log"] += "\n" + self.dict_print["text"]
            else:
                self.dict_print["text_log"] += self.dict_print["text"]
                
        self.dict_print["cabecalho_5_anterior"] = self.dict_print["cabecalho_5"]


        partes = []
        if self.dict_print["text_log_anterior"]:
            partes.append(f'{self.separador}\nBEFORE {self.dict_print["cabecalho_anterior"]}\n{self.separador} ')
            partes.append(self.dict_print["text_log_anterior"])
        partes.append(f'{self.separador}\nEXECUTION {self.dict_print["cabecalho_test"] + self.dict_print["cabecalho_5"]}\n{self.separador} ')
        partes.append(self.dict_print["text_log"])
        text_print = "\n".join(partes)
        self.clear_screen()
        print(text_print,  flush=True)
        return self.dict_print


if __name__ == "__main__":
    import time

    print_text = Print_Text_Dgp()
    
    # Estrutura base de dados
    dict_print = {
        "cabecalho_1": "TAREFA 1",
        "cabecalho_2": "PRIMEIRA",
        "cabecalho_3": "EXECUCAO",
        "cabecalho_4": "SUCESSO",
        "cabecalho_5": "INICIO",
        "cabecalho_5_anterior": "",
        "cabecalho_test": "",
        "cabecalho_test_anterior": "",
        "cabecalho_anterior": "",
        "acao_exe": "PROCESSANDO - ",
        "text": "Iniciando tarefa 1",
        "text_log": "",
        "text_log_anterior": "",
    }

    # Passos da Tarefa 1
    passos_tarefa_1 = [
        ("INICIO", "Iniciando tarefa 1"),
        ("BOTAO 1", "Clicando no botão 1"),
        ("INFORMACAO", "Pegando informação"),
        ("VALIDACAO", "Validando informação"),
        ("FINALIZACAO", "Finalizando tarefa 1"),
    ]

    for c5, txt in passos_tarefa_1:
        dict_print["cabecalho_5"] = c5
        dict_print["text"] = txt
        # Recebe o dicionario atualizado a cada iteracao
        dict_print = print_text.before_execution(dict_print)
        time.sleep(1)

    # Transição para a Tarefa 2 (Altera cabeçalhos principais)
    dict_print.update({
        "cabecalho_1": "TAREFA 2",
        "cabecalho_2": "SEGUNDA",
        "cabecalho_3": "EXECUCAO",
        "cabecalho_4": "ERRO",
    })

    # Passos da Tarefa 2
    passos_tarefa_2 = [
        ("INICIO", "Iniciando tarefa 2"),
        ("BOTAO 1", "Clicando no botão 1"),
        ("INFORMACAO", "Pegando informação"),
        ("ERRO", "Erro ao obter informação"),
    ]

    for c5, txt in passos_tarefa_2:
        dict_print["cabecalho_5"] = c5
        dict_print["text"] = txt
        dict_print = print_text.before_execution(dict_print)
        time.sleep(1)