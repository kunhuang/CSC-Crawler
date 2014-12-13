# coding: utf-8

# This script is used for crawling Cisco Support Community
# Created by Kun Huang, Dec 21, 2014

import re
import glob
import os
from dateutil.parser import parse as dateparse
import csv
import requests
import pdb
from bs4 import BeautifulSoup as Soup
import sys
import os.path

# Get "Category" from CSC, by html text
def get_category(html):
    return Soup(html).select('ul.breadcrumb > li:nth-of-type(3) > a')[0].string

# Get "Number of Relies" from CSC, by html text
def get_replies(html):
    return Soup(html).select('table.table-striped tr:nth-of-type(1) td:nth-of-type(2)')[0].string

# Get "Avg.rating" from CSC, by html text
def get_rating(html):
    return Soup(html).select('table.table-striped tr:nth-of-type(1) td:nth-of-type(5)')[0].string

# Get "Number of View" from CSC, by html text
def get_views(html):
    return Soup(html).select('table.table-striped tr:nth-of-type(2) td:nth-of-type(2)')[0].string

# Get "Number of Votes" from CSC, by html text
def get_votes(html):
    return Soup(html).select('table.table-striped tr:nth-of-type(2) td:nth-of-type(5)')[0].string

# Get "Number of Shares" from CSC, by html text
def get_shares(html):
    return Soup(html).select('table.table-striped tr:nth-of-type(3) td:nth-of-type(2)')[0].string

# Get if the question is answered yet
def get_if_answered(html):
    return [u'answered'] == Soup(html).select('div.question-status > div')[0]['class']

# Get the url of person who posted the question
def get_description_person(html):
    return Soup(html).select('div.discussion-content span.fullname > a')[0]['href']

# Get the time of question post
def get_description_time(html):
    return Soup(html).select('div.discussion-content span.created > abbr')[0].string

# Get the content of the question
def get_description_content(html):
    return '\n'.join([line.string.encode('utf-8') for line in Soup(html).select('.discussion-content-wrapper div.discussion-body > div.field > div.field-items > div.field-item > p') if  line.string != None])

# Get the array of reply info, including person, time content, the reply_to id, and whether it's the correct answer
def get_reply_array(html):
    # Get single reply info by the article tag
    def get_reply_info(article_tag, reply_to):
        # Structure
        # [person, time, content, reply_to, correct_answer]
        try:
            return [article_tag.select('.fullname a')[0]['href'],
                    article_tag.select('.created span.timeago')[0].string,
                    '\n'.join([line.string.encode('utf-8') for line in article_tag.select('div.discussion-body > div.field > div.field-items > div.field-item > p') if line.string != None]),
                    reply_to,
                    len(article_tag.select('.correctAnswer')) != 0,]
        except:
            print 'error'
            print [line.string for line in article_tag.select('div.discussion-body > div.field > div.field-items > div.field-item > p')]

    # make the reply tree structure into reply_array[],
    def make_reply_tree(indented_tag, reply_array, root_node):
        article = indented_tag.select('article:nth-of-type(1)')[0]
        reply_array.append(get_reply_info(article, root_node))
        while(article.find_next_sibling() != None):
            if article.find_next_sibling().has_attr('class') and article.find_next_sibling()['class'] == [u'indented']:
                current_node = len(reply_array)
                make_reply_tree(article.find_next_sibling(), reply_array, current_node)
                article = article.find_next_sibling()
            else:
                article = article.find_next_sibling('article')
                reply_array.append(get_reply_info(article, root_node))
        return len(reply_array)
    
    reply_array = []
    threaded_view = Soup(html).select('#comments .threaded-view')[0]
    make_reply_tree(threaded_view, reply_array, 0)
    
    return reply_array

def main():
    # html = requests.get('https://supportforums.cisco.com/discussion/12365761/security-levels-subinterfaces-adaptive-security-appliance').text.encode('utf-8')
    # html = requests.get('https://supportforums.cisco.com/discussion/12373296/change-asa5510-asa5515-x').text.encode('utf-8')
    # html = requests.get('https://supportforums.cisco.com/discussion/12367741/cisco-2500-series-router-reset-factory-default').text.encode('utf-8')
    html = requests.get('https://supportforums.cisco.com/discussion/12372231/help-2-subnets-lan-asr5505-and-isr-1921').text.encode('utf-8')
    html = requests.get('https://supportforums.cisco.com/discussion/12370671/ipsec-tunnel-query').text.encode('utf-8')
    html = requests.get('https://supportforums.cisco.com/discussion/12369136/crypto-3560c-ikev2-ipsec').text.encode('utf-8')

    category_list = ['firewalling', 'vpn', 'datacenter', "AAA-Identity-NAC", "WAN-Routing-Switching", "LAN-Routing-Switching"]
    
    # Read from command line
    if len(sys.argv) != 2 or str(sys.argv[1]) not in category_list:
        print 'Usage: python detail_crawler.py [category]'
        print 'Example: python detail_crawler.py ' + category_list[0]
        print 'Valid categories:'
        print category_list
        sys.exit(-1)
        
    category = str(sys.argv[1])

    # Open files for reading and writing
    url_path = 'data/'+category+'/'+category+'_url.csv'
    out_path = 'data/'+category+'/'+category+'_detail.csv'
    log_path = 'data/'+category+'/'+category+'_detail_crawler_log.txt'
    try:
        f_log = open(log_path, 'w')
    except:
        print "Can't open log file:"+log_path
        sys.exit(-1)
    try:
        f_out = open(out_path, 'w')
    except:
        print "Can't open output file:"+out_path
        sys.exit(-1)
    try:
        f_url = open(url_path, 'rb')
    except:
        print "Can't open url file:"+url_path
        sys.exit(-1)


    f_out_writer = csv.writer(f_out)
    f_out_writer.writerow(('URL', 'Category', 'Title', '#Replies', 'Rating', '#Views', '#Votes', '#Shares', 'Description-Person', 'Description-Time', 'Description-Content', 'Answered', 'Reply-Person', 'Reply-Time', 'Reply-Content', 'Replay-To', 'Correct Answer'))

    f_url_reader = csv.reader(f_url)
    headers = f_url_reader.next()

    current_num = 1
    for url_row in f_url_reader:
        url = url_row[2]
        title = url_row[1]    
        try:
            # Grap HTML content
            html = requests.get(url).text.encode('utf-8')
            
            # Parse info
            row = [
                url,
                get_category(html),
                title,
                get_replies(html),
                get_rating(html),
                get_views(html),
                get_votes(html),
                get_shares(html),
                get_description_person(html),
                get_description_time(html),
                get_description_content(html),
                get_if_answered(html),
            ]
            if int(get_replies(html)) > 0:
                reply_array = get_reply_array(html)
                for reply in reply_array:
                    row = row + reply
            
            # Write into out file
            f_out_writer.writerow(row)

            # Print and write the log
            print '%d #success url:%s'%(current_num, url)
            f_log.write('%d #success url:%s\n'%(current_num, url))
            current_num = current_num + 1
        except:
            # Print and write the log
            print '%d #fail url:%s'%(current_num, url)
            f_log.write('%d #fail url:%s\n'%(current_num, url))
            current_num = current_num + 1

if __name__ == '__main__':
    main()