# 0x00. Personal data

## Resources
Read or watch:
- [What Is PII, non-PII, and Personal Data?](https://www.giac.org/paper/gsec/2180/personally-identifiable-information-pii-non-pii-personal-data/105824)
- [Logging Documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt Package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://realpython.com/python-logging/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/env python3`
- A `README.md` file is mandatory at the root of the project folder
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- File lengths will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method
- All functions should be type annotated
