"""
    Autores:
            Carlos Castillo
            Enrique Cueva
"""
import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "datos_prefectos"

    def start_requests(self):
        
        archivo = open("data/url.csv", "r") #Lee la direccion principal y lo guarda en 'archivo'.
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        filename = ("data/prefectos.csv") #Crea un archivo csv llamado 'prefectos'
        urls = ("data/urls_prefectos.csv")#Crea un archivo csv llamado 'urls_prefectos' que guardara todas los enlaces de cada provincia.
        urls = codecs.open(urls, 'a', encoding='utf-8')
        #filename = codecs.open(filename, 'w', encoding='utf-8')
        

        with codecs.open(filename, 'a', encoding='utf-8') as f:
            f.write('%s|%s|%s|%s|%s\n'%('Nombre','Provincia','Partido','FechaInicio','FechaFin')) #Encabezado del archivo csv
            tablas = response.xpath('//table[@class="wikitable sortable"]') #Response que permite obtener todas las 'table'
            tr = tablas.xpath('tbody/tr') #xpath que permite obtener todos los 'tr'.
            for l in tr:
                lista = l.xpath('td') #xpath que permite obtener todos los 'td'
                
                if len(lista) > 0: #Compara si la lista no esta vacia
                    nombre = lista[2].xpath('a/text()').extract() #Extrae el nombre que esta dentro de los 'a'.
                    
                    if len(nombre) > 0: #Compara si la lista no esta vacia
                        nombre = lista[2].xpath('a/text()').extract()[0].strip('\n') # Si no esta vacia extrae lo que contenga el 'a'.
                    else:
                        nombre = lista[2].xpath('text()').extract()[0].strip('\n') #Si esta vacia extrae directamente lo que tiene el 'td'.
                    
                    provincia = lista[3].xpath('a/text()').extract()[0] #Extrae directamente lo que contiene el 'a'
                    enlace = lista[4].xpath('a/@href') #Extrae el href que contiene el 'a'
                    
                    if len(enlace) > 0:
                        enlace = lista[4].xpath('a/@href').extract()[0] #Si la lista 'enlace' no esta vacia, extrae directamente el @href
                        urls.write('https://es.wikipedia.org%s\n'%enlace)# Guarda en el archivo urls el enlace de cada provincia.
                    
                    partido = lista[5].xpath('a/text()').extract()[0] #Extrae directamente lo que contiene el 'a'
                    fechas = lista[6].xpath('a') #Extrae todos los 'a'
                    
                    if len(fechas) > 0:
                        if len(fechas) == 1: #Si la lista no esta vacia y el tamaño de la lista es == 1 significa que tiene una fecha completa y establece el año en 2000
                            inicio = 2009
                        else:
                            inicio = fechas[1].xpath('text()').extract()[0] #Si no saca directamente el año
                    fin = 2019 #El año de fin siempre sera 2019.
                    
                    
                    f.write(u"%s|%s|%s|%s|%s\n" % (nombre,provincia,partido,inicio,fin)) #Guarda en el archivo 'prefectos' todos los datos.
            #filename.close()
        urls.close() #Cierra el archivo 'urls'
        self.log('Saved file %s' % filename)
        


    

           