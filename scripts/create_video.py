from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, TextClip, CompositeVideoClip
from PIL import Image
import textwrap

def resize_image(image_path, new_height):
    img = Image.open(image_path)
    aspect_ratio = img.width / img.height
    new_width = int(new_height * aspect_ratio)
    img = img.resize((new_width, new_height), Image.LANCZOS)
    resized_image_path = image_path.replace('.png', '_resized.png')
    img.save(resized_image_path)
    return resized_image_path

def split_text(script, num_parts):
    words = script.split()
    avg_len = len(words) // num_parts
    parts = []
    for i in range(num_parts - 1):
        parts.append(' '.join(words[i*avg_len : (i+1)*avg_len]))
    parts.append(' '.join(words[(num_parts-1)*avg_len:]))
    return parts

def create_text_clip(subtitle, img_size, duration):
    max_width = img_size[0] - 40  # Add padding
    wrapped_text = textwrap.fill(subtitle, width=int(max_width / 10))  # Adjust wrapping width
    
    txt_clip = TextClip(wrapped_text, fontsize=10, color='white', method='caption').set_duration(duration)
    txt_clip = txt_clip.on_color(size=(txt_clip.w + 20, txt_clip.h + 10), color=(0, 0, 0), pos=('center', 'center'))  # Add background
    txt_clip = txt_clip.set_position(('center', 'bottom'))

    return txt_clip

def create_video(image_paths, audio_path, video_path, subtitles):
    clips = []
    audio_clip = AudioFileClip(audio_path)
    video_duration = audio_clip.duration
    duration_per_image = video_duration / len(image_paths)
    
    subtitle_parts = split_text(subtitles, len(image_paths))

    for i, (image_path, subtitle) in enumerate(zip(image_paths, subtitle_parts)):
        # Resize the image
        resized_image_path = resize_image(image_path, 720)
        
        # Create the image clip
        img_clip = ImageClip(resized_image_path).set_duration(duration_per_image)

        # Create the text clip
        txt_clip = create_text_clip(subtitle, img_clip.size, duration_per_image)

        # Combine the image and text clips
        composite = CompositeVideoClip([img_clip, txt_clip])
        clips.append(composite)

    # Concatenate all clips
    video = concatenate_videoclips(clips, method="compose")

    # Add audio to the video
    video = video.set_audio(audio_clip)

    # Write the final video file
    video.write_videofile(video_path, codec="libx264", fps=24)
