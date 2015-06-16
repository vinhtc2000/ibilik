#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on May 27, 2015

@author: zinhvcoin
'''
import re
import urllib
from lxml import html
from time import sleep, strftime, gmtime
import codecs
 
def getDetailUrl():
    frefix = ""
    dateTime = strftime("%Y%m%d%H%M%S", gmtime())
    
    frefix = "3126"
    fullReport = ""
    
    for i in range(3126, 19955):
        if i % 1000 == 1:
            frefix = str(i)
            fullReport = ""
            
        print "=========" + str(i)
        url = "http://www.ibilik.my/rooms?page=" + str(i)
        page = html.fromstring(urllib.urlopen(url).read())
        for link in page.xpath("//div[@class='title']/a"):
            href = "http://www.ibilik.my" + link.attrib["href"]
            print href
            fullReport = fullReport + href + "\n"
        
            with codecs.open("D:\\ibilik_Link_"+dateTime + "_" + str(frefix) + ".txt", "w", encoding="utf-8") as f:
                f.write(fullReport)
                f.close()
            
def parserPhoneNumber(description):
    sleep(2)
    #Handle O -> 0, I -> 1
    description = description.lower().replace("o","0")
    description = description.lower().replace("i","1")
    description = description.lower().replace("l","1")
    
#     print description
    # Parser phone number
    phonePattern = re.compile(r'(\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9})')
    phoneNumbers = re.findall(phonePattern, description)
    for i in range(0,len(phoneNumbers)):
        phoneNumber = phoneNumbers[i]
        # Handle phoneNumber
        exPhone = ""
         
        for num in str(phoneNumber).split(" "):
            if len(str(num)) > 1:
                exPhone = exPhone + str(num) + " "
        
        if len(exPhone)>9:
            return exPhone
    
    return "[ERROR] - Can't scrape phone number"

if __name__ == '__main__':
    getDetailUrl()
#     urls = ["http://www.ibilik.my/rooms/1461073/a-c-room-include-utilities-sunway-pjs-taylor-inti-nice-location","http://www.ibilik.my/rooms/1461072/fully-furnished-townhouse-to-let-at-taman-tasik-purchong-can-start-immediately","http://www.ibilik.my/rooms/1461071/furnished-room-monorail-bkt-bintang-rajalaut-sultan-ismail-pudu","http://www.ibilik.my/rooms/1461070/looking-for-housemate-menara-u2","http://www.ibilik.my/rooms/1461069/a-c-room-kdu-iact-um-tropicana-city-mall-location-wise","http://www.ibilik.my/rooms/1461068/suriamas-fully-furnished-small-rooms-to-let-available-july-2015","http://www.ibilik.my/rooms/1461067/mahkota-garden-condo-partially-furnished-3r-2b-2c-p","http://www.ibilik.my/rooms/1461066/a-c-room-include-utilities-tropicana-city-mall-damasara-kim-affordable-nice","http://www.ibilik.my/rooms/1461066/a-c-room-include-utilities-tropicana-city-mall-damasara-kim-affordable-nice","http://www.ibilik.my/rooms/1461065/a-c-room-include-utilities-tropicana-city-mall-damasara-kim-location-wise","http://www.ibilik.my/rooms/1461064/a-c-room-include-utilities-tropicana-city-mall-damasara-kim-affordable-rental","http://www.ibilik.my/rooms/1461063/a-c-room-include-utilities-tropicana-city-mall-damasara-kim-nice-location","http://www.ibilik.my/rooms/1461062/a-c-room-include-utilities-kelana-jaya-affordable-rental","http://www.ibilik.my/rooms/1461061/a-c-room-include-utilities-kelana-jaya-affordable-nice","http://www.ibilik.my/rooms/1461060/a-c-room-include-utilities-kelana-jaya-nice-location","http://www.ibilik.my/rooms/1461058/ken-3-condominium-for-rent-ss2-kdu-pj","http://www.ibilik.my/rooms/1461057/medium-room-for-single-working-chinese-male-female-at-kelana-jaya-lrt-station","http://www.ibilik.my/rooms/1461056/beautiful-nice-room-for-rent-at-usj-taipan","http://www.ibilik.my/rooms/1461055/beautiful-nice-room-for-rent-at-sunway-pjs-taylor-inti","http://www.ibilik.my/rooms/1461054/strategic-location-sunway-pjs-taylor-inti-room-with-aircond-for-rent","http://www.ibilik.my/rooms/1461053/comfortable-rooms-for-rent-at-paradigm-mall-kelana-jaya","http://www.ibilik.my/rooms/1461052/a-c-room-include-utilities-sunway-pjs-taylor-inti-nice-location","http://www.ibilik.my/rooms/1461051/nice-comfortable-aircond-room-bandar-puteri-puchong","http://www.ibilik.my/rooms/1461050/aircond-room-bandar-puteri-puchong-nice-comfortable","http://www.ibilik.my/rooms/1461049/spacious-aircond-room-sri-andalas-taman-sentosa-botanic-include-utility","http://www.ibilik.my/rooms/1461048/wawasan-puchong-mall-beautiful-and-clean-include-utilities","http://www.ibilik.my/rooms/1461047/aircond-room-bandar-puteri-klang-botanic-inclusive-utility","http://www.ibilik.my/rooms/1461046/nice-aircond-room-sri-andalas-taman-sentosa-botanic-include-utilities","http://www.ibilik.my/rooms/1461045/room-for-rent-at-setia-alam-shah-alam-included-electric","http://www.ibilik.my/rooms/1461044/aircond-room-botanic-sri-andalas-taman-sentosa-cheap","http://www.ibilik.my/rooms/1461043/strategic-location-paradigm-mall-kelana-jaya-room-with-aircond-for-rent","http://www.ibilik.my/rooms/1461042/beautiful-nice-room-for-rent-at-tropicana-city-mall-damasara-kim","http://www.ibilik.my/rooms/1461041/a-c-room-include-utilities-tropicana-city-mall-damasara-kim-nice-location"]
#     
#     fullReport = ""
#     for i in range(0,len(urls)):
#         page = html.fromstring(urllib.urlopen(urls[i]).read())
#     #     page = html.fromstring("""
#     #     """)
#         location1 = page.xpath("//div[@class='user_nav']/a")[2].text
#         location2 = page.xpath("//div[@class='user_nav']/a")[3].text
#         description = html.tostring(page.xpath("//div[@class='rental_wrapper']")[0])
#         phoneNum = parserPhoneNumber(description)
#         print "==============================================="
#         print "URL:\t\t" + urls[i]
#         print "Location 1:\t" + location1
#         print "Location 2:\t" + location2
#         print "Description:\t" + phoneNum
#         print "==============================================="
#         
#         fullReport = fullReport + str(urls[i]) + "\t" + location1 + "\t" + location2 + "\t" + phoneNum + "\n"
#         
#         f = open("D:\\" + "ibilik.txt", 'w+')
#         f.writelines(fullReport + "\n")
#         f.close()
        