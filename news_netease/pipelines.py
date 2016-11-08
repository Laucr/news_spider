# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
import pymongo

reload(sys)
sys.setdefaultencoding("utf-8")


# file version
class FilePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        context = item['context']
        file_dir = 'NetEaseNews'
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        if context is not '':
            with open(file_dir + '/' + title, 'w') as f:
                f.write(context)
                f.close()
        return item


# db version
class MongoPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['netease']
        self.collection = self.db['news']

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item
