import os
from datetime import datetime
from dotenv import load_dotenv
from external_api.GitHubAPI import GitHubAPI

# Скрипт для теста покупки товара на сайте saucedemo.com
def test_actions_with_repo():

    load_dotenv()

    name_os: str = os.getenv('GITHUB_REPOSITORY')
    test_name_repository = name_os + datetime.now().strftime('%H%M%S')

    #Создание подключения
    apiGitHub = GitHubAPI()

    #Создать репозиторий
    print(f'Создание репозитория {test_name_repository}')
    new_repo_url = apiGitHub.create_repository(test_name_repository)

    #Проверить создание нового репозитория
    isRepoCreated = apiGitHub.get_all_repositories(test_name_repository)
    assert isRepoCreated, 'Ошибка: репозиторий не создан'

    print(f'Новый репозиторий {test_name_repository} успешно создан,\nurl: {new_repo_url}')

    #Удалить созданные репозиторий
    print(f'Удаление репозитория {test_name_repository}')
    apiGitHub.delete_repository(test_name_repository)    

    #Проверить, что репозиторий отсутствует в списке
    isRepoCreated = apiGitHub.get_all_repositories(test_name_repository)
    assert not isRepoCreated, 'Ошибка: репозиторий не был удалён'

    print(f'Репозиторий {test_name_repository} удалён')

    # Закрыть соединение
    del apiGitHub
