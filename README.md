# Machine Learning API using FastAPI

[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/your-github-username)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/your-github-username?tab=repositories)
[![View My Profile](https://img.shields.io/badge/MEDIUM-Article-purple?logo=Medium)](https://medium.com/@emmanuel.ikogho/classification-predicting-sepsis-with-machine-learning-and-fastapi-3a3d05d0b5b4)
[![Docker App](https://img.shields.io/badge/Docker-App-yellow)](https://huggingface.co/spaces/ikoghoemmanuell/Sepsis-Prediction-With-FastAPI)

Develop a Machine Learning API (Application Programming Interface) using FastAPI.

![ai(3)](https://github.com/ikoghoemmanuell/Machine-Learning-API-using-FastAPI/assets/102419217/1566fe8f-68bc-48fd-b9e0-2f8de41fd18c)

## Introduction

We will explore a comprehensive machine learning project focused on predicting sepsis using classification techniques. By leveraging FastAPI, we were able to deploy the model as a user-friendly API, enabling real-time predictions. The combination of machine learning and web development has immense potential in healthcare and can significantly contribute to early sepsis detection and patient care.

## Description

## Importance of Project  

The dataset used contains a list of patients in a hospital and their attributes and whether the patient is positive for Sepssis or not.

Sepsis is a severe and potentially life-threatening condition that occurs when the body's response to an infection triggers widespread inflammation. It is often referred to as blood poisoning.

The aim of this project is to explore the various factors that can cause sepsis in order to predict the occurence of sepsis.

Predicting sepsis is important because early recognition and intervention can significantly improve patient outcomes. Sepsis can progress rapidly and become life-threatening within a short period. By identifying patients who are at risk of developing sepsis, healthcare providers can initiate timely treatment and interventions to prevent the condition from worsening.

# Dataset Description -

The data for this project is in a csv format. The following describes the columns present in the data.

| Column Name | Target | Description                                                                   |
| ----------- | ------ | ----------------------------------------------------------------------------- |
| ID          | N/A    | Unique number to represent patient ID                                         |
| PRG         | False  | Plasma glucose                                                                |
| PL          | False  | Blood Work Result-1 (mu U/ml)                                                 |
| PR          | False  | Blood Pressure (mm Hg)                                                        |
| SK          | False  | Blood Work Result-2 (mm)                                                      |
| TS          | False  | Blood Work Result-3 (mu U/ml)                                                 |
| M11         | False  | Body mass index (weight in kg/(height in m)^2                                 |
| BD2         | False  | Blood Work Result-4 (mu U/ml)                                                 |
| Age         | False  | patients age (years)                                                          |
| Insurance   | N/A    | If a patient holds a valid insurance card                                     |
| Sepssis     | True   | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |

## Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...` follow the steps below:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

- Linux & MacOs:
  python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

The both long command-lines have a same structure, they pipe multiple commands using the symbol `;` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI

- Run the demo apps (being at the repository root):

  FastAPI:

  - Demo

        uvicorn src.demo_01.api:app --reload

    <!-- - Sepsis prediction

          uvicorn src.salary.api:app --reload  -->

  - Go to your browser at the following address, to explore the api's documentation :
    http://127.0.0.1:8000/docs

<!-- ## Screenshots

<table>
    <tr>
        <th>FastAPI</th>
        <th>FastAPI</th>
    </tr>
    <tr>
        <td><img src="./screenshots/.png"/></td>
        <td><img src="./screenshots/.png"/></td>
    </tr>
</table> -->

## Resources

Here are some ressources you would read to have a good understanding of FastAPI :

- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)

## 👏 Support

If you found this article helpful, please give it a clap or a star on GitHub!

## Author

- [Emmanuel Ikogho](https://www.linkedin.com/in/emmanuel-ikogho-6b959b24b/)
