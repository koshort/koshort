"""Constants used in koshort library. """
import os

DATA_DIR = "data/"
ALPHABET = ["가","나","다","라","마","바","사","아","자","차","카","타","파","하"]

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)