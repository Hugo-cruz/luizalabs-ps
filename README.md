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
This project was made based on [MVC](https://pt.wikipedia.org/wiki/MVC) pattern. This pattern was choosen to make it easy to maintain or to scale. we used a the <i>model.py</i> file, all data handling code is


## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)