# coding: utf-8

# This script is used for crawling Cisco Support Community
# Created by Kun Huang, Dec 21, 2014

# Headers for HTTP POST request, depending on the categories
headers = {
    "datacenter":{
        "from_data": '''
        {
            "view_name": "cisco_community_activity",
            "view_display_id": "discussions_pane",
            "view_args": "4436",
            "view_path": "node/4436",
            "view_base_path": null,
            "view_dom_id": "322d77d771f9c99c219003cd2b6726e0",
            "pager_element": "0",
            "field_is_answered_value_i18n": "All",
            "items_per_page": "45",
            "page": "1"
        }
        ''',
        "request_headers": {
            'Host': 'supportforums.cisco.com',
            'Connection': 'keep-alive',
            'Content-Length': '23459',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Origin': 'https://supportforums.cisco.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://supportforums.cisco.com/community/4436/data-center',
        }
    },
    "vpn":{
        "from_data": '''
        {
            "view_name": "cisco_community_activity",
            "view_display_id": "discussions_pane",
            "view_args": "6001",
            "view_path": "node/6001",
            "view_base_path": null,
            "view_dom_id": "cab8f63bf8271a8eb6e54d02d44a6142",
            "pager_element": "0",
            "field_is_answered_value_i18n": "All",
            "items_per_page": "45",
            "page": "1"
        }
        ''',
        "request_headers": {
            'Host': 'supportforums.cisco.com',
            'Connection': 'keep-alive',
            'Content-Length': '23459',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Origin': 'https://supportforums.cisco.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://supportforums.cisco.com/community/6001/vpn',
        }
    },
    "firewalling": {
        "from_data": '''
        {
            "view_name": "cisco_community_activity",
            "view_display_id": "discussions_pane",
            "view_args": "5966",
            "view_path": "node/5966",
            "view_base_path": null,
            "view_dom_id": "ace0ce237475a149522dd17ff0640a62",
            "pager_element": "0",
            "field_is_answered_value_i18n": "All",
            "items_per_page": "45",
            "page": "1"
        }
        ''',
        "request_headers": {
            'Host': 'supportforums.cisco.com',
            'Connection': 'keep-alive',
            'Content-Length': '23459',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Origin': 'https://supportforums.cisco.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://supportforums.cisco.com/community/5966/firewalling',
        }
    },
    "AAA-Identity-NAC": {
        "from_data": '''
        {
            "view_name": "cisco_community_activity",
            "view_display_id": "discussions_pane",
            "view_args": "5936",
            "view_path": "node/5936",
            "view_base_path": null,
            "view_dom_id": "fb85ec6cdc2d65b299897c21422fc896",
            "pager_element": "0",
            "field_is_answered_value_i18n": "All",
            "items_per_page": "45",
            "page": "1"
        }
        ''',
        "request_headers": {
            'Host': 'supportforums.cisco.com',
            'Connection': 'keep-alive',
            'Content-Length': '23459',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Origin': 'https://supportforums.cisco.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://supportforums.cisco.com/community/5936/aaa-identity-and-nac',
        }
    },
    "WAN-Routing-Switching": {
        "from_data": '''
        {
            "view_name": "cisco_community_activity",
            "view_display_id": "discussions_pane",
            "view_args": "5991",
            "view_path": "node/5991",
            "view_base_path": null,
            "view_dom_id": "aa92cb93d0c913e404b9f6ee53837733",
            "pager_element": "0",
            "field_is_answered_value_i18n": "All",
            "items_per_page": "45",
            "page": "1"
        }
        ''',
        "request_headers": {
            'Host': 'supportforums.cisco.com',
            'Connection': 'keep-alive',
            'Content-Length': '23459',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Origin': 'https://supportforums.cisco.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://supportforums.cisco.com/community/5991/wan-routing-and-switching',
        }
    },
    "LAN-Routing-Switching": {
        "from_data": '''
        {
            "view_name": "cisco_community_activity",
            "view_display_id": "discussions_pane",
            "view_args": "6016",
            "view_path": "node/6016",
            "view_base_path": null,
            "view_dom_id": "82199667345356dd9cf881e8f73c2dbb",
            "pager_element": "0",
            "field_is_answered_value_i18n": "All",
            "items_per_page": "45",
            "page": "1"
        }
        ''',
        "request_headers": {
            'Host': 'supportforums.cisco.com',
            'Connection': 'keep-alive',
            'Content-Length': '23459',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Origin': 'https://supportforums.cisco.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://supportforums.cisco.com/community/6016/lan-switching-and-routing',
        }
    }
}

import requests
import json
import pdb
import csv
from bs4 import BeautifulSoup as Soup
import sys
import os.path

def main():
    # Read from command line
    category_list = ['firewalling', 'vpn', 'datacenter', "AAA-Identity-NAC", "WAN-Routing-Switching", "LAN-Routing-Switching"]
    if len(sys.argv) != 3 or str(sys.argv[1]) not in category_list:
        print 'Usage: python detail_crawler.py [category] [number of pages]'
        print 'Example: python detail_crawler.py ' + category_list[0] + ' 500'
        print 'Valid categories:'
        print category_list
        sys.exit(-1)

    category = str(sys.argv[1])
    num_page = int(sys.argv[2])

    # Open files for writing
    url_path = 'data/'+category+'/'+category+'_url.csv'
    log_path = 'data/'+category+'/'+category+'_url_crawler_log.txt'
    
    if os.path.isfile(url_path) == True:
        print "The url file:"+url_path+" already exists."
        sys.exit(-1)

    if not os.path.exists('data/'+category):
        os.makedirs('data/'+category)

    try:
        f_log = open(log_path, 'wb')
    except:
        print "Can't open url file:"+log_path
        sys.exit(-1)
    try:
        f_url = open(url_path, 'wb')
    except:
        print "Can't open url file:"+url_path
        sys.exit(-1)

    from_data = json.loads(headers[category]['from_data'])

    writer = csv.writer(f_url)
    writer.writerow(['page' ,'subject', 'url'])

    for i in range(2,num_page):
        try:
            from_data['page'] = str(i-1)
            r = requests.post('https://supportforums.cisco.com/views/ajax', data=from_data)
            html = json.loads(r.text)[2][u'data'].encode('utf-8')
            
            rows = [[i, a.string.encode('utf-8'), 'https://supportforums.cisco.com'+a['href'],]  for a in Soup(html).select('.views-field.views-field-title > a')]
            writer.writerows(rows)
            
            print "#success page"+str(i)
            f_log.write("#success page"+str(i)+'\n')
        except Exception, e:
            print "#fail page"+str(i)
            f_log.write("#fail page"+str(i)+'\n')
                   
    f_url.close()
    f_log.close()

if __name__ == '__main__':
    main()