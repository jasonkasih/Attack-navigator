"""
This script will generate JSON layer files usable in MITRE ATT&CK Navigator.

It pulls the data from individual YAML files inside an input directory
and uses that to write the JSON files. It will also generate a "combined.json"
file which overlays all techniques into one.

Written by GitLab Red Team
"""
import json
import os
import copy
import argparse
import yaml

# This PoC adds a green highlight. You can change this to any color you want.
HIGHLIGHT_COLOR = "#31a354"

# You might want to make changes to the default layout. For example, removing
# technology platform filters that don't apply to your organization.
JSON_BLOB = {
    "name": "",
    "versions": {
        "attack": "13",
        "navigator": "4.8.2",
        "layer": "4.4"
    },
    "domain": "enterprise-attack",
    "description": "",
    "hideDisabled": True,
    "layout": {
        "layout": "flat"
    },
    "filters": {
        "platforms": [
            "Linux",
            "macOS",
            "Windows",
            "Network",
            "PRE",
            "Containers",
            "Office 365",
            "SaaS",
            "Google Workspace",
            "IaaS",
            "Azure AD"
        ]
    },
    "techniques": []
}


def parse_yaml(filename):
    """
    Reads a single YAML file and returns specific data as json using a template
    """
    with open(filename, "r", encoding="utf-8") as writer:
        yaml_data = yaml.load(writer, Loader=yaml.FullLoader)

    json_data = copy.deepcopy(JSON_BLOB)
    json_data["name"] = yaml_data["name"]
    json_data["description"] = yaml_data["description"]

    for tactic, techniques in yaml_data["techniques"].items():
        if techniques:
            for technique in techniques:
                json_data["techniques"].append({"techniqueID": technique,
                                                "tactic": tactic,
                                                "color": HIGHLIGHT_COLOR})

    return json_data


def write_json(json_data, filename):
    """
    Writes a single JSON file given data and a file path
    """
    with open(filename, "w", encoding="utf-8") as writer:
        json.dump(json_data, writer, indent=2)


def parse_combined_json(techniques):
    """
    Generates JSON data for the combined layer files, using a template
    """
    json_data = copy.deepcopy(JSON_BLOB)
    json_data["name"] = "Combined Output"
    json_data["description"] = "All operations combined"
    json_data["techniques"] = techniques

    return json_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", "-i", type=str, required=True)
    parser.add_argument("--output-dir", "-o", type=str, required=True)
    args = parser.parse_args()

    combined_techniques = []

    for filename in os.listdir(args.input_dir):
        if filename.endswith(".yaml"):
            yaml_file = os.path.join(args.input_dir, filename)
            json_data = parse_yaml(yaml_file)

            # Add all ATT&CK techniques to a combined variable
            # for use in a global layer
            for technique in json_data["techniques"]:
                combined_techniques.append(technique)

            # Write the json layer file
            json_file = os.path.splitext(filename)[0] + ".json"
            json_file = os.path.join(args.output_dir, json_file)
            write_json(json_data, json_file)

    json_data = parse_combined_json(combined_techniques)
    json_file = os.path.join(args.output_dir, "zzz-combined.json")
    write_json(json_data, json_file)


if __name__ == "__main__":
    main()
