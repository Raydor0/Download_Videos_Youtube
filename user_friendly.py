import pytube

video_list = []
count = 0
band = True

print("Enter URLs (Terminate by 'STOP')")


""" ----------------------- Confirm if starts with 'https://www.youtube.com/' ----------------------- """
def confirmarBeggining(url):
    global band
    confirm = ''
    lenght = len(url)
    if band:
        for x, letras in enumerate(url):
            s = letras
            confirm += s
            
    return confirm



""" ----------------------- Main ----------------------- """
while True:
    url = input("")
    
    TheBeginning = confirmarBeggining(url).lower()
    Beginning = TheBeginning[0:24]

    if Beginning != 'https://www.youtube.com/':
        print("The url does not contain 'https://' at the Beggining")
        continue
    count = count + 1

    if url == 'STOP':
        break
    video_list.append(url)


for x, url in enumerate(video_list):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(22)
    print(f"Downloading Video {x}...")
    stream.download()
    print("Done")




