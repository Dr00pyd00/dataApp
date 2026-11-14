
# Very simple python AP 

It is a simple api write in Python  with uvicorn.   
It use `Data` items thats juste contain:
- id (int)
- text (str)
- crated_at (str) 

## Installation 

```bash
mkdir ~/dataApp
cd ~/dataApp
git clone https://github.com/Dr00pyd00/dataApp.git . 

# make sur uv is installed
uv sync
uv run uvicorn main:app --reload
```

## Usage 

`BASE_URL` = `http://127.0.0.1/`

#### Routes:

- `GET` -> `http://127.0.0.1/` : test root 

- `GET` -> `http://127.0.0.1/data` : see all data
- `GET` -> `http://127.0.0.1/data/<int>` : detail of one data by ID
- `POST` -> `http://127.0.0.1/data` : create new data 
- `DELETE` -> `http://127.0.0.1/data/<int>` : delete data by ID 
- `PUT` -> `http://127.0.0.1/data/<int>` : update data by ID 



