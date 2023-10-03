# benzi

big ben on your desktop. Cross-platform.

# Dependencies

Install the required dependencies with:

```sh
pip install -r requirements.txt
```

# Usage

```
usage: benzi.py [-h] [-s SOUND]

big ben on your desktop.

options:
  -h, --help            show this help message and exit
  -s SOUND, --sound SOUND
                        specify a sound file to play on the hour
```

The script runs synchronously, meaning you will need to run it in the background if you don't want a Python console window sitting around. On Windows, you can use `pythonw`, and on Linux, you may set up a custom daemon, or alternatively the following command will work:

```sh
python ./benzi.py &
disown
```
