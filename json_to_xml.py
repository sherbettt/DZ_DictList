#!/usr/bin/env python3.12
import json
import xmltodict

with open("sbom.json", "r") as f:
    data = json.load(f)

with open("sbom.xml", "w") as f:
    f.write(xmltodict.unparse(data, pretty=True))