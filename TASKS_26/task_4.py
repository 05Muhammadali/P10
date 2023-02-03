from pytube import YouTube

link = input("Send yourube video link:")
video = YouTube(link)
quality = input("Quality video: (High/Low)")
result = None
if quality == "High":
    result = video.streams.get_highest_resolution()
if quality == "Low":
    result = video.streams.get_lowest_resolution()

result.download()
