import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "datos_paises"

    def start_requests(self):
        """
        urls = [
            'http://quotes.toscrape.com/page/2/',
        ]
        """
        archivo = open("data/salida.csv", "r")
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
            @reroes
        """
        filename = ("data/datos.csv")
        with codecs.open(filename, 'a', encoding='utf-8') as f:
            lista = response.xpath('//div[@class="fi-team__members"]/a/div[@class="fi-p"]')
            contador = 0
            for l in lista:
                nombre = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__n"]/a/span/text()').extract()[0]
                edad = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--age"]/span[@class="fi-p__info--ageNum"]/text()').extract()[0].strip() 
                pais = l.xpath('//div[@class="fi-t__n"]/span/text()').extract()[0].strip()
                rol = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--role"]/text()').extract()[0].strip()
                if(rol != 'Entrenador'):
                    numero = l.xpath('//div[@class="fi-p__info"]/div[@class="fi-p__jerseyNum "]/span/text()').extract()[contador].strip()
                else:
                    numero = 0
                f.write(u"%s|%s|%s|%s|%s\n" % (nombre,edad,rol,numero,pais))
                contador += 1
        self.log('Saved file %s' % filename)
        


           