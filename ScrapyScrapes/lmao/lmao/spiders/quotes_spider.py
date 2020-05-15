import scrapy
class quotes_spider(scrapy.Spider):
    name = 'quotes'
    start_urls =[
        'http://quotes.toscrape.com/'
    ]
    def parse(self, response):
        title = response.css("author::text").extract()
        yield{
            'titletext' : title
        }