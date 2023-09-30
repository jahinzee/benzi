# benzi

big ben on your desktop.

# Dependencies

Install the required dependencies with:

```sh
pip install -r requirements.txt
```

# Usage

The script runs synchronously, meaning you will need to run it in the background if you don't want a Python console window sitting around. On Windows, you can use `pythonw`, and on Linux, you may set up a custom daemon, or alternatively the following command will work:

```sh
python ./benzi.py & && disown
```
