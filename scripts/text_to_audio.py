from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioConfig

def text_to_audio(api_key, endpoint, text, output_audio_path):
    speech_config = SpeechConfig(subscription=api_key, endpoint=endpoint)
    audio_config = AudioConfig(filename=output_audio_path)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text).get()
