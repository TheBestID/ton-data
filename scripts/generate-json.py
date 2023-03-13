#!/usr/bin/python
import json
from datetime import date
from push_to_git import load_data_to_git
""" 
Given following arguments:
company_logo -- link to logo, such as https://raw.githubusercontent.com/TheBestID/ton-contracts/main/collection/data/mfti2.jpeg 
company_name, vacancy_name
Three wallets -- company_wallet, applicant_wallet, referral_wallet
"""

company_name = 'Yandex'
vacancy_name = 'SWE intern'
ya_logo = 'https://raw.githubusercontent.com/TheBestID/ton-contracts/main/collection/data/mfti2.jpeg'

wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
applicant_wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
referral_wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
vacancy_id = 0

# description = "Hired " + vacancy_name + " at " + company_name


def generate_jsons_for_vacancy(company_name, vacancy_name, company_logo, company_wallet, applicant_wallet, referral_wallet, vacancy_id):
    description = f"Hired {vacancy_name} at {company_name}"
    name_for_vacancy = f"Vacancy {vacancy_id}"
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
                "trait_type": "Vacancy ID",
                "value": f'{vacancy_id}'
            },
        ],
        "description": f'{description}',
        "image": f'{company_logo}',
        "name": f'{name_for_vacancy}'
    }

    roles = ['Company', 'Referral', 'Applicant']

    for role in roles:
        current = template.copy()
        current["attributes"][4]["value"] = role
        try:
            with open(f"{role}-{vacancy_id}.json", "w") as outfile:
                json.dump(current, outfile)
            print(f"Successfully generated {role}-{vacancy_id}.json")
        except:
            print(f"Failed to generate {role}-{vacancy_id}.json")


def create_metadata_for_vacancy(company_name, vacancy_name, company_logo, company_wallet, applicant_wallet, referral_wallet, vacancy_id):
    generate_jsons_for_vacancy(company_name, vacancy_name, company_logo,
                               company_wallet, applicant_wallet, referral_wallet, vacancy_id)
    load_data_to_git(vacancy_id)
    print(f"Data for vacancy {vacancy_id} is generated.")


create_metadata_for_vacancy('Yandex', 'SWE intern',
                           ya_logo, wallet, wallet, wallet, vacancy_id)
