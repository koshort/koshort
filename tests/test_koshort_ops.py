import koshort
import glob
from koshort.constants import DATA_DIR

def test_clear_data():
    """Check if file is correctly cleared."""

    koshort.clear()
    items = glob.glob(DATA_DIR+"*")
    assert len(items) == 0