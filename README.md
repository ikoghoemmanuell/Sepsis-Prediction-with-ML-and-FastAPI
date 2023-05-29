# Machine Learning API using FastAPI
Develop a Machine Learning API (Application Programming Interface) using FastAPI.

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
![Python](https://img.shields.io/badge/python-3.9-blue.svg)

## Introduction

In this project, Icreate an API that might be requested to interact with a ML model. This enables individuals and organizations keep their model architecture secret or to make their model available to users already having an API. By creating an API, and deploying it, a model can receive request using the internet protocol as presented by the illustration below.

![API illustration](https://lh3.googleusercontent.com/-qVJ4ZsbjsmH6CnYbojsAR4ImyHV8yxsFVinunH-pX7VCapGvufcXiPak6YVKIrj9ZdiCHwK5UFtQW8yuU5t83pz6fbqN1F2p74OWuT5dObCPnTBuCYr_P1mUg8arbP0WuEt7j_A)

**Source** : *The benefits of Machine Learning APIs - UbiOps*

## Description

<!-- 
[FastAPI](https://fastapi.tiangolo.com/) # 
-->

There is  a minimal API demo with [FastAPI](https://fastapi.tiangolo.com/), this will make sure that everything works correctly. Then, I will then create my own API, this will allow you to interact with a Machine Learning model, that is:
- Pass data through a request;
- Get the data in using the API;
- Apply the necessary processing;
- Submit the processed data to the ML model to make the predictions;
- Process the predictions obtained and return them as the API's response ot the input request.

## Importance of Project  
The dataset used contains a list of patients in a hospital and their attributes and whether the patient is positive for Sepssis or not. 

Sepsis is a severe and potentially life-threatening condition that occurs when the body's response to an infection triggers widespread inflammation. It is often referred to as blood poisoning.

Sepsis can develop when the immune system releases chemicals into the bloodstream to combat an infection but instead causes widespread inflammation throughout the body. 
The aim of this project is to explore the various factors that can cause sepsis in order to predict the occurence of sepsis.


Predicting sepsis is important because early recognition and intervention can significantly improve patient outcomes. Sepsis can progress rapidly and become life-threatening within a short period. By identifying patients who are at risk of developing sepsis, healthcare providers can initiate timely treatment and interventions to prevent the condition from worsening.


# Dataset Description -

The provided data is a modified version of a publicly available data source, and is subject to copyright.

### Donor of database: 
                          The Johns Hopkins University
                          Johns Hopkins Road
                          Laurel, MD 20707
                          (301) 953-6231

### Licence agreement: 

The dataset can only be used for the purpose of this assignment. Sharing or distributing this data or using this data for any other commercial or non-commercial purposes is prohibited.


### Data Fields

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|                                                                                  
| M11     | Attribute 6    |  Body mass index (weight in kg/(height in m)^2|
| BD2             | Attribute 7     |   Blood Work Result-4 (mu U/ml)|
| Age              | Attribute 8      |    patients age  (years)|
| Insurance | N/A     | If a patient holds a valid insurance card|
| Sepssis                 | Target           | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |



### Missing Attribute Values: Yes

## Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol ` ; ` but you may manually execute them one after another.

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

    <!-- - Salary prediction

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





## Contributing

Feel free to make a PR or report an issue 😃.

Oh, one more thing, please do not forget to put a description when you make your PR 🙂.

## Author

- [Gilbert Botchway](https://www.linkedin.com/in/gilbert-botchway/)
