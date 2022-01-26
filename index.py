from colorama import init,Fore
import os,shutil
from link import cr_link
init()
if len(os.listdir('./unknown/index2')) != 0:
    for n in os.listdir('./unknown/index2'):
        os.remove('./unknown/index2/'+n)
def symbols(x=list(),end=True,color='LIGHTYELLOW_EX',textt=str()):
    try:
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
    except Exception as e:
        print(e)
        exit()
symbols([0,1],False,'LIGHTMAGENTA_EX',' [ options section ]'),symbols([2,3],True,'green',' [1]'),symbols(end=True,color='LIGHTcyan_EX',textt=' Exit'),symbols([11,2,3],True,'green',' [2]'),symbols(end=False,color='LIGHTcyan_EX',textt=' Audio player page'),symbols([2,3],True,'lightgreen_ex',' Enter a number >>> ')
num = input()
if not str(num).isdigit():
    while not str(num).isdigit():
        symbols([2,3],True,'lightgreen_ex',' Enter a number >>> ')
        num = input()
    symbols([2,4],True,'magenta',' [+]'),symbols(end=False,color='cyan',textt=' Done')
else:
    symbols([2,4],True,'magenta',' [+]'),symbols(end=False,color='cyan',textt=' Done')
num = int(num)
if num == 1:
    symbols([4,10,10,10,10,10,10],False,'lightmagenta_ex',' Bye')
    exit()
elif num == 2:
    try:
        from pyngrok import conf
    except ImportError:
        symbols([3,1],False,'LIGHTmagenta_EX',' [ install lib ]')
        from subprocess import getoutput
        x = getoutput('pip install pyngrok')
        if 'Successfully installed pyngrok' in x:
            symbols([2,4],True,'magenta',' [+]'),symbols(end=False,color='cyan',textt=' Successfully installed')
        else:
            symbols([2,4],True,'lightred_ex','[-]'),symbols(end=True,color='lightmagenta_ex',textt='Library not installed'),symbols(x=[11,3],end=True,color='lightcyan_ex',textt=' Please install pyngrok manually and then press Enter.')
            input()
            try:
                from pyngrok import conf
            except ImportError:
                symbols([4],False,'lightred_ex','The library is not installed properly')
                exit()
    symbols([3,1],False,'lightmagenta_ex',' [ Enter a .mp3 Path or link ]'),symbols([3,7,10],False,'cyan',' Example :'),symbols([2,3],False,'lightgreen_ex',' /home/unknown/Desktop/music.mp3'),symbols([2,3],False,'lightgreen_ex',' https://...../.../music.mp3'),symbols([2,3],True,'lightgreen_ex',' Enter a Path or Link : ')
    path_link = input()
    if len(path_link) == 0:
        while len(path_link) == 0:
            symbols([2,3],True,'lightgreen_ex',' Enter a Path or Link : ')
            path_link = input()
        symbols([2,4],True,'lightmagenta_ex',' [+]'),symbols(end=False,color='cyan',textt=' Done')
    else:
        symbols([2,4],True,'lightmagenta_ex',' [+]'),symbols(end=False,color='cyan',textt=' Done')

    symbols([3,10,1],False,'lightmagenta_ex',' [ Configuration section ]'),symbols([2,12,3,1],True,'lightgreen_ex',' Enter Your Ngrok Token (if you have not Token enter the D) : ')
    token = input()
    if len(token) == 0:
        symbols([2,12,2,4],False,'red',' !'),symbols([2,12,4],False,'red',' !'),symbols([4],False,'Lightcyan_ex',' Bye')
        exit()
    elif token == 'D':
        try:
            symbols([2,12,2,4],True,'lightmagenta_ex',' [+]'),symbols(end=False,color='cyan',textt=' Done')
        except Exception as e:
            symbols([2,12,2,4],True,'red',' [!] '),symbols(end=False,color='cyan',textt=str(e)),symbols([2,12,4],False,'red',' !'),symbols([4],False,'red',' !')
            exit()
    else:
        try:
            conf.get_default().auth_token = token
            symbols([2,12,2,4],True,'lightmagenta_ex',' [+]'),symbols(end=False,color='cyan',textt=' Done')
        except Exception as e:
            symbols([2,12,2,4],True,'red',' [!] '),symbols(end=False,color='cyan',textt=str(e)),symbols([2,12,4],False,'red',' !'),symbols([4],False,'red',' !')
            exit()
    symbols([2,12,3,1],False,'lightmagenta_ex',' [ Port section ]'),symbols([2,12,2,4],True,'lightgreen_ex',' Enter a port : ')
    port = input()
    while not port.isdigit():
        symbols([2,12,3,1],False),symbols([2,12,2,4],True,'lightgreen_ex',' Enter a port : ')
        port = input()
    symbols([2,12,4],True,'lightmagenta_ex',' [+]'),symbols(end=False,color='cyan',textt=' Done')
    with open('./unknown/index/iRLords.js') as UN:
        x = UN.read()
    with open('./unknown/index2/iRLords.js','w') as UN2:
        UN2.write(str(x.replace('@IRLORDS',str(path_link))))
    l = os.listdir('./unknown/index/')
    l.remove('iRLords.js')
    for i in l:
        shutil.copyfile(f'./unknown/index/{i}',f'./unknown/index2/{i}')
    cr_link(int(port))
else:
    symbols([4,10],True,'magenta',' [!] '),symbols(end=False,color='lightgreen_ex',textt='Wrong')