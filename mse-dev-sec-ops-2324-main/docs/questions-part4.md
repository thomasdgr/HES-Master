# Questions

## Part 4
- **Q4.1**: Often secrets are committed in a repository. Different research tools exist and help to detect this kind of dangerous forgotten credentials. Integrate a check in your pipeline for these kinds of problems. Have a look at https://github.com/zricethezav/gitleaks. What kind of leaked secrets can you find in the git repo? Did the tool not find something that it should have found? Why? What possibilities exist to prevent this kind of leakage?

    **Answer**: GitLeaks is a tool that scans the repository for secrets. It can be integrated into the pipeline to prevent secrets from being leaked such as passwords and API_Keys, tokens, private or cryptographic keys and even config files. See the [.gitlab-ci.yml](../.gitlab-ci.yml) file for the implementation of the GitLeaks solution. The tool found some secrets in the repository, such as the `SECRET_KEY` in the `.env` file. The tool did not find the `API_KEY` in the `.env` file because it was not included in the default GitLeaks rules. To prevent this kind of leakage, we can create a `.gitleaks.toml` file with custom rules to include the `API_KEY` in the scan. We can also use the `.gitignore` file to exclude the `.env` file from being committed to the repository.

- **Q4.2**: Try to find any possible problems in our used libraries (e.g. flask). The `pyproject.toml` describes all the additional libraries used by the application. You can use a dependency scanning (have a look here: https://docs.gitlab.com/ee/user/application_security/dependency_scanning/) to see if all imported libraries are safe. Do you find any problems? Integrate the scanning in your pipeline.

    **Answer**: We can implement a dependency scanning in the pipeline to check for vulnerabilities in the libraries used by the application. The output of the scan can be found in the section "Secure>Dependency List" on GitLab. See the [.gitlab-ci.yml](../.gitlab-ci.yml) file for the implementation of the Dependency Scanning solution. We found several vulnerabilities in the libraries used by the application, such as Jinja2 or MarkupSafe.

- **Q4.3 (optional)**: API Fuzzing (and other kinds of DAST) is described at this page: https://docs.gitlab.com/ee/user/application_security/api_fuzzing/ . Choose one of the different description possibilities for your *calculator* API. Integrate it in your pipeline.

    **Answer**: See the [.gitlab-ci.yml](../.gitlab-ci.yml) file for the implementation of the API Fuzzing solution.