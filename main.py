import tkinter
import math
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# importacoes

import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

# cores

cor0 = "#0D0000" # preto
cor1 = "#feffff" # branca
cor2 = "#6CE8F0" # azul

# fundos

fundo_dia = "#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)

# criando frames

frame_top = Frame(janela, width=320, height=50, bg=cor1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

global image 

# funcao que retorna as informacoes
def informacao():
 
    chave = 'b72d9223189dcb9fc0d75c4dbe91c051'
    cidade = e_local.get()
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)


    # fazendo chamada da API 
    r = requests.get(api_link)

    # convertendo os dados presentes na variável r em dicionário
    dados = r.json()
   
    # obtendo zona, país e horas

    pais_codigo = dados['sys']['country']

    # zona
    zona_fuso = pytz.country_timezones[pais_codigo]

    # pais
    pais = pytz.country_names[pais_codigo]

    # data
    zona = pytz.timezone(zona_fuso[0])

    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %y | %H:%M:%S %p")

    # tempo
    temp = dados['main']['temp']
    pressao = dados['main']['pressure']
    umidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']


    # conversor de temperatura para celsius

    C = temp - 273

    # mudando informacoes

    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)

        return pais_continente_nome

    continente = pais_para_continente(pais)

    # passando informacoes nas labels

    l_temp['text'] = round(C)
    l_temp_nome['text'] = "°C"
    l_cidade['text'] = cidade + " - " + pais +  " / " + continente
    l_data['text'] = zona_horas
    l_umidade['text'] = umidade
    l_umidade_simbolo['text'] = '%'
    l_umidade_nome['text'] = 'Umidade'
    l_pressao['text'] = "Pressão:" + str(pressao)
    l_velocidade['text'] = "Velocidade do vento:" + str(velocidade)
    l_descricao['text'] = descricao

    # trocar o fundo

    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H")

    global image 

    zona_periodo = int(zona_periodo)

    if zona_periodo <= 5:
        imagem = Image.open('Imagens/noite.png')
        fundo = fundo_noite
    elif zona_periodo <=11:
        imagem = Image.open('Imagens/sol.png')
        fundo = fundo_dia
    elif zona_periodo <= 17:
        imagem = Image.open('Imagens/sol_tarde.png')
        fundo = fundo_tarde
    elif zona_periodo <= 23:
        imagem = Image.open('Imagens/noite.png')
        fundo = fundo_noite
    else:
        pass


    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_icon = Label(frame_corpo, image= imagem, bg=fundo)
    l_icon.place(x=165,y=60)

    # passando informacoes nas labels

    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)

    l_temp['bg'] = fundo
    l_temp_nome['bg'] = fundo
    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_umidade['bg'] = fundo
    l_umidade_simbolo['bg'] = fundo
    l_umidade_nome['bg'] = fundo
    l_pressao['bg'] = fundo
    l_velocidade['bg'] = fundo
    l_descricao['bg'] = fundo


# configurando frame_top

e_local = Entry(frame_top, width=20,justify='left',font=("",14), highlightthickness=1, relief='solid')
e_local.place(x=15,y=10)
b_ver = Button(frame_top, command=informacao, text='Ver clima', bg= cor1, fg=cor2, font=("Ivy 9"), highlightthickness=1, relief='raised', overrelief=RIDGE)
b_ver.place(x=250,y=10)

# configurando frame_corpo

l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 14"))
l_cidade.place(x=10,y=8)

l_data = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_data.place(x=10,y=54)

l_temp = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 30"))
l_temp.place(x=10,y=80)

l_temp_nome = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 30"))
l_temp_nome.place(x=65,y=80)

l_umidade = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 25"))
l_umidade.place(x=10,y=135)

l_umidade_simbolo = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10 bold"))
l_umidade_simbolo.place(x=50,y=140)

l_umidade_nome = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 8"))
l_umidade_nome.place(x=50,y=160)

l_pressao = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_pressao.place(x=10,y=190)

l_velocidade = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_velocidade.place(x=10,y=220)

l_descricao = Label(frame_corpo,text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_descricao.place(x=200,y=195)

janela.mainloop()