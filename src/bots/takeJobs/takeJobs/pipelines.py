# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



# from mysql import mysql.connector

import mysql.connector

# 'host.docker.internal'

class TakejobsPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'lala102030',
            database = 'teste'
        )

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
        date_extracted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):

        #Check if item already exists
        self.cur.execute(""" select * from scrapy_vagas where title = %s """, (item["title"],))
        result = self.cur.fetchall()

        if result:
            #Dont insert
            pass
        else:
            ##Define insert statament & Insert item
            self.cur.execute(""" insert into scrapy_vagas (title, description, local, date, site) values (%s,%s,%s,%s,%s) """, (
                str(item["title"]),
                str(item["description"]),
                str(item["local"]),
                str(item["date"]),
                str(item["site"])
            ))

            self.conn.commit()
        return item

    def close_spider(self, spider):

        #Close cursor and connection to database
        self.cur.close()
        self.conn.close()

# class takejobsPipeline(db.Model):
#     def __init__():
#         pass