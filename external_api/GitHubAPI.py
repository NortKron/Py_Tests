import os
from github import Auth
from github import Github

class GitHubAPI():
   github_client = None
   github_user = None

   def __init__(self):
      github_login = os.getenv('GITHUB_USER')
      github_token = os.getenv('GITHUB_TOKEN')

      auth = Auth.Token(github_token)
      self.github_client = Github(auth=auth)
      self.github_user = self.github_client.get_user()

   def __del__(self):
        self.github_client.close()

   def get_all_repositories(self, repo_name: str) -> bool:
      list_repositories = self.github_user.get_repos()
      
      repo_search = next((repo for repo in list_repositories if repo.name == repo_name), None)
      return repo_search
   
   def create_repository(self, repo_name: str):
      # Создание нового репозитория
      description = 'Description of the repository'
      
      # Сделать репозиторий публичным или приватным
      private = False

      repo = self.github_user.create_repo(
         name=repo_name,
         description=description,
         private=private,
         has_issues=True,
         has_wiki=True,
         has_downloads=True
      )

      return repo.html_url

   def delete_repository(self, repo_name: str):
      try:
         repo = self.github_user.get_repo(repo_name)
         repo.delete()
      except Exception as e:
         print(f"Ошибка при удалении репозитория: {e}")   
