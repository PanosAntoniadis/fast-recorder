import argparse
import sys
import os
from helper import record
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''
		Tool for recording a speech dataset quickly.
	''')

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional_arguments')

    required.add_argument(
        '--output', help="Folder to save the files", required=True)
    required.add_argument(
        '--input', help="Folder that contains the input transcriptions", required=True)
    required.add_argument(
        '--rate', help="Sample rate to be used", required=True, type=int)
    required.add_argument(
        '--channels', help="Number of channels to be used", required=True, type=int)
    optional.add_argument(
        '--delay', help="Delay until recording start", default=2, type=float)

    args = parser.parse_args()
    out = args.output
    inp = args.input
    rate = args.rate
    channels = args.channels
    delay = args.delay

    if not out.endswith('/'):
        out = out + '/'
    if not inp.endswith('/'):
        inp = inp + '/'

    if not os.path.exists(out):
        os.makedirs(out)

    for text in sorted(os.listdir(inp)):
        while True:
            print('press n to record ' +
                  os.path.join(inp, text) + ' or q to quit')
            ans = input()
            if ans == "n":
                break
            if ans == "q":
                sys.exit("Exiting...")
        with open(os.path.join(inp, text), 'r') as f:
            print('Text to dictate:')
            print(f.read())
            time.sleep(delay)
            wav_path = os.path.join(out, text + '.wav')
            if not os.path.exists(wav_path):
                record(rate, channels, wav_path)
