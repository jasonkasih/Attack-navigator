# GitLab Hosted ATT&CK Navigator

This project contains a fully-working example of using GitLab.com to:

- Build and deploy an interactive instance of MITRE's [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) on your own GitLab Pages site.
- Parse YAML files you write that define ATT&CK heatmap coverage.
- Pre-populate your ATT&CK Navigator instance with custom layer files matching each YAML file you provide.
- Additionally, create a single combined layer file based on all of your YAML files.

This can help with the following use cases:

- Red Teams looking to track historical coverage of attack techniques across operations, and in total.
- Blue Teams looking to track coverage of detection capabilities.
- Threat Intelligence folks looking to track adversary behaviors.

You can this example build [here](#coming-soon), which includes sample attack data not related to any GitLab initiatives.

## How to use this project

You can read [this blog](#coming-soon) for a detailed explanation of this project.

The high-level steps to use this yourself are:

1. Fork this project to your own namespace.
2. Optionally, make your fork private.
3. Provide your own YAML files inside the `/layers` folder.
4. Manually run the default pipeline.
5. Once the pipeline completes, go to "Deploy" -> "Pages", and check the box "Use unique domain".

That's it! You can now visit your own portal at the URL specified in "Deploy" -> "Pages". If you made the project private, this portal will require you to authenticate with your GitLab credentials.

Going forward, any changes you make to the `/layers` folder will automatically build a new version of the web application including your new layer files.