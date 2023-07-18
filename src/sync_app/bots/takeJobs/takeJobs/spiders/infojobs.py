import scrapy
from takeJobs.items import TakejobsItem

class InfojobsSpider(scrapy.Spider):
    name = "infojobs"
    search = "Vendedor"
    next_page = 1

    def start_requests(self):
        yield scrapy.Request(f"https://www.infojobs.com.br/vagas-de-emprego-{self.search}.aspx?page={self.next_page}")

    def parse(self, response):
        vagas = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "js_cardLink", " " ))]')

        vaga_item = TakejobsItem()

        for vaga in vagas: 
            title = vaga.xpath('.//h2[@class="h3 font-weight-bold text-body mb-8"]//text()').get(),
            if title[0] is not None:
                vaga_item['title'] = title[0].strip()
            else:
                vaga_item['title'] = "Não encontrado"
            

            description = vaga.xpath('.//div[@class="small text-medium"]//text()').get(),
            if description[0] is not None:
                vaga_item['description'] = description[0].strip()
            else:
                vaga_item['description'] = "Não encontrado"


            local = vaga.xpath('.//div[@class="small text-medium mr-24"]//text()').get().strip(),
            if local[0] is not None:
                vaga_item['local'] = local[0].strip()
            else:
                vaga_item['local'] = "Não encontrado"


            date = vaga.xpath('.//div[@class="text-medium small"]//text()').get(),
            if date[0] is not None:
                vaga_item['date'] = date[0].strip()
            else:
                vaga_item['date'] = "Não encontrado"


            vaga_item['site'] = "Infojobs"

            yield vaga_item

        # last_page = response.xpath('//li[@class="page-item disabled"]').get()
        
        self.next_page += 1
        url = f'https://www.infojobs.com.br/vagas-de-emprego-vendedor.aspx?page={self.next_page}'
        print(f"NEXT PAGE: ", {url})
        yield response.follow(url, callback=self.parse)

        
        
