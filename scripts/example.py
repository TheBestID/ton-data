from create_metadata import create_metadata_for_vacancy

company_name = 'Yandex'
vacancy_name = 'SWE intern'
ya_logo = 'https://raw.githubusercontent.com/TheBestID/ton-contracts/main/images/data/Yandex_logo.jpeg'

wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
applicant_wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
referral_wallet = "kQBf4BVi8IQ5iILFqsr0WHnyg1VRgZRBbjBv_ji5jc6Urpqq"
vacancy_id = 0

create_metadata_for_vacancy(
    company_name, vacancy_name, ya_logo, wallet, wallet, wallet, vacancy_id)
