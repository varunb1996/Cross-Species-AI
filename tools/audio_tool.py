import librosa

def load_audio(audio_path):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    return audio, sr


def segment_audio(
    audio,
    sr,
    segment_duration=5
):

    segment_length = sr * segment_duration

    segments = []

    for i in range(
        0,
        len(audio),
        segment_length
    ):

        segment = audio[
            i:i+segment_length
        ]

        if len(segment) > 1000:
            segments.append(segment)

    return segments