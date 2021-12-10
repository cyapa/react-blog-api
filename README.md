# API for the **[React Blog App](https://github.com/cyapa/react-blog)** by Chathura Yapa


## API Domains

- Blog domain
    - [x] Create
    - [x] Delete
    - [x] Read

- Comment domain
    - [x] Create
    - [x] Delete
    - [x] Read

- Like domain
    - [ ] Create
    - [ ] Delete
    - [ ] Read
 
- Database migration
   - [ ] Create migration shell script
   - [ ] Create migration SQLs

- Docker setup
    - [x] Basic API deployment
    - [ ] Database migration before API dpeloyment

- MakeFile setup

## How to run the API in local machine

1. Clone this repo from GitHub and from root directory run `pip install -r requirements.txt` to install the dependancies. 

    Then run `uvicorn main:app --reload` to host the API in local machine. The documentation is available on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
