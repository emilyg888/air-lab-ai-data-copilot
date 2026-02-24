import yaml
from pathlib import Path


DATASET_REGISTER_PATH = Path("01_governance/dataset_register.yaml")


def load_dataset_register():
    """
    Load the dataset register as a dictionary keyed by dataset name.
    """
    with open(DATASET_REGISTER_PATH, "r") as f:
        register_yaml = yaml.safe_load(f)

    datasets = register_yaml.get("datasets", [])
    register = {}

    for ds in datasets:
        register[ds["name"]] = ds

    return register


if __name__ == "__main__":
    register = load_dataset_register()
    for name, meta in register.items():
        print(f"{name}: {meta['status']}")
