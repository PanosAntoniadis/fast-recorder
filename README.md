# fast-recorder

In a ASR project, a boring part is the creation of a speech dataset. This script makes the dictation of a set of transcriptions easier. It was initially developed as a tool in my [GSoC project](https://github.com/eellak/gsoc2019-sphinx).


## Prerequisites

```pip install sounddevice```


## Usage

We assume that there is a folder that contains a set of texts for dictation. At first, it displays the next text to be dictated, it waits for some seconds and then it starts the recording. When the user finishes the curent recording, he presses ``` Ctrl+C```  and the file is saved automatically as a .wav file.

``` 
$ python recorder.py -h

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

For example, if we have two transcriptions in ```data``` folder, in order to dictate them in [Sphinx](https://cmusphinx.github.io/wiki/tutorialam/) format we do the following:
```
$ python recorder.py --output wav --input data/ --rate 16000 --channels 1 --delay 2
press n to record data/data_0 or q to quit
n
Text to dictate:
test1

Recording...
press Ctrl+C to stop the recording
^C
Recording finished: 'wav/data_0.wav'


press n to record data/data_1 or q to quit
n
Text to dictate:
test2

Recording...
press Ctrl+C to stop the recording
^C
Recording finished: 'wav/data_1.wav'
```


## License
This tool is licensed under the MIT License.
