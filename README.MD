# League of Legends Queue Auto-Accept

This Python script automatically accepts the queue in the League of Legends client when a match is found.

## Requirements

- Python 3.6 or later
- `requests` library

## Installation

1. Clone this repository or download the files.
```bash
git clone https://github.com/gquesnot/lol-queue-auto-accept.git
cd lol-queue-auto-accept
````


2. Install the required Python packages.
```bash
pip install -r requirements.txt
```
3. Edit the `main.py` script and replace `"path/to/League of Legends/lockfile"` with the actual path to the lockfile in your LoL game directory.
```python
LOCKFILE_PATH = "path/to/League of Legends/lockfile"
```


# Usage
1. Make sure your League of Legends client is running and you are logged in.

2. Run the script:
```bash
python main.py
```
3. The script will periodically check if you are in a queue, and it will automatically accept the queue when a match is found.


