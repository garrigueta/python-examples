# Python MIDI examples

## Description

Contains some examples of Python to manage MIDI resources

## Set-up

Install included requirements file:

```bash
pip install -r MIDI/requirements.txt
```

For Mac based OS you need to install portaudio
```bash
# for Mac
# fixes: 
#   src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
# https://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include
brew install portaudio
```