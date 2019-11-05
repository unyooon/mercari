import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

class Mercari():

    def __init__(self, name):
        self.name = name
        #self.id = ing_name
        self.dir = './data/mercari/csv/{}.csv'.format(self.name)


    def get_informations(self):

        df = pd.read_csv('./data/mercari/csv/default.csv')
        browser.get("https://www.mercari.com/jp/search/?sort_order=price_desc&keyword={}&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=".format(self.name))
        page = 1

        while True:

            if len(browser.find_elements_by_css_selector("li.pager-next .pager-cell:nth-child(1) a")) > 0:
                print("######################page: {} ########################".format(page))
                print("Starting to get posts...")

                posts = browser.find_elements_by_css_selector(".items-box")


                for post in posts:
                    title = post.find_element_by_css_selector("h3.items-box-name").text


                    price = post.find_element_by_css_selector(".items-box-price").text
                    price = price.replace('¥¥', '')


                    sold = 0
                    if len(post.find_elements_by_css_selector(".item-sold-out-badge")) > 0:
                        sold = 1

                    url = post.find_element_by_css_selector("a").get_attribute("href")
                    se = pd.Series([title, price, sold,url],['title','price','sold','url'])
                    df = df.append(se, ignore_index=True)


                page+=1

                btn = browser.find_element_by_css_selector("li.pager-next .pager-cell:nth-child(1) a").get_attribute("href")
                print("next url:{}".format(btn))
                browser.get(btn)
                print("Moving to next page......")


            else:
                print("no pager exist anymore")
                break

        df.to_csv(self.dir)
        print("DONE")

    def main():

        args = sys.argv
        df = pd.read_csv('./data/mercari/csv/default.csv')



