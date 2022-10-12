

from pytube import YouTube
c = 0
link = open('links.txt','r')
for i in link: 
    c=c+1
    try: 
          
        # object creation using YouTube
        # which was imported in the beginning 
       yt = YouTube(i) 
    except: 
          
        #to handle exception
        print("Connection Error") 
 

	
    try:
       yt.streams.filter(progressive = True, 
       file_extension = "mp4").first().download(output_path = "saving path", 
       filename = str(c))
       
       print(i)
       print('Task Completed!')


    except: 
          
        #to handle exception
        print("Connection Error") 
