# -*- coding: utf-8 -*-

import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class AqicrawlerPipeline(object):
    def __init__(self):
        self.f = open("aqi.json", "w")

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False).encode("utf-8") + '\n'
        self.f.write(data)
        return item

    def spider_closed(self, spider):
        self.f.close()

