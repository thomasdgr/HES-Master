
# CI/CD and SSDLC labs (TSM CyberSec)

This is a simple calculator application using Flask. The application is a simple calculator that can perform addition, subtraction, multiplication, and division.

## Environment setup and usage

For the environment setup, the following steps are necessary:

1. Install Python and [PDM (package manager)](https://pdm-project.org/latest/)
1. Install the required packages with `pdm install` --> The pyproject.toml file contains the required packages
1. Start the development server with `pdm run flask`

The started server can be reached on the localhost (127.0.0.1) on port 5000. This can be configured if desired.

## Usage and routes of the demo app

The following table shows the different routes of the REST API:
| route | GET parameters | function |
| --- | --- | --- |
| / | n/a | Welcome page |
| /login | n/a | Login page (only the username is used for the moment) |
| /help | n/a | Help page |
| /inc | x | increments the value x by 1 |
| /add | x, y | executes x+y |
| /mul | x, y | executes x*y |
| /div | x, y | executes x/y |

### Examples

Here some usage examples

- <http://127.0.0.1:5000/inc?x=5> will take the value of x=5 and increments it
- <http://127.0.0.1:5000/mul?x=3&y=7> will take the value of x=3 and y=7 and executes x\*y (3\*7=21)
- <http://127.0.0.1:5000/> brings you to the landing page
- <http://127.0.0.1:5000/login> brings you to the login page
