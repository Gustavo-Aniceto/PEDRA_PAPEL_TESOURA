import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import os  # Importe a biblioteca "os" para manipular caminhos de arquivo
def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif jogador == "pedra":
        return "Você ganhou! Pedra vence tesoura." if computador == "tesoura" else "Você perdeu! Papel vence pedra."
    elif jogador == "papel":
        return "Você ganhou! Papel vence pedra." if computador == "pedra" else "Você perdeu! Tesoura vence papel."
    elif jogador == "tesoura":
        return "Você ganhou! Tesoura vence papel." if computador == "papel" else "Você perdeu! Pedra vence tesoura."


def jogar(escolha_jogador):
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    resultado = verificar_vencedor(escolha_jogador, computador)
    mostrar_resultado(escolha_jogador, computador, resultado)

def mostrar_resultado(jogador, computador, resultado):
    img_jogador = Image.open(f"imagens/{jogador}.png")
    img_computador = Image.open(f"imagens/{computador}.png")

    img_jogador = img_jogador.resize((100, 100))
    img_computador = img_computador.resize((100, 100))

    img_jogador_tk = ImageTk.PhotoImage(img_jogador)
    img_computador_tk = ImageTk.PhotoImage(img_computador)

    label_jogador.config(image=img_jogador_tk)
    label_computador.config(image=img_computador_tk)

    label_resultado.config(text=resultado)

    label_jogador.image = img_jogador_tk
    label_computador.image = img_computador_tk
app = tk.Tk()
app.title("Pedra, Papel ou Tesoura")

escolha_var = tk.StringVar()
escolha_var.set("")

tk.Label(app, text="Escolha pedra, papel ou tesoura:", font=("Arial", 16)).grid(row=0, columnspan=3, pady=10)

# Lista para armazenar as imagens das opções
imagens_opcoes = []

# Crie os botões com as imagens das opções
opcoes = ["pedra", "papel", "tesoura"]
for index, opcao in enumerate(opcoes):
    img_opcao = Image.open(f"imagens/{opcao}.png")
    img_opcao = img_opcao.resize((100, 100))
    img_opcao_tk = ImageTk.PhotoImage(img_opcao)
    imagens_opcoes.append(img_opcao_tk)  # Adicione a imagem à lista

    tk.Button(app, image=img_opcao_tk, command=lambda escolha=opcao: jogar(escolha)).grid(row=1, column=index, padx=10, pady=10)

# Crie uma linha de separação usando o widget ttk.Separator
ttk.Separator(app, orient=tk.HORIZONTAL).grid(row=2, columnspan=3, sticky="ew", pady=10)

label_jogador = tk.Label(app)
label_jogador.grid(row=3, column=0, padx=20, pady=10)

label_computador = tk.Label(app)
label_computador.grid(row=3, column=2, padx=20, pady=10)

label_resultado = tk.Label(app, text="", font=("Arial", 16))
label_resultado.grid(row=4, columnspan=3, pady=10)

app.mainloop()