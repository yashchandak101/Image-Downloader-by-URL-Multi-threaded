import time
from ImageDownloader import ImageDownloaderByUrl  
import threading

start = time.perf_counter()

if __name__ == "__main__":
    print(f"Thread Name = {threading.current_thread().name} and Thread Number = {threading.get_ident()}")
    

    urls = [
        "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
        "https://images.unsplash.com/photo-1519337265831-281ec6cc8514",
        "https://images.unsplash.com/photo-1497294815431-9365093b7331",
        "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05",
        "https://images.unsplash.com/photo-1526045612212-70caf35c14df",   
        "https://images.unsplash.com/photo-1516116216624-53e697fedbea",
        "https://images.unsplash.com/photo-1445979323117-80453f573b71",
        "https://images.unsplash.com/photo-1521747116042-5a810fda9664",
        
    ]
    
    threads = []
    for url in urls:
        thread = ImageDownloaderByUrl(url)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        
    finish = time.perf_counter()
    print(f"Time taken = {round(finish - start, 2)} seconds")