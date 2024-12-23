# Flask Boilerplate
## Install/setup
### WARNING: before using please note that this project depends on ```uv```
To  setup a new project using this simply run
```git clone https://github.com/avycado13/flask-boilerplate```
and
```uv sync```

## Files breakdown
### `app/`
#### `models.py`
This is where all models including auth models are defined.
#### `extensions.py`
All extensions are defined here to avoid circular importing.
#### `__init__.py`
The main backbone of the application factor resides here.
You can register all your views and blueprints here.
