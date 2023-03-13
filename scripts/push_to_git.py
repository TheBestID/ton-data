from git import Repo

PATH_OF_GIT_REPO = r'../.git' 
COMMIT_MESSAGE = 'comment from python script'

repo = Repo(PATH_OF_GIT_REPO)
roles = ['Company', 'Referral', 'Applicant']
def git_add(rep, vacancy_id):
    for role in roles:
        rep.git.add(f'{role}-{vacancy_id}.json')
        print(f'Added {role}-{vacancy_id}.json.')

def git_commit(rep, vacancy_id):
    rep.index.commit(f"Add metadata files for vacancy {vacancy_id}.")
    print(f'\nCommited files for vacancy {vacancy_id}.')


def git_push(rep):
    origin = rep.remote(name='origin')
    origin.push()
    print('Successfully pushed.')    


def load_data_to_git(vacancy_id):
    rep = Repo(PATH_OF_GIT_REPO)
    git_add(rep, vacancy_id)
    git_commit(rep, vacancy_id)
    git_push(rep)