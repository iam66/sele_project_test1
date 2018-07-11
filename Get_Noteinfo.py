from xml.dom import minidom

#打开xml文件
dom=minidom.parse('E:\\python_practice\\xml_read\\class_info.xml')

root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
