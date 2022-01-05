# FastAPI Project Template

Project template for Hacarus projects using FastAPI.

### Prerequisites
- Python 3.8+
- Poetry 0.12+

Running the application

```python
poetry run uvicorn api.main:app --reload
```
```shell script
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [78703] using watchgod
INFO:     Started server process [78705]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

To see available API documentation, go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

`uvicorn` is a production ready server that supports asyncio. Here are some common commands.

```shell script
poetry run uvicorn api.main:app --port 5000   // To change the port
poetry run uvicorn api.main:app --reload      // Detect file changes and reload
poetry run uvicorn api.main:app --workers 2   // Change number of request workers
```

For additional features and technical specifications, you can visit the official [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/first-steps/).

### Directory Structure

    ├── .env                    <- Contains your environment variables
    ├── README.md               <- The top-level README for developers using this project.
    ├── api
    │   ├── routes              <- Contains all the functions for each request
    │   ├── schema              <- Schema list
    │   |   ├── response.py     <- Response models (used in OpenAPI)
    │   |   ├── request.py      <- Request models (used in validating request body)
    │   |   └── database.py     <- Declare any database models here
    │   |
    │   ├── commons             <- Common library folder.
    │   |   └── utils.py        <- Utility functions
    │   |
    │   ├── config.py           <- If you want to set config, do it here.
    │   └── server.py           <- All app initialization and pre-loadings
    │
    └── pyproject.toml     <- A configuration file to store build system requirements for Python projects.
    
 ### Application Configuration
 
 It's easy to declare environment variables using the `.env` file.
 You can add as many environment variables as you want as long as you also add the corresponding entry in `api/config.py`.
 
For example, if you have the following environment variables
 
 ```shell script
ENV_VAR1=1
OPERATING_SYSTEM=Windows
CYCLES=2.2
```

then you need to make sure to add this to the `config.py` file as such

```python
class Settings(BaseSettings):
    app_name: str = "Your project name"
    env_var1: int = 1
    operating_system: str = "Windows"
    cycles: float = 1.0
```

Pydantic automatically handles environment variable parsing.

- The configuration mapping is **CASE INSENSITIVE**.
- It is also required to put types so that pydantic can handle the correct conversion.
- The default value in `config.py` will be overwritten if an environment variable of same name is present.

### Sample API calls

For the basic API calls and FastAPI syntax, checkout `api/routes/sample.py`. This contains all the basic routing patterns as well as some request and error handling.

For a more advance example of using a response and request model, check out `api/routes/sample2.py`.