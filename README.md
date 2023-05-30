# notemaua-mss-withdraw 📚💻

Microservice for withdraws and notebooks management in NoteMaua project for Instituto Mauá de Tecnologia.

## The Project 📝

### Introduction and Objectives ⁉

The project aims to create a system that facilitates the process of laptop withdrawal and devolution for Instituto Mauá de Tecnologia. It provides a platform for students and staff members to manage the borrowing and return of laptops.

### Clean Architecture 🧼🏰

The purpose of the project is to implement a Clean Architecture for microservices using AWS Lambda. Clean Architecture follows the principles of SOLID and emphasizes structuring the code in layers, each with a specific responsibility. This architectural approach ensures a modular and maintainable codebase.

To develop this project, we have utilized the [clean_mss_template](https://github.com/Maua-Dev/clean_mss_template), a template specifically designed for creating microservices with clean architecture.

## Installation 👩‍💻

Clone the repository using the template.

### Create a virtual environment in Python (only for the first time)

###### Windows

    python -m venv venv

###### Linux

    virtualenv -p python3.9 venv

### Activate the virtual environment

###### Windows:

    venv\Scripts\activate

###### Linux:

    source venv/bin/activate

### Install the requirements

    pip install -r requirements-dev.txt

### Run the tests

    pytest

### To run local set .env file

    STAGE = TEST


## Contributors 💰🤝💰

- Luigi Trevisan - [LuigiTrevisan](https://github.com/LuigiTrevisan)
- Rafael Bidetti - [Bidetti](https://github.com/Bidetti)
- Dimitri Zenaro - [Diimy](https://github.com/Diimy)

## Especial Thanks 🙏

- [Mauá Institute of Technology](https://www.maua.br/)
- [Dev. Community Mauá](https://www.instagram.com/devcommunitymaua/)
