import scrapy
from takeJobs.items import TakejobsItem
from scrapy.crawler import CrawlerProcess

class VagasComSpider(scrapy.Spider):
    name = "vagas"

    def start_requests(self):
        yield scrapy.Request(f"https://www.vagas.com.br/vagas-de-{self.search}?")

    def parse(self, response):
        vagas = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "vaga", " " ))]')

        vaga_item = TakejobsItem()

        for vaga in vagas:
            vaga_item['title'] = str(vaga.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "link-detalhes-vaga", " " ))]//@title').get())
            vaga_item['description'] = str(vaga.xpath(".//p//text()").get().strip())
            vaga_item['local'] = str(vaga.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "vaga-local", " " ))]//text()[2]').get())
            vaga_item['date'] = str(vaga.xpath('.//span[@class="data-publicacao"]//text()').get())
            vaga_item['site'] = "Vagas.com"
            vaga_item['link'] = "https://www.vagas.com.br" + str(vaga.xpath('.//a[@class="link-detalhes-vaga"]//@href').get())

            yield vaga_item    



        next_page = response.xpath('//a[@id="maisVagas"]//@data-url').get()
        url = "https://www.vagas.com.br" + str(next_page)
        print(f"NEXT PAGE: ", {url})
        if next_page:
            yield response.follow(url, callback=self.parse)
