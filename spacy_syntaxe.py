from pathlib import Path
import spacy
from spacy.tokens import Doc
from spacy import displacy
import re 
nlp = spacy.load("fr_core_news_lg")

sentence = "Peux tu raconter une courte scène mettant en scène un médecin ?"

doc = nlp(sentence)
opts = {
    "fine_grained": True, 

}

svg = displacy.render(doc, style="dep", options=opts)
output_path = Path("export_spacy.svg")
with output_path.open("w", encoding="utf-8") as f:
    f.write(svg)