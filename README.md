<<<<<<< HEAD
# evaluacion-final

1. Hacer scrapy de la página https://es.wikipedia.org/wiki/Prefectos_provinciales_del_Ecuador

Generar un archivo con los siguientes datos:

Nombre|Provincia|Partido|AnioInicio|AnioFin

2.- Ingresar a cada enlace de la columna predecesor

Ejm.
https://es.wikipedia.org/wiki/Anexo:Prefectos_de_Azuay

y agregar datos al primer archivo

Nombre|Provincia|Partido|AnioInicio|AnioFin

3.- Leer el csv final generado y presentar los prefectos en base a la provincia.
- Usar un widget de ipython

4.- Subir todo al repositorio


AUTORES:
	Carlos Castillo
	Enrique Cueva

PROCEDIMIENTO:

cd evaluacion-final/evaluacion_final

1. Ejecturar: 
	scrapy crawl datos_prefectos
2. Ejecutar:
	scrapy crawl datos_prefectos1
3. Ejectutar:
	scrapy crwal datos_prefectos2
4. Levantar jupyter y ejecutar el notebook
=======
# pe-18-datos

## actualizar desde los forks
- git remote add upstream https://github.com/reroes/pe-18-datos
- git fetch  upstream
- git merge upstream/master
- git push

## sentencias scrapy

In [49]: l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--age"]/span[@class="fi-p__info--ageNum"]/text(
    ...: )').extract()[0]
Out[49]: u'31'

In [50]: l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--role"]/text()').extract()[0]
Out[50]: u'\r\nArquero              '

In [51]: l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__n"]/a/span/text()').extract()[0]
Out[51]: u'Franco ARMANI'

>>>>>>> upstream/master
