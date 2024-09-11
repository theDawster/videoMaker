import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/dawitg/Downloads/ffmpeg"

from moviepy.editor import VideoFileClip, concatenate_videoclips



clip1 =  VideoFileClip("backgroundVids/video1.mp4").subclip(0, 10)
clip2 =  VideoFileClip("backgroundVids/video1.mp4").subclip(0, 10)
clip3 =  VideoFileClip("backgroundVids/video1.mp4").subclip(0, 10)

combined = concatenate_videoclips([clip1, clip2, clip3])
combined.write_videofile("test.mp4")