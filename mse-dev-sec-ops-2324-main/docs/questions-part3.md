# Questions

## Part 3

- **Q3.1**: Setup your CI/CD pipeline with an additional SAST solution. I propose that you use `semgrep` for this task. Get your inspiration here: https://semgrep.dev/for/gitlab and https://docs.gitlab.com/ee/user/application_security/sast/

    **Answer**: see [.gitlab-ci.yml](../.gitlab-ci.yml) file for the implementation of the SAST solution with `semgrep`.

- **Q3.2**: Describe the found problems (alerts) in the `calculator app` (in the original code, git tag `v2.0`)

    **Answer**: The problems found by `semgrep` in the calculator app were described with a security level, a precise location to the vulnerability and a rule id. See the sast report under the artifact for the complete list of vulnerabilities found.

- **Q3.3**: Install DAST OWASP ZAP on your host or in a Docker. Play with OWASP ZAP, analyze the calculator code

    **Answer**: Using the OWASP ZAP Docker image, we ran the following command to scan the calculator app (which is actually our application to be tested in the /src folder) and generate a report in HTML format:
    ```sh
    cd src/
    pdm run flask
    docker run -v $(pwd)/src:/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://host.docker.internal:5000 -g gen.conf -r zap-report.html
    ```

- **Q3.4**: Implement a DAST solution in your pipeline. Get some inspiration here https://docs.gitlab.com/ee/user/application_security/dast/ . Describe what you have integrated in your pipeline. *Note: you must ensure that your application is running while you are testing!*

    **Answer**: see [.gitlab-ci.yml](../.gitlab-ci.yml) file for the implementation of the DAST solution with OWASP ZAP.

- **Q3.5 (optional)**: Normally, the provided code has some bugs (found with SAST), which are discovered by SAST solution. Describe the found bugs (in the original code, git tag `v2.0`) and provide solution to remediate the problems. Indicate which commit/tag contains the corrected code.

    **Answer**: Several differencies were found between the original code and the corrected code such as the addition of the `SECRET_KEY` as an environment variable instead of being hardcoded in the code. The corrected code can be found in the [commit](https://gitlab.forge.hefr.ch/thomas.dagierjo/mse-dev-sec-ops-2324/-/commit/7f0ae9757e26603ca1021986473e797069f26f73).

- **Q3.6 (optional)**: Describe the found bugs (in the original code, git tag `v2.0`) with DAST and provide solution to remediate the problems. Indicate which commit/tag contains the corrected code. Do corrections only in the provided code (no libraries)

    **Answer**: Not done.
