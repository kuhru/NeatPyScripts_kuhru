import webbrowser
import os
import time


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
# my default was IE ancient for some reason, so i registered chrome.exe under chrome

ct = 0
cur = 0
location = input("Enter the directory path: ")

for r, d, f in os.walk(location):
    for file in f:
        if ct < 36:
            content = "file:///" + os.path.join(location, file)
            # print(content)
            webbrowser.get('chrome').open(url=content, new=2, autoraise=True)
            # keeps opening the images in new tabs of the same window
            time.sleep(0.25)
            ct = ct + 1
            cur = cur + 1
        if ct == 36:
            # making sure not more than 36 images are opened at once by the program
            # ct decides how many images are opened.
            print("\nNumber of Files Already Processed: " + str(cur) +" \nFiles Remaining to be Processed: " + (str(len(f) - cur)))
            whatnow = str(input("Press 1 to continue\nPress 2 to stop execution\n"))
            if whatnow == '1' or whatnow == '':
                ct = 0
            elif whatnow == '2' or whatnow.lower() == 'stop':
                break
            print('_____________________')
    print()
    if cur == len(f):
        print("All files processed in: " + location)
    else:
        print(str(len(f) - cur) + " files still remaining in " + location)
    break
