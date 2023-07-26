# newshint
official newshint website  repo

## Prerequisites
- Python `3.9x`
- pip
- venv


## Create virtual environment 

- clone `myenv` repo from [pj8912/myenv](https://github.com/pj8912/myenv.git)
- setup `myenv` in your environment to easily create virtual environments for your python projects
```
$ myenv
```


## Installation

- Clone Repo

```
git clone https:github.com/Newshint/newshint.git
```

- Create `myenv`
    - ` myenv`
    - Activate `myenv`
        - `source myenv/bin/activate`


- Install requirements

```
pip install -r requirements.txt
```
- add `debug=True` inside `app.run()` in your `app.py` file:
    - `app.run(debug=True)`

- run
```
python app.py
```