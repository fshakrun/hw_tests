import pytest
from ya_api import \
    create_folder, \
    check_folder_name

class Test_Main:

    def test_success_create_folder(self):
        print('\n' + 'Папка создана успешно')
        assert create_folder('Test_Folder').status_code == 201

    def test_success_check_folder(self):
        print('\n' + 'Ищем папку')
        assert check_folder_name('Test_Folder').status_code == 200

    def test_failed_create_folder(self):
        print('\n' + 'Что-то пошло не так')
        assert create_folder('Test_Folder').status_code == 409

    def test_failed_check_folder(self):
        print('\n' + 'Папки не найдено')
        assert check_folder_name('Invalid_Folder').status_code == 404