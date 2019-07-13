# fast-recorder

In a ASR project, a difficult and boring part is the creation of a speech dataset. This scripts makes the dictation of a set of transcriptions easier. It was created as a tool in a [GSoC project](https://github.com/eellak/gsoc2019-sphinx).


# Required packages
```pip install sounddevice```


# Usage
We assume that there is a folder that contains a set of texts to be dictated. Repetitely, it displays the next text to be dictates, then waits for some seconds and starts the recording. When the user finishes the curent recording, he presses and Ctrl+C and the file is saved automatically as a .wav file.

```python recorder.py -h

usage: recorder.py [-h] --output OUTPUT --input INPUT --rate RATE --channels
                   CHANNELS [--delay DELAY]

Tool for recording a speech dataset quickly.

optional arguments:
  -h, --help           show this help message and exit

required arguments:
  --output OUTPUT      Folder to save the files
  --input INPUT        Folder that contains the input transcriptions
  --rate RATE          Sample rate to be used
  --channels CHANNELS  Number of channels to be used

optional_arguments:
  --delay DELAY        Delay until recording starts
  
```
