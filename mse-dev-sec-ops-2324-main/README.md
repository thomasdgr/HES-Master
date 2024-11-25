

# CI/CD and SSDLC labs (TSM CyberSec)

On this page you'll find the lab(s) for the TSM CyberSec course. 

## Organization

The labs is finally only one lab in which you build a CI/CD pipeline with the main focus on security add-ons. This will include:

* unit tests
* coverage tests
* SAST integration
* DAST integration
* data leakage prevention
* ... and much more

The lab will be performed in groups of two students.

## Evaluation

The groups (pair) will be evaluated.

Any work is stored by the groups in their own Git repo, in the **`main` branch**. This contains:

* Code
* CI/CD pipeline
* Documentation

The documentation contains the answers to all the questions asked. It is a rolling lab, which means, that additional questions will come each week. Use the question files (e.g. `docs/question-part1.md`) for your answers! (--> Overall duration of the lab approximately 5 weeks)

### Grading

How is the lab graded?

- If you answer the questions correctly, you have the grade 5.0
- To get more than 5.0, you must for example :
    - propose an original solution
    - deepen one or more themes
    - answer the optional questions of the labs (if there are any)


### Submission

All your work must be terminated and commit to your *group repo* at latest **24.04.2024**

## Preparation

You must (in the pair) fork the Git Repo that contains an example Web-API application with a minimalistic CI/CD pipeline. This repo will build the starting point for all your upcoming lab tasks. These preparation steps will be done together in class


### Tasks

1. Fork this git repo here https://gitlab.forge.hefr.ch/devsecops/mse-dev-sec-ops-2324
    - Get some inspiration [here](https://concurp.pages.forge.hefr.ch/2022-2023/website/lab00/) how to fork a repo
2. Give **Maintainer** access to your colleague in your group
3. Give **Developer** access to the professor (@michael.maeder)
4. Clone your newly created repo to your local machine and `cd` into the directory
5. Set the `upstream` to the main repo to get any updates
   * `git remote add upstream git@gitlab.forge.hefr.ch:devsecops/mse-dev-sec-ops-2324.git`
6. `git pull upstream main` will update your fork repo with the latest changes from the main repo


# Lab envrionment setup

In the first part, the lab will be mainly a setup of the environment for everybody to ensure that you can work correctly. The basics will be shown directly in the course.

Currently the following directory structure exists:

* **docs**: place for you to put your documentation, explanations, answers, graphics, etc
* **src**: a minimalistic web application (written in Python 3.x) that can perform the following calculations:
    * addition / subtraction
    * multiplication
    * division
  * **tests**: test comes here (e.g. unit tests, coverage, ...)

## Analysis of the application and the existing pipeline

You must understand the application, how it works, the basics of Flask (as web platform) and of course the automation processes (CI/CD) for testing, building, etc. the application.

## Usage of the API

*see README.md in the `src` directory*

## Basic pipeline

The provided basic pipeline description `.gitlab-ci.yml` is **not optimized at all**. It works in a *shaky* way and does the following tasks:

- run the unit tests (described in `src/tests`)
- checks the test coverage
- create a test and coverage report in HTML format, which is then accessible through **your** gitlab pages (e.g. `https://devsecops.pages.forge.hefr.ch/mse-dev-sec-ops-2223/`)


## The questions

The questions for all the parts can be found in the [questions-partX.md files](./docs/) file in the docs directory. You can write your answers directly into these files if you wish.


# Resources
* [TSM Cybersecurity Moodle](https://moodle.msengineering.ch/course/view.php?id=2376)
* [Lecture notes](https://heia-fr-maeder.github.io/mse_cybersec)
* [Coverage report](hhttps://mse-dev-sec-ops-2324-devsecops-mse-fd7bb329cbf2fd39e71840cb4686.pages.forge.hefr.ch/)
* [Short Intro to CI/CD](https://www.youtube.com/watch?v=l5705U8s_nQ&t=358s)
* [How to make your code shine with Gitlab CI pipelines](https://medium.com/semantixbr/how-to-make-your-code-shine-with-gitlab-ci-pipelines-48ade99192d1)
