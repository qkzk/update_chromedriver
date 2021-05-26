"""
title:  Automatically update ChromeDriver
author: qkzk
date:   2021/05/26
"""

import requests
import zipfile

URL_FILE = "https://chromedriver.storage.googleapis.com/"
FILE_NAME = "chromedriver_linux64.zip"
DEST_PATH = "/home/quentin/Downloads/chromedriver/"
DESTINATION_FOLDER = DEST_PATH + "chromedriver_linux64/"


def get_latest_version_number() -> str:
    """
    Retrieve the latest stable version of ChromeDriver from google storage API.
    """
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    version_response = requests.get(url)
    return version_response.text


def download_chrome_driver(version: str) -> str:
    """
    Check for the latest version of ChromeDriver and download it.
    Returns the full path of the downloaded file.
    """

    file = requests.get(URL_FILE + version + "/" + FILE_NAME)
    with open(DEST_PATH + FILE_NAME, "wb") as zipped_content:
        zipped_content.write(file.content)

    return DEST_PATH + FILE_NAME


def unzip_file(zipped_file: str, destination: str):
    """
    Extract the zipped file to its destination
    """
    with zipfile.ZipFile(zipped_file, "r") as zip_ref:
        zip_ref.extractall(destination)


def main():
    """Drive the application"""
    version = get_latest_version_number()
    downloaded_file = download_chrome_driver(version)
    unzip_file(downloaded_file, DESTINATION_FOLDER)
    print(
        f"Downloaded and unzipped ChromeDriver version {version} to {DESTINATION_FOLDER}"
    )


if __name__ == "__main__":
    main()
