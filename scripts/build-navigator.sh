#!/bin/bash

# install pre-reqs
apt update && apt install -y jq python3-pip python3-yaml
npm install -g @angular/cli

# download navigator
git clone https://github.com/mitre-attack/attack-navigator

# Generate and deploy the custom layers
mkdir "$CI_PROJECT_DIR"/attack-navigator/nav-app/src/assets/custom-templates
python3 "$CI_PROJECT_DIR"/scripts/create-layers.py \
    -i  "$CI_PROJECT_DIR"/layers \
    -o "$CI_PROJECT_DIR"/attack-navigator/nav-app/src/assets/custom-templates

# configure navigator to default to these layers
cd "$CI_PROJECT_DIR"/attack-navigator/nav-app/src/
files=$(ls assets/custom-templates/*.json) # relate path here is intentional, as it is needed for the config file
urls=$(echo "$files" | jq -R -s -c 'split("\n")[:-1]')
jq --argjson urls "$urls" '.default_layers.urls = $urls | .default_layers.enabled = true' assets/config.json > temp.json
mv temp.json assets/config.json

# build navigator
cd "$CI_PROJECT_DIR"/attack-navigator/nav-app
npm install --unsafe-perm --legacy-peer-deps
NODE_OPTIONS=--openssl-legacy-provider ng build

# copy the files to the public GitLab Pages directory
mkdir "$CI_PROJECT_DIR"/public/
cp -r dist/*  "$CI_PROJECT_DIR"/public/
