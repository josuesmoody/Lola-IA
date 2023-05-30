
WebList = ['visita','ejecuta']
OpenList = ['abre','empieza']
SearchList = ['busca', 'buscar', 'encuntra']
ListaReproducir = ['reproduce', 'pon']
ListaCaptura = ['Hacer captura', 'Captura', 'Screenshot']

from Funciones.Website import Websiter
from Funciones.open import Opener
from Funciones.search import Search
from Funciones.reproducir import Reproducir
from Funciones.Captura import Captura
from Scripts.Hablar import Hablar

def ActionToQuery(Query):
    Text = str(Query)
    Query = str(Query).split(" ")

    for words in Query:
        if words in WebList:
            Name = Text.replace('visita','')
            Name = Name.replace('ejecuta','')
            Name = Name.replace(' ','')
            Hablar(' Visitando... ' + Name)
            Websiter(Name=Name)

        elif words in OpenList:
            Name = Text.replace('abre',"")
            Name = Name.replace('empieza',"")
            Name = Name.replace(' ','')
            Hablar(' Abriendo... ' + Name)
            Opener(Name=Name)

        elif words in SearchList:
            Name = Text.replace('busca',"")
            Name = Text.replace('buscar',"")
            Name = Name.replace('encuentra',"")
            Name = Name.replace(' ','')
            Hablar(' Buscando... ' + Name)
            Search(Key=Name)
        
        elif words in ListaReproducir:
            Name = Text.replace('reproduce',"")
            Name = Name.replace('pon',"")
            Name = Name.replace(' ','')
            Hablar(' Reproduciendo... ' + Name)
            Reproducir(Key=Name)
        
        elif words in ListaCaptura:
            Name = Text.replace('Hacer captura',"")
            Name = Name.replace('pon',"")
            Name = Name.replace(' ','')
            Hablar(' Reproduciendo... ' + Name)
            Reproducir(Key=Name)
            
