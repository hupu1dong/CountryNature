import moviepy.editor as mp

from video.EachFile import walkFile as wl

from video.VideoTime import get_File_Time as ftime

def add_mosac(video,start_time_s,end_time_s,img_path,postition_x_y):
    logo = (mp.ImageClip(img_path)
            .set_duration(video.duration)  # 时长
            # .resize(height=100)  # 水印高度，等比缩放
            .margin(left=0, top=0, opacity=1) # 水印边距和透明度
            # .set_pos(("left","top")))
            .set_pos(postition_x_y))  # 水印位置
    # 设置遮盖起始时间
    logo.start = start_time_s
    # 设置遮盖结束时间
    logo.end=end_time_s
    result = mp.CompositeVideoClip([video, logo])
    return result
if __name__ == '__main__':
    fileList = wl("F:\DropWaterSign")
    for l in fileList:
        # 这里写入mp4源文件路径
        video = mp.VideoFileClip(l)
        ft = ftime(l)
        # 这里是各遮盖的设置，参数：video对象,遮盖开始时间(秒)，遮盖结束时间(秒)，遮盖使用的图片路径,遮盖的未知(x和y坐标)
        result = add_mosac(video, start_time_s=0, end_time_s=ft, img_path='video/blank.jpg', postition_x_y=(780, 15))

        # 输出结果 .mp4文件默认用libx264编码， 比特率单位bps
        result.write_videofile(l[:17]+"result_"+l[17:], codec="libx264", bitrate="10000000")
        print(l[:17]+"result_"+l[17:]+"写入完成!!!")