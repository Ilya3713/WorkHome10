
import xml.etree.ElementTree as ET
import json
from collections import Counter
from collections import OrderedDict

lists_data = list()
ddata = {}  
out = {}

def Get_xml():
  tree = ET.parse("newsafr.xml")
  root = tree.getroot()
  xml_items = root.findall("channel/item/description")
  for xmli in xml_items:
      for i in xmli.text.split(' '):
        if len(i) >= 6:
          lists_data.append(i.upper())
          
  counter = Counter(lists_data)

  for key, value in counter.items(): 
      dic_value = ddata.get(key)  
      if dic_value != None: 
          if dic_value > value:
              value = dic_value
      ddata.update({key: value})

  s = (OrderedDict(sorted(ddata.items(), key=lambda t: t[1], reverse=True)))
  srez3 = list(s)[0:10] # срез, топ 10


  print ('Топ 10 повторяющихся слов:\n')
  for key_srez in srez3:  
      print ( key_srez, ":", ddata.get(key_srez))



def Get_json():
  with open('newsafr.json') as files:
    data = json.load(files)

  for items in data['rss']['channel']['items']:
    for i in items['description'].split(' '):
      if len(i) >= 6:
        lists_data.append(i.upper())
        

  counter = Counter(lists_data)
  
  for key, value in counter.items(): 
      dic_value = ddata.get(key)  
      if dic_value != None: 
          if dic_value > value:
              value = dic_value
      ddata.update({key: value})

  s = (OrderedDict(sorted(ddata.items(), key=lambda t: t[1], reverse=True)))
  srez3 = list(s)[0:10] # срез, топ 10

  print ('Топ 10 повторяющихся слов:\n')
  for key_srez in srez3:  
      print ( key_srez, ":", ddata.get(key_srez))



number_Get = input('Введите в каком формате парсить json или xml: \n')
if str(number_Get) == 'json':
  Get_json()
elif str(number_Get) == 'xml':
  Get_xml()
else:
  print('Неверный формат. Укажите json либо xml')
