# Questions

## Part 2

- **Q2.1**: Every commit triggers the CI/CD pipeline. Find out a way to trigger the pipeline only if specific commits (e.g. commit in a development branch) are made. Where can this be configured. Describe your solution and implement it in your pipeline.
  
    **Answer**: The pipeline can be configured to run only on specific branches or tags by using the `only` keyword in the [.gitlab-ci.yml](../.gitlab-ci.yml) file. As we can suppose development branch are any branch that are note 'main', we just can replace the `only` keyword by `except` and specify the `main` branch. This way, the pipeline will run only when a commit is made to a `development` branch and not on the `main` branch.

- **Q2.2**: Take the [CIS controls](./CIS_Controls_v8_Online.22.02.pdf) and give some examples of controls from this standard that are not or not enough implemented in the calculator app.
  
    **Answer**: In the CIS controls, there are several controls that are not or not enough implemented in the calculator app such as the following:
    - **Control 1.1**: The secret key is not encrypted so there are not enough data protection measures in place.
    - **Control 1.2**: The application does not have proper logging and monitoring mechanisms in place to detect and respond to security incidents.
    - **Control 1.3**: We do test the application for vulnerabilities but we do not simulate actions of an attacker to identify potential security weaknesses.
    - **Control 1.4**: We do not prevent or limit the impact of malware or unauthorized software on the application.


- **Q2.3 (optional)**: The linter from question 1.3 is a good start. It is only executed in your pipeline. But what if you would also integrate it directly in your local development environment (e.g. IDE)? Can you do the linting before you commit? Describe your solution and implement it in your (local) pipeline.
      
     **Answer**: To integrate the linter in the local development environment, we can use the extension in the IDE for `Flake8`. This way, the linter will run automatically in the IDE and show any errors or warnings in the code when opening or saving a file. So linting will always be done several times before committing the code to the repository.
