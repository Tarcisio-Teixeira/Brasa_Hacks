#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 07:59:02 2020

@author: tarcisio.soares-teixeira-neto
"""
import random, math, time
#####################Client Class#########################
LISTA_DE_BONUS = ["10% de desconto na proxima compra", "5% de desconto na proxima compra", "um pack de cerveja gratis"] 
class Client():
    def __init__ (self, Name ,x ,y, estoque):
        self.Name = Name
        self.estoque = estoque
        self.locx = x
        self.locy = y
    def recebimeto(self, carregamento):
        for (k,v) in carregamento.items():
            if k not in self.estoque.keys():
                self.estoque[k] = v
            else:
                self.estoque[k] += v
    def __str__(self):
        s = "Cliente " + self.Name + "\n"
        return s

#####################Client Class########################
class Client_Premium(Client):
    def __init__(self, Name ,x ,y , estoque, bonus):
        self.bonus = bonus if bonus != [] else []
        self.Name = Name
        self.estoque = estoque if estoque != {} else {}
        self.locx = x
        self.locy = y
    def recebimeto(self, carregamento):
        for (k,v) in carregamento.items():
            if k not in self.estoque.keys():
                self.estoque[k] = v
            else:
                self.estoque[k] += v
    def venda(self, carregamento):
        for (k,v) in carregamento.items():
            self.estoque[k] -= v
        self.bonus.append(random.choice(LISTA_DE_BONUS))
        
    def venda_request(self, carregamento):
        for (k,v) in carregamento.items():
            if self.estoque[k] < v:
                return 0
        return random.choice([0,1])
    def __str__(self):
        s = "Cliente Premium " + self.Name + "\n"
        s+= "Seu estoque e:\n"
        for (k,v) in estoque.items():
            s += k + ": " + str(v) + "\n"
        if self.bonus == []:
            s += "Voce nao tem bonus acumulados\n"
            return s
        s+= "Seus bonus sao: \n"
        for i in self.bonus:
            s+= i + "\n"
        return s

#####################EA Class########################
class EA():
    def __init__ (self, x, y, limites , estoque):
        self.estoque = estoque if estoque != {} else {}
        self.limites = limites
        self.locx = x
        self.locy = y
    def venda(self, carregamento):
        for (k,v) in carregamento.items():
            self.estoque[k] -= v
    def venda_request(self, carregamento):
        for (k,v) in carregamento.items():
            if self.limites[k] < v:
                return 0
        return 1
    
#####################Pit-Stop Class######################## 
class Pit_Stop():
    def __init__ (self, x, y, limites , estoque, endereco):
        self.endereco = endereco
        self.estoque = estoque if estoque != {} else {}
        self.limites = limites
        self.locx = x
        self.locy = y
    def venda(self, carregamento):
        for (k,v) in carregamento.items():
            self.estoque[k] -= v
    def venda_request(self, carregamento):
        for (k,v) in carregamento.items():
            if self.limites[k] < v:
                return 0
        return 1
    
####################################################
r = list(range(5))
s = list(range(5))
beers = ['skol','stella', 'brahma', 'corona','budwiser','antartica']

EA_dist_max = 0.75
random.shuffle(r)
random.shuffle(s)
EA_limites = {i: 5 for i in beers}
EA_estoque = {i:20 for i in beers}
EAS = [EA(i,j, EA_limites, EA_estoque) for i in r[:3] for j in s[:3]]

ED_dist_max = 0.5
random.shuffle(r)
random.shuffle(s)
ED_estoque = {i: random.choice(list(range(40))) for i in beers}
EDS = [Client_Premium("Bot", i,j, ED_estoque, []) for i in r[:3] for j in s[:3]]

PS_dist_max = 2
random.shuffle(r)
random.shuffle(s)
PS_limites = {i: 5 for i in beers}
PS_estoque = {i: 20 for i in beers}
PSS = [Pit_Stop(i,j, PS_limites, PS_estoque, "rua aleatoria {}".format(random.randint(0,30))) for i in r[:3] for j in s[:3]]

print("Bem vindo ao beer network")
print("Criar conta")
#user_name =  input("Nome de Usuario: \n"Cliente premium)
#pasword = input("Senha: \n")
Name = input("Escolha nome de Usuario: \n")

Local = input("Endereco do estabelecimento: \n")

while(True):
    
    mode = input("Escolha um modo, Cliente Premium ou Cliente Normal \n")
    #mode = "Cliente normal"
    if mode.strip() == "Cliente premium" or mode.strip() == "Cliente Premium" or mode.strip() == "cliente premium" or mode.strip() == "cliente Premium":
        print("\n - Vamos atualizar seu estoque \n")
        time.sleep(0.3)
        cond = True
        while(cond == True):
            estoque = {}
            estoque['skol'] = int(input("Quantas cervejas skol: "))
            estoque['stella'] = int(input("Quantas cervejas stella: "))
            estoque['brahma'] = int(input("Quantas cervejas brahma: "))
            estoque['corona'] = int(input("Quantas cervejas corona: "))
            estoque['budwiser'] = int(input("Quantas cervejas budwiser: "))
            estoque['antartica'] = int(input("Quantas cervejas antartica: "))
            time.sleep(0.3)
            print("\n -Por Favor, confirme seu estoque: \n")
            for (k,v) in estoque.items():
                time.sleep(0.1)
                print(k + ": " + str(v))
            time.sleep(1)
            confirma = input("\n -Seu estoque estar certo [S/N]? \n")
            if confirma == "S"or confirma == "s" or confirma == "sim":
                cond = False
        break
    elif mode.strip() == "Cliente normal" or mode.strip() == "Cliente Normal" or mode.strip() == "cliente normal" or mode.strip() == "cliente Normal":
        break
    else:
        time.sleep(0.5)
        print("Modo invalido!! digite Cliente Premium ou Cliente Normal.\n")
print("\n")
time.sleep(0.2)
print("Bem vindo ao breja network!\n")

if mode.strip() == "Cliente premium" or mode.strip() == "Cliente Premium" or mode.strip() == "cliente premium" or mode.strip() == "cliente Premium":
    cliente = Client_Premium(Name,2 ,3, estoque, [])
    first_time = True
    while(True):
        if not first_time:
            cond_demand = random.choice([True, False, False, False, False])
            if cond_demand:
                carregamento = {b:random.randint(0,5) for b in beers }
                print("\n -Voce tem um pedido novo!\n")
                print("\nPedido:\n")
                print("\n skol: {}\n".format(carregamento['skol']))
                print("\n stella: {}\n".format(carregamento['stella']))
                print("\n brahma: {}\n".format(carregamento['brahma']))
                print("\n corona: {}\n".format(carregamento['corona']))
                print("\n budwiser: {}\n".format(carregamento['budwiser']))
                print("\n antartica: {}\n".format(carregamento['antartica']))
                vai_entregar = input("\n -Seu estoque esta disponivel para fazer essa entrega [S/N]?\n")
                if vai_entregar == "S" or vai_entregar == "s":
                    print("\n.......Checando transporte.......\n")
                    time.sleep(0.5)
                    print("\n -logo logo, nosso motorista ira recolher esse carregamento\n")
                    print("\n -muito obrigado por contribur com a ambev\n")
                    cliente.venda(carregamento)
        first_time = False     
        acao = input("\n -Digite P para fazer um novo pedido, I para ver suas informacoes e D para sair do app\n")
        
        if acao == "D":
            break
        elif acao == "P":
            print("\n -Vamos anotar seu pedido \n")
            cond = True
            while(cond == True):
                carregamento = {}
                carregamento['skol'] = int(input("Quantas cervejas skol: "))
                carregamento['stella'] = int(input("Quantas cervejas stella: "))
                carregamento['brahma'] = int(input("Quantas cervejas brahma: "))
                carregamento['corona'] = int(input("Quantas cervejas corona: "))
                carregamento['budwiser'] = int(input("Quantas cervejas budwiser: "))
                carregamento['antartica'] = int(input("Quantas cervejas antartica: "))
                print("\n -Vamos confirmar seu pedido: \n")
                for (k,v) in carregamento.items():
                    print(k + ": " + str(v))
                confirma = input("\n -Seu pedido estar certo [S/N]? \n")
                if confirma == "S"or confirma == "s" or confirma == "sim":
                    cond = False
            print("-Pedido anotado, em instantes entraremos em contato para dar atualizacao sobre o pedido")
            print("........running algorithm........" )
            time.sleep(1)
            print("........checando EA nas proximidades.....")
            EA_found = 0
            for EA in EAS:
                if math.sqrt((cliente.locx - EA.locx)**2 + (cliente.locy - EA.locy)**2) < EA_dist_max :
                    EA_found = EA.venda_request(carregamento)
                if EA_found == 1:
                    EA_chosen = EA
                    break
            if EA_found == 1:
                entrega_cond = input("-Podemos fazer a entrega hoje, voce aceita receber hoje [S/N]?")
                if entrega_cond == "S" or entrega_cond == "s":
                    print("-logo logo, a entrega sera feita.")
                    EA_chosen.venda(carregamento)
                    cliente.recebimeto(carregamento)
                else:
                    print("-Seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
            elif EA_found == 0:
                time.sleep(1)
                print("........checando ED nas proximidades.....")
                ED_found = 0
                for ED in EDS:
                   # print((ED.locx, ED.locy))
                    if math.sqrt((cliente.locx - ED.locx)**2 + (cliente.locy - ED.locy)**2) < ED_dist_max :
                        ED_found = ED.venda_request(carregamento)
                    if ED_found == 1:
                        ED_chosen = ED
                        break
                if ED_found == 1:
                    entrega_cond = input("-Podemos fazer a entrega hoje, voce aceita receber hoje [S/N]?")
                    if entrega_cond == "S" or entrega_cond == "s":
                        print("-logo logo, a entrega sera feita.")
                        ED_chosen.venda(carregamento)
                        cliente.recebimeto(carregamento)
                    else:
                        print("-Seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
                elif ED_found == 0:
                    time.sleep(1)
                    print("........checando PS nas proximidades.....")
                    PS_found = 0
                    for PS in PSS:
                        if math.sqrt((cliente.locx - PS.locx)**2 + (cliente.locy - PS.locy)**2) < PS_dist_max :
                            PS_found = PS.venda_request(carregamento)
                        if PS_found == 1:
                            PS_chosen = PS
                            break
                    if PS_found == 1:
                        entrega_cond = input("-Infelizmente nao conseguiremos fazer sua entrega hoje, mas existe um PIT-STOP na localizacao {} em que voce pode fazer a retirada do pedido.Voce tem interesse [S/N]?".format(PS_chosen.endereco))
                        if entrega_cond == "S" or entrega_cond == "s":
                            print("-Seu pedido foi enviado para o PIT STOP, aguardando retirada")
                            PS_chosen.venda(carregamento)
                            cliente.recebimeto(carregamento)
                        else:
                            print("-Seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
                    else:
                        print("-Não vai ser possivel entregar no D+0, seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
        elif acao == "I":
            print(cliente)
        else:
            print("-Acao invalida!! tente novamente")
    
elif mode.strip() == "Cliente normal" or mode.strip() == "Cliente Normal" or mode.strip() == "cliente normal" or mode.strip() == "cliente Normal":
    cliente = Client(Name,2 ,3,{})
    while(True):
        acao = input("-Digite P para fazer um novo pedido, I para ver suas informacoes e D para sair do app")
        if acao == "D":
            break
        elif acao == "P":
            print("\n -Vamos anotar seu pedido \n")
            cond = True
            while(cond == True):
                carregamento = {}
                carregamento['skol'] = int(input("Quantas cervejas skol: "))
                carregamento['stella'] = int(input("Quantas cervejas stella: "))
                carregamento['brahma'] = int(input("Quantas cervejas brahma: "))
                carregamento['corona'] = int(input("Quantas cervejas corona: "))
                carregamento['budwiser'] = int(input("Quantas cervejas budwiser: "))
                carregamento['antartica'] = int(input("Quantas cervejas antartica: "))
                print("\n -Vamos confirmar seu pedido: \n")
                for (k,v) in carregamento.items():
                    print(k + ": " + str(v))
                confirma = input("\n -Seu pedido estar certo [S/N]? \n")
                if confirma == "S"or confirma == "s" or confirma == "sim":
                    cond = False
            print("-Pedido anotado, em instantes entraremos em contato para dar atualizacao sobre o pedido")
            print("........running algorithm........" )
            time.sleep(1)
            print("........checando EA nas proximidades.....")
            EA_found = 0
            for EA in EAS:
                if math.sqrt((cliente.locx - EA.locx)**2 + (cliente.locy - EA.locy)**2) < EA_dist_max :
                    EA_found = EA.venda_request(carregamento)
                if EA_found == 1:
                    EA_chosen = EA
                    break
            if EA_found == 1:
                entrega_cond = input("-Podemos fazer a entrega hoje, voce aceita receber hoje [S/N]?")
                if entrega_cond == "S" or entrega_cond == "s":
                    print("-logo logo, a entrega sera feita.")
                    EA_chosen.venda(carregamento)
                    cliente.recebimeto(carregamento)
                else:
                    print("-Seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha/n")
            elif EA_found == 0:
                time.sleep(1)
                print("........checando ED nas proximidades.....")
                ED_found = 0
                for ED in EDS:
                   # print((ED.locx, ED.locy))
                    if math.sqrt((cliente.locx - ED.locx)**2 + (cliente.locy - ED.locy)**2) < ED_dist_max :
                        ED_found = ED.venda_request(carregamento)
                    if ED_found == 1:
                        ED_chosen = ED
                        break
                if ED_found == 1:
                    entrega_cond = input("-Podemos fazer a entrega hoje, voce aceita receber hoje [S/N]?")
                    if entrega_cond == "S" or entrega_cond == "s":
                        print("-logo logo, a entrega sera feita.")
                        ED_chosen.venda(carregamento)
                        cliente.recebimeto(carregamento)
                    else:
                        print("-Seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
                elif ED_found == 0:
                    time.sleep(1)
                    print("........checando PS nas proximidades.....")
                    PS_found = 0
                    for PS in PSS:
                        if math.sqrt((cliente.locx - PS.locx)**2 + (cliente.locy - PS.locy)**2) < PS_dist_max :
                            PS_found = PS.venda_request(carregamento)
                        if PS_found == 1:
                            PS_chosen = PS
                            break
                    if PS_found == 1:
                        entrega_cond = input("-Infelizmente nao conseguiremos fazer sua entrega hoje, mas existe um PIT-STOP na localizacao {} em que voce pode fazer a retirada do pedido.Voce tem interesse [S/N]?".format(PS_chosen.endereco))
                        if entrega_cond == "S" or entrega_cond == "s":
                            print("-Seu pedido foi enviado para o PIT STOP, aguardando retirada")
                            PS_chosen.venda(carregamento)
                            cliente.recebimeto(carregamento)
                        else:
                            print("-Seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
                    else:
                        print("-Não vai ser possivel entregar no D+0, seu pedido foi encaminhado para o cdd e tem previsao de chegada para amanha")
                            
        elif acao == "I":
            print(cliente)
        else:
            print("-Acao invalida!! tente novamente")