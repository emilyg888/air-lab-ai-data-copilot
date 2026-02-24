from pathlib import Path


SEMANTIC_LAYER_PATH = Path("02_semantic_layer")
VIEW_DEFS_PATH = SEMANTIC_LAYER_PATH / "view_definitions"


def load_semantic_views():
    """
    Load semantic view documentation as text blobs.
    """
    views = {}

    for md_file in VIEW_DEFS_PATH.glob("*.md"):
        view_name = md_file.stem
        views[view_name] = md_file.read_text(encoding="utf-8")

    return views


if __name__ == "__main__":
    views = load_semantic_views()
    for name in views.keys():
        print(f"Loaded semantic view: {name}")
