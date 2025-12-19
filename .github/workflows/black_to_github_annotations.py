from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TypedDict

import github_action_utils as gha_utils


REPO_PATH = Path(__file__).parent.parent.parent

class Entry(TypedDict):
    location: Location


class Location(TypedDict):
    path: str
    lines: Lines


class Lines(TypedDict):
    begin: int
    end: int


json_data: list[Entry] = json.load(sys.stdin)
for change in json_data:
    location = change["location"]
    path = location["path"]
    lines = location["lines"]
    print("error title=Black Format Issue,file=src/bonsai/bonsai/bim/module/drawing/gizmos.py,line=90::Black formatting issue in src/bonsai/bonsai/bim/module/drawing/gizmos.py")
    print("::error title=Black Format Issue,file=src/bonsai/bonsai/bim/module/drawing/gizmos.py,line=90::Black formatting issue in src/bonsai/bonsai/bim/module/drawing/gizmos.py")
    print("error title=Black Format Issue,file=src/bonsai/bonsai/bim/module/drawing/gizmos.py,line=90,endLine=90::Black formatting issue in src/bonsai/bonsai/bim/module/drawing/gizmos.py")
    print("::error title=Black Format Issue,file=src/bonsai/bonsai/bim/module/drawing/gizmos.py,line=90,endLine=90::Black formatting issue in src/bonsai/bonsai/bim/module/drawing/gizmos.py")
    gha_utils.error(
        f"Black formatting issue in {path}",
        title="Black Format Issue",
        file=path,
        line=lines["begin"],
        end_line=lines["end"],
    )
