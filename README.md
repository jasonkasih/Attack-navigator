# GitLab Hosted ATT&CK Navigator

This project shows how you can use GitLab.com to build and deploy your own instance of MITRE's [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator).

We've included automation to parse user-provided YAML files, which will then pre-populate the application with annotated matrixes (singular and combined). The build is automatically hosted using GitLab Pages with optional authentication, giving you a full solution to visualize your coverage of the [MITRE ATT&CK framework](https://attack.mitre.org/).

You can see this example build [here](https://gitlab-hosted-attack-navigator-gitlab-com-gl-sec-8122c70a07a435.gitlab.io/), and read [this blog](#coming-soon) for a detailed explanation of the project and how we use it ourselves.

![screenshot](navigator-screenshot.png)

## How to use this project

The high-level steps to use this yourself are:

1. Fork this project to your own namespace.
2. Optionally, make your fork private.
3. Provide your own YAML files inside the `layers/` folder. Use the `templates/template.yaml` file as guidance.
4. Run the default pipeline if you didn't already kick it off by changing content in the `layers/` folder.
4. Once the pipeline has completed, go to "Deploy" -> "Pages", and check the box "Use unique domain".

That's it! You can now visit your site at the URL specified in "Deploy" -> "Pages". If you made the project private, it will require you to authenticate with your GitLab credentials.

Going forward, any changes you make to the `layers/` folder will automatically build a new version of the application including your new layer files.