import koshort
import os
from koshort.constants import DATA_DIR

def test_clear_data():
    """Check if file is correctly cleared."""

    koshort.clear()
    items = os.listdir(DATA_DIR)
    assert len(items) == 0