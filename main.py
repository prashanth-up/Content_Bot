import os
import argparse
import imageio_ffmpeg as ffmpeg

# Set the path to the FFmpeg binary
ffmpeg_path = "/opt/homebrew/bin/ffmpeg"  # Update this path based on the output of `which ffmpeg`
os.environ["FFMPEG_BINARY"] = ffmpeg_path
print("FFMPEG_BINARY set to:", os.environ["FFMPEG_BINARY"])

# Set the path to the ImageMagick binary
imagemagick_path = "/opt/homebrew/bin/magick"  # Update this path based on the output of `which magick`
os.environ["IMAGEMAGICK_BINARY"] = imagemagick_path
print("IMAGEMAGICK_BINARY set to:", os.environ["IMAGEMAGICK_BINARY"])

from scripts import config_loader, generate_script, text_to_audio, generate_images
from scripts.create_video import create_video  # Correctly import the create_video function
from tqdm import tqdm

def main(image, audio, video, create):
    config = config_loader.load_config()
    topics = config_loader.load_topics()

    os.makedirs('output_videos', exist_ok=True)
    for topic in tqdm(topics, desc="Processing topics"):
        topic_dir = os.path.join('output_videos', topic.replace(' ', '_'))
        os.makedirs(topic_dir, exist_ok=True)
        assets_audio_dir = os.path.join(topic_dir, 'assets_audio')
        assets_images_dir = os.path.join(topic_dir, 'assets_images')
        os.makedirs(assets_audio_dir, exist_ok=True)
        os.makedirs(assets_images_dir, exist_ok=True)

        script = None
        audio_path = None
        image_paths = []

        if audio or video or create:
            tqdm.write(f"Generating script for topic: {topic}")
            script = generate_script.generate_script(config['openai_api_key'], topic)
            if script:
                script_path = os.path.join(topic_dir, "script.txt")
                with open(script_path, "w") as script_file:
                    script_file.write(script)
            else:
                tqdm.write(f"Skipping topic: {topic} due to errors in script generation.")
                continue

        if audio or create:
            if script:
                audio_path = os.path.join(assets_audio_dir, "audio.mp3")
                text_to_audio.text_to_audio(config['azure_api_key'], config['azure_region'], script, audio_path, voice="en-US-JennyNeural", style="cheerful")

        if image or create:
            image_paths = generate_images.generate_images(config['openai_api_key'], topic, 2, assets_images_dir)
            if not image_paths:
                tqdm.write(f"No images generated for topic: {topic}. Skipping image generation.")

        if video or create:
            if script and audio_path and image_paths:
                video_path = os.path.join(topic_dir, "video.mp4")
                create_video(image_paths, audio_path, video_path, subtitles=script)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process tasks for content generation.")
    parser.add_argument('-i', '--image', action='store_true', help="Generate images")
    parser.add_argument('-a', '--audio', action='store_true', help="Generate audio")
    parser.add_argument('-v', '--video', action='store_true', help="Create video")
    parser.add_argument('-c', '--create', action='store_true', help="Run all tasks")

    args = parser.parse_args()
    main(args.image, args.audio, args.video, args.create)
