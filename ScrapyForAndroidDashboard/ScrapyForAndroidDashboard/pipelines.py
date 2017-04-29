# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# ---
# title: hello,hikyson
# tags: [Default]
# category: [Default]
# comments: true
# date: 2014-04-20 22:18:43
# ---
#
# hello,hikyson
#
# <!-- more -->
#
# |Version|Codename|API|Distribution|
# |---|---|---|---|
# |111|222|333|444|
import os

from ScrapyForAndroidDashboard.git_pusher import post_title, local_time_str, post_name, push, post_file_dir


class ScrapyforandroiddashboardPipeline(object):
    def process_item(self, item, spider):
        # generate md file
        divider = "---"
        line_feed = "\r\n"
        title = post_title
        tags = "[android,spider,scrapy]"
        category = "[scrapy]"
        comments = "true"
        date = local_time_str
        more = "<!-- more -->"
        head = "".join(
            [divider, line_feed, "title: ", title, line_feed, "tags: ", tags, line_feed, "category: ", category,
             line_feed, "comments: ", comments, line_feed, "date: ", date, line_feed, divider, line_feed])
        summary = "This is a post generate by a spider , grab from url: [developer.android.google.cn](developer.android.google.cn)"
        updatetime = "Update time: %s" % local_time_str
        version_data_dict = json.loads(item["version_data"])
        version_chart_url = "https:" + version_data_dict["chart"] + ".png"
        # version text
        text_version = "".join(
            ["![version_chart](%s)" % version_chart_url, line_feed, line_feed, "|Codename|API|Distribution|",
             line_feed, "|---|---|---|", line_feed])
        version_items = version_data_dict["data"]
        for version_item in version_items:
            api = version_item["api"]
            name = version_item["name"]
            perc = version_item["perc"]
            text_version = text_version + "|" + str(api) + "|" + name + "|" + str(perc) + "|" + line_feed

        post = "".join(
            [head, line_feed, line_feed, summary, line_feed, updatetime, line_feed, line_feed, more, line_feed,
             line_feed, text_version])
        for file_name in os.listdir(post_file_dir):
            if file_name.find(post_title) >= 0:
                os.remove(os.path.join(post_file_dir, file_name))
        file_name = os.path.join(post_file_dir, post_name)
        with open(file_name, 'wb') as f:
            f.write(post)
        push()
        return item
