# benzi

A cross-platform utility that sends you a desktop notification on the hour, every hour. Might be useful if you have a hard time keeping track of... time.

## Installation

Use either `pipx` (recommended) or `pip`.

```sh
pipx install git+https://github.com/jahinzee/benzi.git  
```

> **Dependency Note:** The `playsound` project looks to be unmaintained, and uses the deprecated `setup.py` installation method. This app uses [this fork by taconi](https://github.com/taconi/playsound), which uses the supported pyproject.toml method.

## Usage

```
usage: __init__.py [-h] [-s SOUND] [-t]

options:
  -h, --help            show this help message and exit
  -s SOUND, --sound SOUND
                        specify a sound file to play on the hour
  -t, --test            send a test notification on launch and exit
```

### Running async

The app, by itself, runs *synchronously*, meaning you will need to run it in the background if you don't want a Python console window sitting around.

On Linux and macOS, you can use `nohup` to run asynchronously from the terminal session.

```sh
nohup benzi &   # place any arguments before the &
```
