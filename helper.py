import argparse
import queue
import sys
import sounddevice as sd
import soundfile as sf


def record(samplerate, channels, filename):
    try:
        q = queue.Queue()

        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            q.put(indata.copy())

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate=samplerate,
                          channels=channels) as file:
            with sd.InputStream(samplerate=samplerate,
                                channels=channels, callback=callback):
                print('Recording...')
                print('press Ctrl+C to stop the recording')
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
        print('\n')
        return 0
