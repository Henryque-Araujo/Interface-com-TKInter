import tkinter as tk
import requests

# Função para consultar o banco na API
def consultar_banco():
    codigo = entry_codigo.get().strip()
    if not codigo:
        label_resultado_consulta["text"] = "Resultado da Consulta: Informe o Código do Banco."
        label_nome_banco["text"] = ""
        return

    try:
        # URL da API (Exemplo: Banco Central do Brasil - substitua se necessário)
        url = f"https://brasilapi.com.br/api/banks/v1/{codigo}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            nome_banco = data.get("name", "Não informado")
            label_resultado_consulta["text"] = "Resultado da Consulta: Banco Cadastrado na Base"
            label_nome_banco["text"] = nome_banco
        else:
            label_resultado_consulta["text"] = "Resultado da Consulta: Banco Inválido"
            label_nome_banco["text"] = ""
    except Exception as e:
        label_resultado_consulta["text"] = "Erro ao consultar a API."
        label_nome_banco["text"] = ""

# Configuração principal
root = tk.Tk()
root.title("Unidade 07 - Questão Aleatória 02")
root.geometry("500x300")
root.resizable(False, False)

# Cabeçalho
frame_top = tk.Frame(root, bg="white", height=50)
frame_top.pack(fill=tk.X)
label_titulo = tk.Label(
    frame_top,
    text="Consulta Nome do Banco pelo Código",
    bg="white",
    font=("Arial", 12, "bold"),
)
label_titulo.pack(pady=10)

# Corpo principal
frame_middle = tk.Frame(root, bg="lightgray")
frame_middle.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Campo para informar o código do banco
label_codigo = tk.Label(
    frame_middle, text="Informe o Código do Banco:", bg="lightgray", font=("Arial", 10)
)
label_codigo.grid(row=0, column=0, sticky="w", pady=5)
entry_codigo = tk.Entry(frame_middle, font=("Arial", 10), width=10)
entry_codigo.grid(row=0, column=1, pady=5)

# Botão Consultar Banco
btn_consultar = tk.Button(
    frame_middle,
    text="Consultar Banco",
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    command=consultar_banco,
)
btn_consultar.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

# Resultado da Consulta
label_resultado = tk.Label(
    frame_middle,
    text="Resultado da Consulta:",
    bg="lightgray",
    font=("Arial", 10),
)
label_resultado.grid(row=2, column=0, sticky="w", pady=5)
label_resultado_consulta = tk.Label(
    frame_middle,
    text="",
    bg="gray",
    fg="white",
    font=("Arial", 10),
    width=30,
    anchor="w",
)
label_resultado_consulta.grid(row=2, column=1, pady=5)

# Nome do Banco
label_nome_banco = tk.Label(
    frame_middle,
    text="",
    bg="yellow",
    fg="black",
    font=("Arial", 12, "bold"),
    anchor="center",
)
label_nome_banco.grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)

root.mainloop()
