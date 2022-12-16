# import openpyxl
# from natasha import (
#     Segmenter,
#     MorphVocab,
#
#     NewsEmbedding,
#     NewsMorphTagger,
#     NewsSyntaxParser,
#     NewsNERTagger,
#
#     PER,
#     NamesExtractor,
#     DatesExtractor,
#     MoneyExtractor,
#     AddrExtractor,
#
#     Doc
# )
# segmenter = Segmenter()
# morph_vocab = MorphVocab()
#
# emb = NewsEmbedding()
# morph_tagger = NewsMorphTagger(emb)
# syntax_parser = NewsSyntaxParser(emb)
# ner_tagger = NewsNERTagger(emb)
#
# names_extractor = NamesExtractor(morph_vocab)
# dates_extractor = DatesExtractor(morph_vocab)
# money_extractor = MoneyExtractor(morph_vocab)
#
# book = openpyxl.open("C:/Users/W1zzA/PycharmProjects/dmc_project/try.xlsx", read_only=True)
#
# data = book.active
#
# text = data["A1"].value
# print(text)
#

import pandas as pd
import openpyxl
from natasha import AddressExtractor, NamesExtractor
from natasha.markup import show_markup, show_json
from deeppavlov import configs, build_model
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertTokenizerFast

# tokenizer = AutoTokenizer.from_pretrained("blanchefort/rubert-base-cased-sentiment")
# model = AutoModelForSequenceClassification.from_pretrained("blanchefort/rubert-base-cased-sentiment")

# book = openpyxl.open("try.xlsx", read_only=True)
#
# data = book.active
#
# text = data["A1"].value
# print(text)
#
# from transformers import AutoTokenizer, AutoModelForMaskedLM
#
# tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-large')
# model = AutoModelForMaskedLM.from_pretrained("xlm-roberta-large")
#
# # prepare input
# encoded_input = tokenizer(text, return_tensors='pt')
#
# # forward pass
# output = model(**encoded_input)
# print(output)
#



# # Import generic wrappers
# from transformers import AutoModel, AutoTokenizer
#
#
# # Define the model repo
# model_name = "microsoft/Multilingual-MiniLM-L12-H384"
#
#
# # Download pytorch model
# model = AutoModel.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
#
#
# # Transform input tokens
# inputs = tokenizer("Hello world!", return_tensors="pt")
# print(inputs)
# print("**********************")
# # Model apply
# outputs = model(**inputs)
# print(outputs)
# print("**********************")
#



# row = 15910
# cout = 0
# while cout < 15913:
#     try:
#         text = data.cell(row=row, column=6).value
#         extractor = AddressExtractor()
#         matches = extractor(text)
#         spans = [_.span for _ in matches]
#         facts = [_.fact.as_json for _ in matches]
#         show_markup(text, spans)
#         show_json(facts)
#         cout += 1
#         row += 1
#     except AttributeError:
#         print("object has no attribute 'translate'")
#         cout += 1
#         row += 1
#         text = data.cell(row=row, column=6).value
#         extractor = AddressExtractor()
#         matches = extractor(text)
#         spans = [_.span for _ in matches]
#         facts = [_.fact.as_json for _ in matches]
#         show_markup(text, spans)
#         show_json(facts)
#         cout += 1
#         row += 1

# extractor = AddressExtractor()
# matches = extractor(text)
# spans = [_.span for _ in matches]
# facts = [_.fact.as_json for _ in matches]
# show_markup(text, spans)
# show_json(facts)