from fastapi import FastAPI
from pydantic import BaseModel
import xml.etree.ElementTree as ET

app = FastAPI()

class Restaurant(BaseModel):
    name: str
    location: str
    cuisines: str
    avg_cost_for_two: float
    rating: float

def json_to_xml(data):
    root = ET.Element("Restaurant")
    for k, v in data.items():
        child = ET.SubElement(root, k)
        child.text = str(v)
    return ET.tostring(root, encoding="unicode")

@app.post("/mediate")
def mediate(record: Restaurant):
    # Masking example
    data = record.dict()
    data["name"] = data["name"][0] + "***" + data["name"][-1]
    
    # Simulate JSON -> XML -> JSON
    xml = json_to_xml(data)
    
    return {"canonical": data, "xml": xml}
