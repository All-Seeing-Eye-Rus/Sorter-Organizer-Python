from cgitb import handler
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler
import re

class Handler (FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            moving(filename, folder_html, "html") 
            #Track files according to their format. 
            #1st parameter - file name, 
            #2nd parameter - destination folder, 
            #3rd parameter - file format (the one after the dot ".txt", ".py"...)
            moving(filename, folder_css, "css")     #example
            moving(filename, folder_img, "jpg", "png", "gif", "jpeg")   #example
            moving(filename, folder_text, "doc", "docx", "txt")     #example
            moving(filename, folder_py, "py")   #example
            

def moving(filename, folder, path1=True, path2=None, path3=None, path4=None, path5=None):
    exception = filename.split('.')
    file = folder_track + '/' + filename

    if os.path.exists(folder + '/' + filename): #Creating copies if such a file already exists in the specified directory
        if os.path.exists(folder + '/' + 'Copy(1)-'+filename):
            num = ['1']
            backapFilename = filename
            while os.path.exists(folder + '/' + f'Copy({num[0]})-' + backapFilename) != False:
                s = f'Copy({num[0]})-' + backapFilename
                sBack = s.partition(')')[0]
                numFind = re.findall('(\d+)', sBack)
                num[0] = numFind[-1]
                maxNum = str(int(num[0]) + 1)
                filename = s.replace(num[0], maxNum)
                num[0] = maxNum
        else: filename = 'Copy(1)-' + filename
 

    new_path = folder + '/' + filename

    if len(exception) > 1 and (exception[1].lower() == path1) or len(exception) > 1 and (exception[1].lower() == path2) or len(exception) > 1 and (exception[1].lower() == path3) or len(exception) > 1 and (exception[1].lower() == path4) or len(exception) > 1 and (exception[1].lower() == path5):
        os.rename(file, new_path) 


folder_track = '/User/folderSorter' #Path to the folder where the files will be sorted from
folder_html = folder_track + '/web/html' #The path to the folder where the sorted files will be transferred by category files
folder_img =  folder_track + '/img' #example
folder_css =  folder_track + '/web/css' #example
folder_text =  folder_track + '/text' #example
folder_py =  folder_track + '/python' #example

handler = Handler()
observer = Observer() 
observer.schedule(handler, folder_track, recursive=True)
observer.start()

try:
    while(True): 
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
