# Image Downloader by URL (Multi-threaded)
## Description
This Python project is a multi-threaded image downloader that fetches images from a list of URLs and saves them locally. Each download runs in a separate thread, allowing for faster, concurrent downloading. It uses the requests library to handle HTTP requests and the threading library to manage multiple threads efficiently.

## Features
Multi-threaded: Each image download runs in a separate thread for improved performance.
Unique File Naming: Images are saved with unique names generated using UUIDs.
Directory Handling: Images are saved in an "images" directory, which is created automatically if it doesn’t exist.
Error Handling: The program includes error handling for HTTP errors and network issues.
