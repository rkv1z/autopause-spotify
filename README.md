# spotify-autopause

Automatically pauses Spotify when any other app on your PC starts playing
audio (a YouTube video, a Telegram voice message, a call) and resumes it
when that audio stops. Runs silently in the background.


## How it works

Every 2 seconds, the script asks Windows for all active media sessions
(the same ones behind the volume overlay). It then:

1. Looks for the Spotify session.
2. Checks whether any session is currently playing.
3. Pauses Spotify if something else is playing, and resumes it once nothing is playing.

## Why it doesn't use the Spotify API

Spotify's Web API only allows playback control for Premium accounts. This
script uses Windows' built-in media session controls instead, so it works
with a free account and controls only Spotify, not whatever app last
received a media key press.

## Requirements

- Windows 10/11
- Python 3.x
- Spotify desktop app
- Packages listed in `requirements.txt`

## Installation

```
pip install -r requirements.txt
python your_script_name.py
```

## Run automatically at login

1. Press Win+R, type `shell:startup`, press Enter.
2. Create a shortcut there with the target:
   `"path\to\.venv\Scripts\pythonw.exe" "path\to\your_script_name.py"`
3. `pythonw.exe` runs without a console window. To stop it, end
   `pythonw.exe` in Task Manager.

## Limitations

- Windows only
- Checks every 2 seconds, so there is a short delay
- Only reacts to apps that register with Windows media controls
