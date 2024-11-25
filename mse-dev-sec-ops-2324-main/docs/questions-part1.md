# Questions - Part 1

## Unit tests - Secret keys - Linter - optimized CI/CD pipeline

- **Q1.1**: Provide additional unit tests to ensure that wrong input (type, values, ...) doesn't crash the application, but gets intercepted and produce a controlled error. It is possible that you have also to adjust slightly the application
  
    **Answer**: (See [test_api.py](../src/tests/test_api.py)) The tests check for invalid input types, invalid input values, and missing input values. The application has been adjusted to handle these cases and produce controlled errors.

- **Q1.2**: The secret key for flask is hard coded. Is this good practice? What are the dangers? How could this be fixed?
    
    **Answer**: No, it is not a good practice. The danger is that the key is exposed in the code and can be easily accessed by anyone who has access to the code. This can be fixed by using environment variables to store the secret key and accessing it in the code. This way, the secret key is not exposed in the code and is only accessible to the application which also helps in key rotation when secrets need to be changed.

- **Q1.3**: Give a short description of *Linter*. Integrate a basic linter like [Flake8](https://flake8.pycqa.org/en/latest/) or [Ruff](https://github.com/astral-sh/ruff) in the existing CI/CD pipeline
    
    **Answer**: A linter is a tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs. Linters can be used to enforce coding standards and to ensure that the code is clean and readable. They can also help to identify potential security vulnerabilities and performance issues. Linters are commonly used in software development to improve code quality and to catch errors early in the development process. We chose to integrate Flake8 in the existing [CI/CD pipeline](../.gitlab-ci.yml).

- **Q1.4 (optional)**: The run of the current CI/CD pipeline takes some time. Especially the time to setup the docker with the update and installation of all the dependencies is quite time consuming compared to the real testing time. Do you see any alternatives to speed up this process? Describe and try to implement it in your pipeline.

    **Answer**: One alternative to speed up the CI/CD pipeline is to save a docker image to the container registry with all required packages installed and a proper image that already conains python tools. While triggering the pipeline, the image can be pulled from the registry and used to run both liter and tests. Another alternative is to cache the dependencies so we can reuse them in subsequent pipeline runs. 