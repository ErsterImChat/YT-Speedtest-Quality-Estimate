import speedtest
import math
# Defining Speedtest Variables

servers = []
threads = 4

YoutubeQuality = "Unknown"

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

print("Starting Download Test")
download_speed = int(s.download())/1000000
print("Download Test is done. Now starting Upload Test")
upload_speed = int(s.upload())/1000000

print(str(format((float(download_speed)), '.2f')))


print("Your Current Download Speed is: " + str(format((float(download_speed)), '.2f')))
print("Your Current Upload Speed is: " + str(format((float(download_speed)), '.2f')))
print("Now starting Youtube Quality Analysis")

download_speed = 0.754585485

if float(download_speed) < float(0.3):
        YoutubeQuality = "240p or lower"

if float(download_speed) > float(0.3):
        YoutubeQuality = "360p"

if float(download_speed) > float(1.1):
        YoutubeQuality = "480p"

if int(download_speed) > 3:
        YoutubeQuality = "720p"

if int(download_speed) > 6:
        YoutubeQuality = "1080p"

if int(download_speed) > 20:
        YoutubeQuality = "4K"




print("You should be able to watch Youtube Videos in " + str(YoutubeQuality))
