#XML desde archivo
import xml.etree.ElementTree as ET

try:
    xml_file = open('plants.xml')#apertura
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_plants = xml_data.findall('PLANT')
        for plant in lst_plants:
            print(f"Nombre: {plant.find('COMMON').text}")
            print(f"Botánica: {plant.find('BOTANICAL').text}")
            print("-------------------------------")
    else:
        print(False)
except Exception as err:
    print("Error:", err)
finally:
    xml_file.close()