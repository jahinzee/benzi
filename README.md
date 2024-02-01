# benzi

big ben on your desktop. Cross-platform.

## Installation

Use either `pipx` (recommended) or `pip`.

```
pipx install git+https://github.com/jahinzee/benzi.git  
```

> Dependency Note: The playsound project looks to be unmaintained, and uses the deprecated setup.py installation method. The requirements file uses taconi's fork (https://github.com/taconi/playsound), which addresses this issue.

## Usage

```
usage: benzi.py [-h] [-s SOUND]

big ben on your desktop.

options:
  -h, --help            show this help message and exit
  -s SOUND, --sound SOUND
                        specify a sound file to play on the hour
```

The app runs synchronously, meaning you will need to run it in the background if you don't want a Python console window sitting around. On Windows, you can use `pythonw`, and on Linux, you may set up a custom daemon, or alternatively use `nohup` to run asynchronously from the terminal session:

```sh
nohup python ./benzi.py &   # place any arguments before the &
```
