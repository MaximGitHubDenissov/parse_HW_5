import scrapy


class YahooScrapSpider(scrapy.Spider):
    name = "yahoo_scrap"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/most-active/"]

    def parse(self, response):
       rows = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr')
       for row in rows:
           symbol = row.xpath('.//td[1]/a/text()').get()
           name = row.xpath('.//td[2]/text()').get()
           price = row.xpath('.//td[3]/fin-streamer/text()').get()
           change = row.xpath('.//td[4]/fin-streamer/span/text()').get()
           change_proc = row.xpath('.//td[5]/fin-streamer/span/text()').get()
           volume = row.xpath('.//td[6]/fin-streamer/text()').get()

           yield {
               'Symbol': symbol,
               'Name': name,
               'Price': price,
               'Change': change,
               'Change_proc': change_proc,
               'Volume': volume
           }

           
           
