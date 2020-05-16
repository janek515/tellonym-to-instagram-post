# Tellonym to instagram post

![Contributors](https://img.shields.io/github/contributors/janek515/tellonym-to-instagram-post) ![Size](https://img.shields.io/github/repo-size/janek515/tellonym-to-instagram-post) ![Python application](https://github.com/janek515/tellonym-to-instagram-post/workflows/Python%20application/badge.svg?branch=master)

This python module makes images from Tellonym 'tells' and automatically uploads the to your Google Drive.

## Installation

### Dependencies
In order to run this module you will need:
- [Pillow](https://github.com/python-pillow/Pillow)
- [requests](https://requests.readthedocs.io/en/master/)
- Google Drive API ([Google Client Library](https://developers.google.com/drive/api/v3/quickstart/python#step_2_install_the_google_client_library))
- [tellonym-python](https://github.com/Logxn/tellonym-python) (included)

#### Installing dependencies

Using pip:

```bash
$ pip install -r requirements.txt
```

Using pipenv:

```bash
$ pipenv sync
```

### Downloading module

Go to [the releases page](https://github.com/janek515/tellonym-to-instagram-post/releases), download the newest version and extract it into folder of your choice


## Configuration

You can change the default `bg.jpg` background file to any other `image/jpeg` file you want.

If you want the files no to be uploaded to the main directory of your Google Drive, you need to specify the `folder ID` in the `drive.txt` file.
More on how to find folder ID [here](https://ploi.io/documentation/mysql/where-do-i-get-google-drive-folder-id)

If you don't want to upload your images to the cloud you can disable this function by writing `False` inside of the  `drive.txt` file.

You can change the font to any TrueType or OpenType font of your choice by either changing its file name to `Lato.ttf` or changing the `font` property inside `run.py` file.

## Usage
To initialize the module you need define the class:
```python
from run import TellonymPost as TP

tellpost = TP(creds, interval, fontcol, rectcol, padding, d)

```

The `__init__` function have 6 parameters:
| Parameter | Description | Type | Default value | Optional |
| --- | --- | --- | --- | --- |
| `creds` | Tellonym credentials | `tuple[str, str]` | `None` | No |
| `interval` | Interval for checking on new tells (in minutes). | `int` | `10` | Yes |
| `fontcol` | Font color as 24 bit RGB value. | `tuple[int, int, int]` | `(255, 255, 255)` | Yes |
| `rectcol` | Textbox BG color as 24 bit RGB value.  | `tuple[int, int, int]` | `(0, 0, 0)` | Yes |
| `padding` | Padding of the text inside the textbox (in pixels). | `int` | `10` | Yes |
| `d` | Debug mode | `bool` | `False` | Yes |

To start the automation you need to call a function:
```python

from run import TellonymPost as TP

tellpost = TP(creds, interval, fontcol, rectcol, padding)

tellpost.run()

```

Now the function will start checking tells, generating images, and sending them to your Google Drive.

## Copyright and Credits

Credit to [Logxn](https://github.com/Logxn/) for his [tellonym-python](https://github.com/Logxn/tellonym-python) API.

More about license concerning this module inside the [`LICENSE`](LICENSE) file.
