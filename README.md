
# Content Generation Bot

A Content Generation Bot that creates audio-visual content clips of any topic (but we like to clickbait AI/ML) that can be posted on Instagram. The bot uses a lot of API's and services to create a one-minute-long clip with subtitles. Honestly, I just coudn't find a job and was considering to become an influencer at this point. 

## Features

- Generate AI/ML topics using OpenAI GPT API
- Convert generated scripts to audio using Azure TTS
- Fetch relevant images using OpenAI DALL-E API
- Create a video with audio, images, and subtitles
- Organized folder structure for outputs
- CLI options for specific tasks (images, audio, video, all)

## Prerequisites

- Python 3.7+
- FFmpeg
- ImageMagick
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository**

```sh
git clone https://github.com/prashanth-up/content-generation-bot.git
cd content-generation-bot
```

2. **Set up a virtual environment (optional but recommended)**

```sh
python -m venv contentbot_env
source contentbot_env/bin/activate  # On Windows use `contentbot_env\Scripts\activate`
```

3. **Install the required dependencies**

```sh
pip install -r requirements.txt
```

## Configuration

1. **Create a `config.json` file in the root directory**

```json
{
    "openai_api_key": "YOUR_OPENAI_API_KEY",
    "azure_api_key": "YOUR_AZURE_API_KEY",
    "azure_region": "YOUR_AZURE_REGION"
}
```

2. **Create a `topics.json` file in the root directory with a few clickbait topics that doomscrollers just love to stare at and forget**

```json
{
    "topics": [
      "Introduction to Machine Learning",
      "Supervised vs Unsupervised Learning",
      "Neural Networks Explained"
    ]
}
```

## FFmpeg and ImageMagick Setup

### FFmpeg

FFmpeg is required for processing video and audio. You can install it using Homebrew on macOS, Chocolatey on Windows, or via the package manager on Linux.

- **macOS**

```sh
brew install ffmpeg
```

- **Windows**

```sh
choco install ffmpeg
```

- **Linux**

```sh
sudo apt-get update
sudo apt-get install ffmpeg
```

### ImageMagick

ImageMagick is used for handling image transformations.

- **macOS**

```sh
brew install imagemagick
```

- **Windows**

Download and install from [ImageMagick](https://imagemagick.org/script/download.php).

- **Linux**

```sh
sudo apt-get install imagemagick
```

## Setting Environment Variables

Ensure FFmpeg and ImageMagick binaries are accessible. You may need to set the paths in your script:

```python
import os

# Set the path to the FFmpeg binary
os.environ["FFMPEG_BINARY"] = "/path/to/ffmpeg"  # Update this path based on your system

# Set the path to the ImageMagick binary
os.environ["IMAGEMAGICK_BINARY"] = "/path/to/magick"  # Update this path based on your system
```

## Usage

The main script is `main.py`. You can run it with different options to test specific parts of the project.

### Generate Images Only

```sh
python main.py -i
```

### Generate Audio Only

```sh
python main.py -a
```

### Create Video Only

```sh
python main.py -v
```

### Run All Tasks and Create Video

```sh
python main.py -c
```

## Folder Structure

The output folders will be organized as follows:

```
output_videos/
│
├── Introduction_to_Machine_Learning/
│   ├── assets_audio/
│   │   └── audio.mp3
│   ├── assets_images/
│   │   ├── image1.png
│   │   ├── image2.png
│   │   ├── image3.png
│   │   ├── image4.png
│   │   └── image5.png
│   ├── script.txt
│   └── video.mp4
│
├── Supervised_vs_Unsupervised_Learning/
│   └── ... (similar structure as above)
│
└── Neural_Networks_Explained/
    └── ... (similar structure as above)
```

## Screenshots and Clips

### Example Screenshot

![Placeholder for Screenshot](path/to/screenshot.png)

### Example Video Clip

![Placeholder for Video Clip](path/to/video_clip.mp4)

## Troubleshooting (Don't worry, you won't need this 😎)

- **No Audio in Video**: Ensure FFmpeg is correctly installed and accessible. Verify the audio path and codec settings.
- **Text Positioning**: Adjust the `width` parameter in `textwrap.fill` to fit the text horizontally.
- **Dependencies**: Ensure all dependencies are installed using the `requirements.txt` file.

## Future Work

### Additional Features

- [ ] **Enhanced Scheduling**: Implement a scheduling feature to automatically post the generated content on social media platforms at specified times.
- [ ] **Improved Text-to-Speech**: Integrate more advanced text-to-speech options with different voices and emotions.
- [ ] **Customization Options**: Allow users to customize the video output, including fonts, colors, and background music.
- [ ] **Multi-language Support**: Add support for generating content in multiple languages.
- [ ] **Analytics Integration**: Track the performance of the posted content using analytics APIs.

### Code Improvements

- [ ] **Modular Codebase**: Further divide the code into more modular components for better maintainability and scalability.
- [ ] **Error Handling**: Improve error handling to cover more edge cases and provide more informative error messages.
- [ ] **Optimization**: Optimize the video generation process for speed and efficiency.
- [ ] **Testing**: Implement unit tests and integration tests to ensure the code's reliability and correctness.
- [ ] **Documentation**: Expand the documentation to include detailed usage examples and advanced configurations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are very very very welcome! It took a lot of my sanity to build this in one night so; Please fork the repository and submit pull requests to make it less ugly.

