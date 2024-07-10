import xml.etree.cElementTree as ET

root = ET.Element("my_menu")

ET.SubElement(root, "food", name="nome").text = "pizza"
ET.SubElement(root, "food", name="nome").text = "pasta"

tree = ET.ElementTree(root)
tree.write("mymenu.xml")