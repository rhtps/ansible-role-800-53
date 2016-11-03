import sys
import xmltodict
import yaml

with open(sys.argv[1]) as fd:
    doc = xmltodict.parse(fd.read(), xml_attribs=True)
print yaml.dump(doc, default_flow_style=False)
