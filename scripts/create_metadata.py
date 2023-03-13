
from generate_json import generate_jsons_for_vacancy
from push_to_git import load_data_to_git

company_name = 'Yandex'
vacancy_name = 'SWE intern'
ya_logo = 'https://raw.githubusercontent.com/TheBestID/ton-contracts/main/collection/data/mfti2.jpeg'

wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
applicant_wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
referral_wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
vacancy_id = 0


def create_metadata_for_vacancy(company_name, vacancy_name, company_logo, company_wallet, applicant_wallet, referral_wallet, vacancy_id):
    generate_jsons_for_vacancy(company_name, vacancy_name, company_logo,
                               company_wallet, applicant_wallet, referral_wallet, vacancy_id)
    load_data_to_git(vacancy_id)
    print(f"Data for vacancy {vacancy_id} is generated.")


create_metadata_for_vacancy('Yandex', 'SWE intern',
                           ya_logo, wallet, wallet, wallet, vacancy_id)
