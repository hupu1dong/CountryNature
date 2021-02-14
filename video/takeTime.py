from moviepy.editor import VideoFileClip

clip = VideoFileClip("mooc.mp4")
print(clip.duration)  # seconds