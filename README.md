<img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Backend Developer - Luiza Labs Application

This project was made for the applications of the Backend Developer position at Luiza Labs. It's based on [this document](https://docs.google.com/document/d/14MxNO1gCjBdEEM8cSMuU_Ci2R4aB6vSWpH3IViLrG84/edit).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install everything that is needed by this app.

```bash
pip -r install requirements.txt
```

## Running on Docker
```docker
docker build --tag python-docker .
docker run --publish 5000:5000 python-docker
```

## Patterns
This project was made based on [MVC](https://pt.wikipedia.org/wiki/MVC) pattern. This pattern was choosen to make it easy to maintain or to scale. we used a the <i>model.py</i> file to handle all the data on the app, so it's easier to change to another approach of data handling (MySQL, for example) and keep the method's names to avoid crashing. 

We choose MVC also for a posible insertion of a frontend, for this, it's just a matter of insert some html on the <i>views.py</i> file.

## File System
To model the graph described in the challenge, we used a adjacency list. As we are using python, we took advantage of it's dict implementation, in whice we can acess data on O(1) time complexity. It's been implemented like this:
```python
graph = {
    "person1":["person2","person3"],
    "person2":["person1"],
    "person3":["person1"]
}
```

As we are dealing with a specific problem, we are not modeling a full forest, with all graph properties, we are taking advantage of some specifics of this problem:
- The keys are persons name, so we can deal with it in alphabetical order
- We are only dealing with friends, so they cannot be many (a person cannot have 10ˆ9 friends, for example)

Knowing this, we keep the people's records among several files, each on for a lettter of the alphabet, so we can access a large variety of people in RAM. To know in which file are kept each letter, we have a <i>index.json</i> file with all file's name mapped (it can be used to scale the project too, only changing to another service, like a KVS).

The basic acces is done by:
- Get the first letter of the name
- Access the index
- Select the file name
- Load the file pointed by that name in RAM as a json
- Access the  friend's list

The worst case is accessed by O(26), and the number of acces can be improved by ordering the friend's list.

## Author
Hugo Fellipe 
