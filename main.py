import requests
from pytube import YouTube


def Download(lnk):
    youtubeObject = YouTube(lnk)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except Exception as e:
        print(f"An error has occurred: {e}")
    print("Download is completed successfully")


def check_url(tubeurl):
    pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
    request = requests.get(tubeurl, timeout=20)
    return False if pattern in request.text else True


if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=OFrMD1iCCNQ"
    if check_url(link):
        Download(link)
