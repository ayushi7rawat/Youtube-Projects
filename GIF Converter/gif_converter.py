'''
GIF Converter using Python
Author: Ayushi Rawat
'''

# import the necessary module
from moviepy.editor import *

# load the video
clip = VideoFileClip("my_video.mp4")

# getting only 3 first seconds from video
clip = clip.subclip(0, 3)

# save the video clip as gif
clip.write_gif("mygif.gif")