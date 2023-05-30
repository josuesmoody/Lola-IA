from Scripts.Hablar import Hablar
from Scripts.Escuchar import Escuchar
from Chats.Chats import ReplyToQuery
from Body.Brain import ActionToQuery

def EjecutarMain():

    while True:

        print("")
        print("------------------------------------------------")
        print("")

        Query = Escuchar()
        Query = str(Query).lower()

        RespuestaChat = ReplyToQuery(Query)
        RespuestaChat = str(RespuestaChat)

        if "None" in RespuestaChat:
            pass

        else:
            Hablar(RespuestaChat)

        EjecutarTarea = str(Query).lower()
        ActionToQuery(Query=EjecutarTarea)

        print("")

EjecutarMain()
