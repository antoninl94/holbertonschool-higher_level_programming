#!/usr/bin/python3
"""
This is the ``task_03_xml`` module
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function serialize an object in xml format
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            items = ET.SubElement(root, key)
            items.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(filename)
    except Exception:
        return


def deserialize_from_xml(filename):
    """
    This function create an object from a xml file
    """
    try:
        data = ET.parse(filename)
        root = data.getroot()
        dictionnary = {}
        for child in root:
            dictionnary[child.tag] = child.text
        return dictionnary
    except Exception:
        return
