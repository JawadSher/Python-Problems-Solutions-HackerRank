import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, nesting_level):
    global maxdepth
    
    nesting_level = nesting_level + 1
    
    for i in elem:
        depth(i, nesting_level)
        
    if(nesting_level > maxdepth):
        maxdepth = nesting_level

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
