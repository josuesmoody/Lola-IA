import random

HelloList = ['hola','Hola','bienvenido','hey','namaste']
HelloReplyList = ['Hola Josué','Bienvenido Josue','Bienvenido','Hola Josue, que puedo hacer por ti?','Hola qué tal','Hola']

ByeList = ['Adios','salir']
ByeReplyList = ['Adios Josue','Hasta luego', 'Hasta luego Josue, que tengas un buen dia']

HowList = ['como estas','estas bien']
HowReplyList = ["Estoy bien","Me siento muy bien"]

def ReplyToQuery(Text):

    Query = str(Text).lower()
    Query = Query.replace(" Lola","")
    Query = Query.replace("Lola ","")

    if Query in HelloList:
        Ans = random.choice(HelloReplyList)
        return Ans

    elif Query in ByeList:
        Ans = random.choice(ByeList)
        return Ans

    elif Query in HowList:
        Ans = random.choice(HowReplyList)
        return Ans
