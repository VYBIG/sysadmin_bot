import os
from moviepy import *


def video_for_circle(video: str):
    circle_video = f"{video}.mp4"
    # Преобразование видео в кружок
    input_video = VideoFileClip(circle_video)
    w, h = input_video.size
    circle_size = 400
    aspect_ratio = float(w) / float(h)

    if w > h:
        new_w = int(circle_size * aspect_ratio)
        new_h = circle_size
    else:
        new_w = circle_size
        new_h = int(circle_size / aspect_ratio)
    resized_video = input_video.resized((new_w, new_h))
    output_video = resized_video.cropped(x_center=resized_video.w / 2, y_center=resized_video.h / 2, width=circle_size,
                                         height=circle_size)
    output_video.write_videofile(f"circle_{video}.mp4", codec="libx264", audio_codec="aac", bitrate="1M")
    return f'circle_{video}'

