import yaml
from pathlib import Path


GLOSSARY_PATH = Path("01_governance/glossary.yaml")


def load_glossary():
    """
    Load the business glossary as a dictionary keyed by term name.
    """
    with open(GLOSSARY_PATH, "r") as f:
        glossary_yaml = yaml.safe_load(f)

    terms = glossary_yaml.get("terms", [])
    glossary = {}

    for term in terms:
        glossary[term["term"].lower()] = term

    return glossary


if __name__ == "__main__":
    glossary = load_glossary()
    for k, v in glossary.items():
        print(f"{k}: {v['status']}")
