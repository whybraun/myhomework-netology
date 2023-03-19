import requests

class YaUploader:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {"Authorization": f"OAuth {self.token}"}
        
    def upload_file(self, local_path, remote_path):
        url = f"{self.api_url}/resources/upload?path={remote_path}&overwrite=true"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            href = response.json()["href"]
            with open(local_path, "rb") as f:
                response = requests.put(href, data=f)
                if response.status_code == 201:
                    return True
        return False

if __name__ == '__main__':
    path_to_file = 'путь ПК'
    remote_path = 'путь Я.Диск'
    token = 'Токен'
    uploader = YaUploader(token)
    result = uploader.upload_file(path_to_file, remote_path)
    if result:
        print("Файл успешно загружен на Яндекс.Диск")
    else:
        print("Не удалось загрузить файл на Яндекс.Диск")
