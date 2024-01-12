from pydub import AudioSegment

def trim_audio(input_file, start_time, end_time):
    """
    Trim an audio file and save it to a new file.

    :param input_file (str): Path to the input audio file.
    :param start_time (int): Start time in milliseconds.
    :param end_time (int): End time in milliseconds.
    :return: trrimmed audio
    """
    audio = AudioSegment.from_file(input_file)

    trimmed_audio = audio[start_time:end_time]

    return trimmed_audio

def get_audio_intervals(input_file, interval_length):
    """
    Divide audio into interval_length intervals

    :param input_file:
    :param interval_length:
    :return: array with audios of length interval_length
    """
    audios = []

    audio = AudioSegment.from_file(input_file)
    duration = audio.duration_seconds*1000

    for i in range(0, duration, interval_length):
        audios.append(audio[i:i+interval_length])

    return audios


def save_audio_by_channel(audio_signal, output_file, format):
    """
    Save audio into separate files by channel

    :param audio_signal: Audio signal to be saved
    :param output_file: path of the audio file to be saved
    :param format: format of the audio file
    :return: -
    """

    channels = audio_signal.split_to_mono() # Split the audio into separate channels

    for i, channel in enumerate(channels):  # Save each channel as a separate file (optional)
        channel.export(f"{output_file}_channel_{i + 1}.{format}", format=format)

def save_audio(audio_signal, output_file, format):
    """
    Save audio

    :param audio_signal: Audio signal to be saved
    :param output_file: path to save audio file
    :param format: format of the audio file
    :return: -
    """
    audio_signal.export(f"{output_file}.{format}", format=format)


