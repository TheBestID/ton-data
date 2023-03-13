
from generate_json import generate_jsons_for_vacancy
from push_to_git import load_data_to_git


def create_metadata_for_vacancy(company_name, vacancy_name, company_logo, company_wallet, applicant_wallet, referral_wallet, vacancy_id):
    generate_jsons_for_vacancy(company_name, vacancy_name, company_logo,
                               company_wallet, applicant_wallet, referral_wallet, vacancy_id)
    load_data_to_git(vacancy_id)
    print(f"Data for vacancy {vacancy_id} is generated.")


