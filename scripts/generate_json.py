#!/usr/bin/python
import json
from datetime import date
import os
""" 
Given following arguments:
company_logo -- link to logo, such as https://raw.githubusercontent.com/TheBestID/ton-contracts/main/collection/data/mfti2.jpeg 
company_name, vacancy_name
Three wallets -- company_wallet, applicant_wallet, referral_wallet
"""


def create_data_directory_if_not_exist():
    data_path = os.path.relpath(r"../data/", os.path.dirname(__file__))
    if not os.path.exists(data_path):
        os.makedirs(data_path)
        print("Successfully created data directory")
    else:
        print("Data directory already exists")


def generate_jsons_for_vacancy(company_name, vacancy_name, company_logo, company_wallet, applicant_wallet, referral_wallet, vacancy_id, hiring_process_start_date):
    name_for_vacancy = f"Vacancy {vacancy_name} for {company_name}"
    template = {
        "attributes": [
            {
                "trait_type": "Company",
                "value": f'{company_name}'
            },
            {
                "trait_type": "Company account",
                "value": f'{company_wallet}'
            },
            {
                "trait_type": "Applicant account",
                "value": f'{applicant_wallet}'
            },
            {
                "trait_type": "Referral account",
                "value": f'{referral_wallet}'
            },
            {
                "trait_type": "Role",
                "value": "Sample role"
            },
            {
                "trait_type": "Apply date",
                "value": f'{date.today()}'
            },
            {
                "trait_type": "Duration of hiring",
                "value": f'{(date.today() - hiring_process_start_date).days}'
            },
            {
                "trait_type": "Vacancy ID",
                "value": f'{vacancy_id}'
            },
        ],
        "description": f"Hired {vacancy_name} at {company_name}, powered by SoulDev.",
        "image": f'{company_logo}',
        "name": f'{name_for_vacancy}'
    }

    roles = ['Company', 'Referral', 'Applicant']
    create_data_directory_if_not_exist()
    data_path = os.path.relpath(r"../data/", os.path.dirname(__file__))
    for role in roles:
        current = template.copy()
        current["attributes"][4]["value"] = role
        with open(data_path + f"/{role}-{vacancy_id}.json", "w") as outfile:
            json.dump(current, outfile)
        print(f"Successfully generated {role}-{vacancy_id}.json")
