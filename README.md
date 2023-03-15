# Ton data

## Dependencies:
- `pip install gitpython`
- `pip install toncli`
- `pip install DateTime`

## Usage
1. Import `create_metadata_for_vacancy(...)` function from [create_metadata.py](https://github.com/TheBestID/ton-contracts/blob/main/scripts/create_metadata.py). 
2. Pass to this function the following arguments:
  - `company_name`, 
  - `vacancy_name`, 
  - `company_logo` (as a link to image, like in [example](https://github.com/TheBestID/ton-contracts/blob/main/scripts/example.py)), 
  - `company_wallet`, 
  - `applicant_wallet`, 
  - `referral_wallet`, 
  - `vacancy_id` (unique id, we get it from backend),
  - `hiring_process_start_date` - when hiring process started.
Of course you need to have access to this repository.
3. Here, in this repo, in [data](https://github.com/TheBestID/ton-contracts/tree/main/data) folder you will get three `.json` files, ending on vacancy_id (like `Company-0.json` for `vacancy_id == 0`). You can use them in deploying scripts.
  
P.S. Script assumes that you run your program from `/scripts` folder. If not, you should change relative `PATH_OF_GIT_REPO` in [push_to_git.py](https://github.com/TheBestID/ton-data/blob/main/scripts/push_to_git.py).  
  
