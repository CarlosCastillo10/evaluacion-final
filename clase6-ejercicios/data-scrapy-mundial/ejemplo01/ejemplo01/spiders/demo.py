import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "mundial"

    def start_requests(self):
        """
        urls = [
            'http://quotes.toscrape.com/page/2/',
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
        filename = "data/salida.csv"
        with codecs.open(filename, 'a', encoding='utf-8') as f:
            lista = response.xpath('//div[@class="fi-teams-list"]/div/a[@class="fi-team-card fi-team-card__team"]')
            for l in lista:
                url = l.xpath('@href').extract()[0]
                pais = l.xpath('div[@class="fi-team-card__info"]/div/text()')\
                        .extract()[0].strip()
                f.write(u"%s|%s\n" % (url,pais))
        self.log('Saved file %s' % filename)
