"""Constants used in koshort library. """
import os

DATA_DIR = "data/"

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)