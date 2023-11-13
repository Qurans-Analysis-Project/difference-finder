"""
find-ligatures.py
This script cycles through all json sources and finds arabic ligatures.
The results are written to tmp/ligatures.py
"""

from pathlib import Path
from typing import List

if __name__ == '__main__':
    # Gather all available narrations from source
    src_path = Path('source')
    assert src_path.exists() and src_path.is_dir()
    out_dir = Path('differences/json')
    assert out_dir.exists() and out_dir.is_dir()

    all_jsons: List[Path] = []
    all_jsons.extend([x for x in src_path.rglob('*.json')])

    # Calculate total number of checks for progress bar
    total = len(all_jsons)
    print(f"Found {total} JSON files.")

    # Cycle through them
    