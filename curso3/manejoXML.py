import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 123 43243  
   </phone>
   <emal hide="yes"/>
</person>'''

tree = ET.fromstring(data) #pones ET o el alias que le hayas puesto y la variable entre parentesis
print("Name:",tree.find("name").text)#cuando le pones .text lo que buscas es el mensaje en si(Chuck)
print("Attr:",tree.find("email").get("hide"))# aca me printea el valor del atributo (yes)
