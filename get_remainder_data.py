from html.parser import HTMLParser
import requests
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError
import json
from lxml import html

def do_a_field_page(url, count=0, output=[]):

    data = requests.get(url)
    text = data.text
    doc = html.fromstring(text)
    doc_ul = doc.xpath("//ul")
    doc_divs = doc.xpath("//div")
    if len(doc_ul) == 0:
        for div in doc_divs:
            if div.attrib.get("class") == "fieldtoc":
                check = False
                if div.xpath("strong"):
                    check = True
                    label = div.xpath("strong")[0].text
        try:
            label
        except UnboundLocalError:
            url
        links = div.xpath("a")
    else:
        for line in doc_ul[0].xpath("li"):
            try:
                label = line.xpath("strong")[0].text
            except IndexError:
                label = line.text
            #print(line.text)
        children = line.getchildren()
        links = line.xpath("span/a")
        if not links:
            pass
        else:
            links = line.xpath('span/a')
    try:
        print(label, links)
    except UnboundLocalError:
        pass
    return ([], count)
    """
    for line in lines:
        a_record = {}
        code_and_label = line.find("{http://www.w3.org/1999/xhtml}strong")
        field = code_and_label.text
        code = field[0:field.index('-')-1].strip()
        label = field[field.index('-')+1:].strip()
        a_record["field"] = code
        a_record["label"] = label
        link_to_follow = [x for x in line.findall("{http://www.w3.org/1999/xhtml}span/{http://www.w3.org/1999/xhtml}a") if x.text == 'Concise'][0]
        followed_data = requests.get('http:'+link_to_follow.attrib["href"])
        followed_text = followed_data.text
        tree = html.fromstring(followed_text)
        result = tree.xpath("//div")
        subfields = []
        indicators = []
        for n in result:
            a_subfield = {}
            a_indicator = {}
            if n.attrib.get('class') == 'subfieldvalue':
                text_data = n.text
                subfield_code = text_data[0:text_data.index('-')]
                subfield_label = text_data[text_data.index('-')+1:]
                a_subfield["code"] = subfield_code.strip()
                a_subfield["label"] = subfield_label.strip()
                subfields.append(a_subfield)
            if n.attrib.get('class') == 'indicatorvalue':
                in_text_data = n.text
                in_code = in_text_data[0:in_text_data.index('-')]
                in_label = in_text_data[in_text_data.index('-')+1:]
                a_indicator["code"] = in_code.strip()
                a_indicator["label"] = in_label.strip()
                indicators.append(a_indicator) 
            a_record["subfields"] = subfields
            a_record["indicators"] = indicators
            fields.append(a_record)
        print("completed field {}; code {}".format(str(count), code))
        count += 1
        """


if __name__ == "__main__":
    fields = []
    count = 0
    opening_salvo = requests.get("https://www.loc.gov/marc/bibliographic/")
    data = opening_salvo.text
    tree = html.fromstring(data)
    divs = tree.xpath("//div")
    for div in divs:
        if div.attrib.get("class") == 'contentslist':
            lines = div.xpath("ul/li")
            for line in lines:
                if 'Fields' in line.xpath("a")[0].text:
                    field_page_link = 'https://loc.gov/marc/bibliographic/' + (line.xpath("a")[0].attrib["href"])
                    output, count = do_a_field_page(field_page_link, count=count, output=fields)

    #fields = []
    #json.dump(fields, open("test.json", "w", encoding="utf-8"), indent=4)