# -*- coding: utf-8 -*-
import re

import scrapy

from ScrapyForAndroidDashboard.items import ScrapyforandroiddashboardItem


class DeveloperAndroidSpider(scrapy.Spider):
    name = "developer.android"
    allowed_domains = ["developer.android.com"]
    start_urls = ['https://developer.android.google.cn/about/dashboards/index.html']

    def find_data_by_re(self, data_strs, re_str):
        for data_text in data_strs:
            data_text = data_text.replace(" ", "").replace("\t", "").replace("\r\n", "").replace("\n", "").strip()
            data_match_groups = re.search(re_str, data_text)
            if data_match_groups and data_match_groups.group(1):
                return data_match_groups.group(1)
        return ""

    def parse(self, response):
        # obtain js codes,because verison,screen and opengl data in it.
        js_texts = response.xpath("//script/text()").extract()

        screen_data_json_str = self.find_data_by_re(js_texts, r"varSCREEN_DATA=\[(.*?)\];")
        version_data_json_str = self.find_data_by_re(js_texts, r"varVERSION_DATA=\[(.*?)\];")
        version_names_json_str = self.find_data_by_re(js_texts, r"varVERSION_NAMES=\[(.*?)\];")

        print ">>> screen_data_json_str  %s" % screen_data_json_str
        print ">>> version_data_json_str  %s" % version_data_json_str
        print ">>> version_names_json_str  %s" % version_names_json_str

        item = ScrapyforandroiddashboardItem()
        item["version_data"] = version_data_json_str
        item["version_names"] = version_names_json_str
        item["screen_data"] = screen_data_json_str
        yield item


        # print "kkkkkkkkkkkkkkkkkkkkk -> %d"%len(chart_list_selectors)
        # for chat_selector in chart_list_selectors:
        #     version_items_selectors = chat_selector.xpath("//tbody/tr")
        #     for index,version_items_selector in enumerate(version_items_selectors):
        #         if index == 0:
        #             continue
        #         print version_items_selector.xpath("/td").extract()
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
