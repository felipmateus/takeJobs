# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

import websockets
import asyncio
import json

# from mysql import mysql.connector

import mysql.connector

# 'host.docker.internal'

class TakejobsPipeline:

    
    def __init__(self, server_url):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'lala102030',
            database = 'teste'
        )
        self.server_url = server_url
        #create cursor, used to exewcute commands
        self.cur = self.conn.cursor()
        # create a table id none exist
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS scrapy_vagas(
        id int NOT NULL auto_increment,
        title VARCHAR(255),
        description VARCHAR(500),
        local VARCHAR(255),
        date VARCHAR(255),
        site VARCHAR(255),
        link VARCHAR(255),
        date_extracted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
        )
        """)

        self.processed_titles = set()  # Conjunto para armazenar títulos já processados

    @classmethod
    def from_crawler(cls, crawler):
        server_url = crawler.settings.get('WEBSOCKET_SERVER_URL')
        return cls(server_url)

    def open_spider(self, spider):
        asyncio.get_event_loop().run_until_complete(self.connect())

    async def connect(self):
        self.websocket = await websockets.connect(self.server_url)
    

    
    async def process_item(self, item, spider):

        title = item["title"]

        if title in self.processed_titles:
            # Item já foi processado, ignorar
            return item


        #Check if item already exists
        self.cur.execute(""" select * from scrapy_vagas where title = %s """, (item["title"],))
        result = self.cur.fetchall()


        self.processed_titles.add(title)

        # Enviar item para o WebSocket
        await self.websocket.send(json.dumps(dict(item)))


        if result:
            #Dont insert
            pass
        else:
            ##Define insert statament & Insert item
            self.cur.execute(""" insert into scrapy_vagas (title, description, local, date, site, link) values (%s,%s,%s,%s,%s,%s) """, (
                str(item["title"]),
                str(item["description"]),
                str(item["local"]),
                str(item["date"]),
                str(item["site"]),
                str(item["link"])
            ))

            self.conn.commit()

            # await self.websocket.send(json.dumps(dict(item)))  # Modify as per your item structure
                
        return item

    def close_spider(self, spider):

        #Close cursor and connection to database
        self.cur.close()
        self.conn.close()
        asyncio.get_event_loop().run_until_complete(self.websocket.close()) # Fechar conexão com o WebSocket