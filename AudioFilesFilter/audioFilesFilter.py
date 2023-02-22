import math
import os

import mutagen.mp3
from mutagen.mp3 import MP3
from mutagen.wave import WAVE


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
    try:
        audio = WAVE(file)
        return round(audio.info.length, 3)
    except mutagen.wave.IffError:
        return 0.0

# Formats time in seconds to a string HH h. MM m. SS s. MSMS ms.
def formatTime(seconds):
    secondsIntegerPart = math.trunc(seconds)
    milliseconds = int(round(seconds - secondsIntegerPart, 3) * 1000)
    hours = secondsIntegerPart // 3600
    secondsIntegerPart %= 3600
    minutes = secondsIntegerPart // 60
    secondsIntegerPart %= 60

    return f'{hours} h. {minutes} m. {secondsIntegerPart} s. {milliseconds} ms.'

# Returns total duration of audio files in directory
def getTotalAudioDuration(path):
    response = {
        'duration': '',
        'filesRead': 0,
        'filesTotal': 0,
        'failedToRead': list()
    }

    totalDurationSeconds = 0
    for file in os.scandir(path):
        if isMP3(file):
            duration = getMP3Duration(file)
            totalDurationSeconds += duration
            response['filesTotal'] += 1
            if duration:
                response['filesRead'] += 1
            else:
                response['failedToRead'].append(file.path)
        elif isWAV(file):
            duration = getWAVDuration(file)
            totalDurationSeconds += duration
            response['filesTotal'] += 1
            if duration:
                response['filesRead'] += 1
            else:
                response['failedToRead'].append(file.path)
        else:
            continue
    response['duration'] = formatTime(totalDurationSeconds)

    return response
