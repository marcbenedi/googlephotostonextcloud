from xml.etree.ElementTree import Element, SubElement, tostring


def get_default_xml_body():
    propfind = Element('d:propfind', {'xmlns:d': 'DAV:', 'xmlns:oc': 'http://owncloud.org/ns', 'xmlns:nc': 'http://nextcloud.org/ns'})
    prop = SubElement(propfind, 'd:prop')
    SubElement(prop, 'd:getlastmodified')
    SubElement(prop, 'd:getcontentlength')
    SubElement(prop, 'd:getcontenttype')
    SubElement(prop, 'oc:permissions')
    SubElement(prop, 'd:resourcetype')
    SubElement(prop, 'd:getetag')

    xml_body = tostring(propfind, encoding='utf-8', method='xml')
    return xml_body