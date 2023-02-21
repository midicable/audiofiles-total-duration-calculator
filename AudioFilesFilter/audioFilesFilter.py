import math
import os

import mutagen.mp3
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

import scipy
from scipy.io import wavfile


# Filters only .wav files
def isWAV(file):
    return file.name.endswith('.wav')

# Filters oly .mp3 files
def isMP3(file):
    return file.name.endswith('.mp3')

# Returns .mp3 file duration
def getMP3Duration(file):
    try:
        audio = MP3(file)
        return round(audio.info.length, 3)
    except mutagen.mp3.HeaderNotFoundError:
        return 0.0


# Returns .wav file duration
def getWAVDuration(file):
    return round(WAVE(file).info.length, 3)

# Returns total duration of audio files in directory
def getTotalAudioDuration(path):
    response = {
        'duration': 0.0,
        'filesRead': 0,
        'failedFiles': list()
    }
    for file in os.scandir(path):
        if isMP3(file):
            duration = getMP3Duration(file)
            if duration:
                response['duration'] += duration
                response['filesRead'] += 1
            else:
                response['failedFiles'].append(file.path)
        elif isWAV(file):
            duration = getWAVDuration(file)
            if duration:
                response['duration'] += getWAVDuration(file)
                response['filesRead'] += 1
            else:
                response['failedFiles'].append(file.path)
        else:
            continue
    return response

# Returns a formatted string of total audio files duration
def getTotalDurationFormatted(path):
    
    duration = getTotalAudioDuration(path)
    seconds_total = math.trunc(duration)
    milliseconds_total = int(round(duration - seconds_total, 3) * 1000)
    hours = seconds_total // 3600
    minutes = (seconds_total - hours * 3600) // 60
    seconds = (seconds_total - minutes * 60) % 60

    return f'{hours} h. {minutes} m. {seconds} s. {milliseconds_total} ms.'