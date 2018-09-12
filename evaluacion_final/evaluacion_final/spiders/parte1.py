import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "datos_prefectos"

    def start_requests(self):
        """
        url = [
            'https://es.wikipedia.org/wiki/Anexo:Resultados_de_las_elecciones_seccionales_de_Ecuador_de_2014',
        ]
        """
        archivo = open("data/url.csv", "r")
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
            @reroes
        """
        filename = ("data/prefectos.csv")
        urls = ("data/urls_prefectos.csv")
        urls = codecs.open(urls, 'a', encoding='utf-8')
        #filename = codecs.open(filename, 'w', encoding='utf-8')
        

        with codecs.open(filename, 'a', encoding='utf-8') as f:
            f.write('%s|%s|%s|%s|%s\n'%('Nombre','Provincia','Partido','FechaInicio','FechaFin'))
            tablas = response.xpath('//table[@class="wikitable sortable"]')
            tr = tablas.xpath('tbody/tr')
            for l in tr:
                lista = l.xpath('td')
                if len(lista) > 0:
                    nombre = lista[2].xpath('a/text()').extract()
                    if len(nombre) > 0:
                        nombre = lista[2].xpath('a/text()').extract()[0].strip('\n')
                    else:
                        nombre = lista[2].xpath('text()').extract()[0].strip('\n')
                    provincia = lista[3].xpath('a/text()').extract()[0]
                    enlace = lista[4].xpath('a/@href')
                    if len(enlace) > 0:
                        enlace = lista[4].xpath('a/@href').extract()[0]
                        urls.write('https://es.wikipedia.org%s\n'%enlace)
                    
                    partido = lista[5].xpath('a/text()').extract()[0]
                    fechas = lista[6].xpath('a')
                    if len(fechas) > 0:
                        if len(fechas) == 1:
                            inicio = 2009
                        else:
                            inicio = fechas[1].xpath('text()').extract()[0]
                    fin = 2019
                    
                    
                    f.write(u"%s|%s|%s|%s|%s\n" % (nombre,provincia.rstrip('\n'),partido,inicio,fin))
            #filename.close()
        urls.close()
        self.log('Saved file %s' % filename)
        


    

           