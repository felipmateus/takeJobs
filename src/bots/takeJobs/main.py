from takeJobs.items import TakejobsItem
from takeJobs.spiders.vagas import VagasComSpider
from scrapy.crawler import CrawlerProcess




def start_spider():
    process = CrawlerProcess()
    process.crawl(VagasComSpider)
    process.start()
    

if __name__ == "__main__":
    start_spider()