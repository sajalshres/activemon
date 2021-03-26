# windows-active-mon
A simple script to monitor user idle and prevent screen from locking

# Installation

- Download binary: [activemon.exe](https://github.com/sajalshres/windows-active-mon/releases/download/latest/activemon.exe)

# Usage

### Show help text

```powershell
> .\activemon.exe -h
usage: activemon.exe [OPTIONS] [FILE]...

Monitors user idle and prevents screen from locking

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INTERVAL, --interval INTERVAL
                        Duration of interval to check if idle (Default is 10 seconds).
  -t THRESHOLD, --threshold THRESHOLD
                        Duration of threshold for idle detection (Default is 60 seconds).
  -b BUTTON, --button BUTTON
                        Button to press to make system in active state. (Default is capslock).
```

### Start monitoring

```powershell
❯ .\activemon.exe
Monitoring started, press CTRL + C to exit
[2021-03-26 18:40:39] INFO Idle time is 13.797 seconds
[2021-03-26 18:40:49] INFO Idle time is 23.812 seconds
[2021-03-26 18:40:59] INFO Idle time is 33.812 seconds
[2021-03-26 18:41:09] INFO Idle time is 43.812 seconds
[2021-03-26 18:41:19] INFO Idle time is 53.812 seconds
[2021-03-26 18:41:29] INFO Idle time is 63.812 seconds
[2021-03-26 18:41:29] INFO Idle since 60 seconds, making user active
[2021-03-26 18:41:44] INFO Idle time is 12.203 seconds
```
