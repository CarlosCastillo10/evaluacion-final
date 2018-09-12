"""
    Autores:
            Carlos Castillo
            Enrique Cueva
"""

import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "datos_prefectos2"

    def start_requests(self):
        
        archivo = open("data/urls2.csv", "r") #Lee cada url de cada provincia que contienen listas y lo guarda en 'archivo'.
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):   

        with codecs.open("data/prefectos.csv", 'a', encoding='utf-8') as f:  #Abre directamente el archivo guardado en el primer spider.
           
            tablas = response.xpath('//table[@class="toc"]') #Response que permite obtener todas las 'table'
            tr = tablas.xpath('tbody/tr')#xpath que permite obtener todos los 'tr'.
            for x in tr:
                lista_td = x.xpath('td/a') #Obtiene todos los 'a' dentro de los 'td'
                lista_th = x.xpath('th') #Extrae todos los 'th'
                
                #Extrae la cabecera de los enlaces y reemplaza 'Anexo:Prefecto de' por un espacio blanco y lo limpia    
                provincia = response.css('.firstHeading ::text').extract_first().replace('Anexo:Prefectos de',"").strip(' ')
                partido = 'No contiene' #No hay ninguna informacion de los partidos a los que pertencen.
                
                if len(lista_th) > 0:
                    periodo = lista_th[0].xpath('text()').extract()[0] #Extrae directamente lo que contienen los 'th'
                    inicio = periodo[0:7].replace('1974 -','1970').strip(' -') #Guarda los primeros 6 elementos de la cadena porque se presenta en formato (1978 - 2014), le hace un replace y limpia los guiones
                    inicio = inicio.strip('\n') #Limpia los saltos de linea
                    fin = periodo[7:].replace('?','Actualidad').strip('\n') #Guarda los caracteres restantes.
                    
                    if inicio == '? - ?':
                        inicio = 1970 #Si inicio tiene el formato '? - ?' lo reemplaza por un año estatico.
                    
                    elif inicio == '? - 197':
                        inicio = 1997 #Si inicio tiene el formato '? - 197' lo reemplaza por un año estatico.
                        fin = 'Actualidad' #Valor que toma fin
                    
                    if fin == '':
                        fin = 'Actualidad' #Si el año final esta vacio le da por defecto 'Actualidad'
                
                if len(lista_td) > 0:
                    nombre = lista_td[0].xpath('text()').extract()[0] #Extrae directamente lo que contienen los 'td'
                
                    
                    f.write(u"%s|%s|%s|%s|%s\n" % (nombre,provincia,partido,inicio,fin)) #Guarda la informacion.
        f.close() #Cierra el archivo

        



        


    

           