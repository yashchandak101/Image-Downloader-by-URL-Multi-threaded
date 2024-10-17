import threading
import requests
import uuid


class ImageDownloaderByUrl(threading.Thread):
    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)

    def run(self):
        print(f"Thread Name = {threading.current_thread().name} and Thread Number = {threading.get_ident()}")
        
        try:

            response = requests.get(self.url)
            response.raise_for_status() 



            image_name = f"images/{str(uuid.uuid4())}.jpg"
            with open(image_name, "wb") as image_file:
                image_file.write(response.content)
                print(f"Image downloaded and saved as {image_name}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download image from {self.url}. Error: {e}")
