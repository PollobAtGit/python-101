import sys
import xml.etree.ElementTree as etree

def recursive_attr_number(node):
    score = 0
    for child in node:
        score += len(child.attrib) + recursive_attr_number(child)
    return score 

def get_attr_number(node):
    return recursive_attr_number(node) + len(node.attrib)

if __name__ == '__main__':
    line_cnt = int(input())
    xml = ""

    while line_cnt:
        xml += input()
        line_cnt = line_cnt - 1

    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
