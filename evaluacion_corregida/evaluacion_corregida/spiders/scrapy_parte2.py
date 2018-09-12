"""
    Autores:
            Carlos Castillo
            Enrique Cueva
"""
import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "datos_prefectos1"

    def start_requests(self):
        
        archivo = open("data/urls1.csv", "r") #Lee cada url de cada provincia que contienen tablas y lo guarda en 'archivo'.
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        with codecs.open("data/prefectos.csv", 'a', encoding='utf-8') as f: #Abre directamente el archivo guardado en el anterior spider.
            #f.write('%s|%s|%s|%s|%s\n'%('Nombre','Provincia','Partido','FechaInicio','FechaFin'))
            tablas = response.xpath('//table[@class="wikitable"]') #Response que permite obtener todas las 'table'
            tr = tablas.xpath('tbody/tr')#xpath que permite obtener todos los 'tr'.
            
            for l in tr:
                lista = l.xpath('td') #xpath que permite obtener todos los 'td'
                
                if len(lista) > 0: #Compara si la lista no esta vacia
                    
                    if len(lista) == 5:
                        nombre = lista[1].xpath('a/text()') #Si el tamaño de la lista es igual a 5 entonces extrae directamente lo que contiene el {a}
                        
                        if len(nombre) > 0: 
                            nombre = lista[1].xpath('a/text()').extract()[0]#Si existe un 'a' extrae el texto
                        else:
                            nombre = lista[1].xpath('text()').extract()[0] #Caso contario extrae directamente lo que contiene el 'td'.

                        inicio = lista[2].xpath('text()').extract()[0].strip('\n') #Extrae directamente lo que contiene el 'td' y limpia el salto de liniea.
                        fin = lista[3].xpath('small/text()') #'Guarda lo que contiene el 'small
                        partido = 'No contiene' 
                        
                        if len(fin) > 0:
                            fin = lista[3].xpath('small/text()').extract()[0] #Si existe un 'small' extrae directamenre el texto.
                        else:
                            fin = lista[3].xpath('text()').extract()[0].strip('\n') #si no extrae lo que contiene el 'td'

                 
                    else:
                        nombre = lista[0].xpath('a/text()') #En caso de que el tamaño de la lista no sea igual a 5(Hay tablas de 4 y 3 columnas)
                        
                        if len(nombre) > 0:
                            nombre = lista[0].xpath('a/text()').extract()[0] ##si existe un 'a'  extrae su texto.
                        else:
                            nombre = lista[0].xpath('text()').extract()[0] #Si no extrae directamente lo que contiene el 'td'
                        
                        inicio = lista[1].xpath('a/text()')
                        
                        if len(inicio) > 0:
                            partido = lista[1].xpath('a/text()').extract()[0] #Si existe un 'a' entonces saca el partido al que pertenece
                            inicio = lista[2].xpath('text()').extract()[0].strip('\n') #Saca directamente lo que contiene el 'td'
                            fin = lista[3].xpath('text()').extract()[0].strip('\n') #Saca directamente lo que contiene el 'td' y limpia los saltos de linea
                            
                        else:
                            partido = 'No contiene' #Si no existe un 'a' entonces no contiene un partido
                            inicio = lista[1].xpath('text()').extract()[0].strip('\n') #Saca directamente lo que contiene el 'td' y limpia el salto de linea
                            fin = lista[2].xpath('i/text()') #Saca lo que contiene el 'i' en caso de que haya.
                            
                            if len(fin) > 0: 
                                fin = lista[2].xpath('i/text()').extract()[0]#Extrae lo que contiene el 'i' si es que hay alguno.
                            else:
                                fin = lista[2].xpath('text()').extract()[0].strip('\n') #Si no extrae directamente lo que contiene el 'td'
                    
                    provincia = response.css('.firstHeading ::text').extract_first().replace('Anexo:Prefectos de',"").strip(' ') #Extrae la cabecera de los enlaces y reemplaza 'Anexo:Prefecto de' por un espacio blanco y lo limpia    

                    f.write(u"%s|%s|%s|%s|%s\n" % (nombre,provincia,partido,inicio,fin)) #Guarda en el archivo 'prefectos' los datos.
        f.close()
                    
                          
        
        



    
