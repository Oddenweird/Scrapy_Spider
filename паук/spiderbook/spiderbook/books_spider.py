import scrapy
import json

class BooksSpider(scrapy.Spider):
    name = 'books_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
   
    def parse(self, response):
        # Извлечение названий книг на текущей странице
        book_titles = response.xpath('//h3/a/@title').getall()
        
        for title in book_titles:
            yield {'title': title}
            print(title)

      
        # Пагинация: проверяем наличие следующей страницы
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
