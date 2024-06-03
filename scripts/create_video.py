from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, TextClip, CompositeVideoClip
from PIL import Image

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
        txt_clip = TextClip(subtitle, fontsize=24, color='white', size=img_clip.size).set_duration(duration_per_image).set_position(('center', 'bottom'))

        # Combine the image and text clips
        composite = CompositeVideoClip([img_clip, txt_clip])
        clips.append(composite)

    # Concatenate all clips
    video = concatenate_videoclips(clips, method="compose")

    # Add audio to the video
    video = video.set_audio(audio_clip)

    # Write the final video file
    video.write_videofile(video_path, codec="libx264", fps=24)
