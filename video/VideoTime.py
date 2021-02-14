from moviepy.editor import VideoFileClip

def get_File_Time(filepath):
    clip = VideoFileClip(filepath)
    return clip.duration
    # print(clip.duration)

