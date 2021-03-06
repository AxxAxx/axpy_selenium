# -*- coding: utf-8 -*-

import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium import *
from selenium.webdriver.common.by import By

#
# DEFINE YOUR FUNCTIONS HERE...
#

def locklab(args):
    driver =  webdriver.Firefox()

    driver.get("https://lock-lab.com/free-drawing/")
    #driver.get("https://www.facebook.com/")
    #driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS)
    element_1 = driver.find_element_by_xpath('id("post-10532")/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_1.clear()
    element_1.send_keys("axel.johansson10@gmail.com")
    #element_2 = driver.find_element_by_name('lastname')
    #element_2.clear()
    #element_2.send_keys("Johansson")
    element_2 = driver.find_element_by_xpath('id("post-10532")/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_2.clear()
    element_2.send_keys("Axel Johansson")
    element_3 = driver.find_element_by_xpath('id("post-10532")/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/span[1]')
    element_3.click()
    print('Sucessfully entered LockLAb "YOUTUBE FAN APPRECIATION" Giveaway')
    
    
    driver.get("https://lock-lab.com/monday-fan-appreciation-free-giveaway/")
    element_1 = driver.find_element_by_xpath('id("post-11313")/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_1.clear()
    element_1.send_keys("axel.johansson10@gmail.com")
    element_2 = driver.find_element_by_xpath('id("post-11313")/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_2.clear()
    element_2.send_keys("Axel Johansson")
    element_3 = driver.find_element_by_xpath('id("post-11313")/div[1]/div[4]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/span[1]')
    element_3.click()
    print('Sucessfully entered LockLAb "MONDAY FAN APPRECIATION" Giveaway')
    
    driver.get("https://lock-lab.com/wednesday-fan-appreciation-free-giveaway/")
    element_1 = driver.find_element_by_xpath('id("post-11312")/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_1.clear()
    element_1.send_keys("axel.johansson10@gmail.com")
    element_2 = driver.find_element_by_xpath('id("post-11312")/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_2.clear()
    element_2.send_keys("Axel Johansson")
    element_3 = driver.find_element_by_xpath('id("post-11312")/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/span[1]')
    element_3.click()
    print('Sucessfully entered LockLAb "WEDNESDAY FAN APPRECIATION" Giveaway')

    driver.get("https://lock-lab.com/friday-fan-appreciation-free-giveaway/")
    element_1 = driver.find_element_by_xpath('id("post-11230")/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_1.clear()
    element_1.send_keys("axel.johansson10@gmail.com")
    element_2 = driver.find_element_by_xpath('id("post-11230")/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
    element_2.clear()
    element_2.send_keys("Axel Johansson")
    element_3 = driver.find_element_by_xpath('id("post-11230")/div[1]/div[3]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]/span[1]')
    element_3.click()
    print('Sucessfully entered LockLAb "FRIDAY FAN APPRECIATION" Giveaway')
    print('Sucessfully entered all 4 Drawings!')
    print('Closing down..')
    driver.close()

def gettext(args):
    driver =  webdriver.Firefox()

    driver.get(args.url)
    element_1 = driver.find_element_by_xpath(args.XPath)
    print(element_1.text)
    driver.close()

    
def main():

    '''Console script'''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_locklab = subparsers.add_parser('locklab')
    # An argument without - is required
    #parser_locklab.add_argument('locklab', type=int, default=1, help='enter all 4 drawings on LockLab.com')
    parser_locklab.set_defaults(func=locklab)

    parser_gettext = subparsers.add_parser('gettext')
    parser_gettext.add_argument('-url', type=str)
    parser_gettext.add_argument('-XPath', type=str)
    parser_gettext.set_defaults(func=gettext)
    
    if len(sys.argv) <=1:
        sys.argv.append('--help')

    # Show help if no arguments are given
    args = parser.parse_args()
    args.func(args)
    
    
if __name__ == "__main__":
    main()
