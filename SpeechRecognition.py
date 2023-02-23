import speech_recognition as sr

# initialize the recognizer
recognizer = sr.Recognizer()

# set loudness level for audio
recognizer.energy_threshold = 300

# load audio file
import speech_recognition as sr
recognizer = sr.Recognizer()

# Processing audio
audio_file = sr.AudioFile("data.wav")
type(audio_file)

with audio_file as source:
  audio_file = recognizer.record(source)
  recognizer.recognize_google(audio_data=audio_file)
type(audio_file)

# result
result = recognizer.recognize_google(audio_data=audio_file)
result
