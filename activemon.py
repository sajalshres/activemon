import time
import sys
import logging
import argparse
import pyautogui
import win32api

__author__ = "Sajal N. Shrestha"
__status__ = "Development"
__version__ = "0.2"

pyautogui.FAILSAFE = False


def get_logger(debug: bool = False) -> logging.Logger:
    level = logging.DEBUG if debug else logging.INFO
    simple_formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(simple_formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.propagate = False
    return logger


def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTIONS] [FILE]...",
        description="Monitors user idle and prevents screen from locking",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"activemon.exe {__version__}"
    )
    parser.add_argument(
        "-i",
        "--interval",
        dest="interval",
        type=int,
        default=10,
        help="Duration of interval to check if idle (Default is 10 seconds).",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        dest="threshold",
        type=int,
        default=120,
        help="Duration of threshold for idle detection (Default is 120 seconds).",
    )
    parser.add_argument(
        "-b",
        "--button",
        dest="button",
        default="capslock",
        help="Button to press to make system in active state. (Default is capslock).",
    )
    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        help="Enables debug mode for verbose logs.",
    )
    parser.set_defaults(debug=False)

    return parser


def get_idle_time() -> float:
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000


def make_user_active(button: str = "capslock") -> None:
    for _ in range(0, 2):
        pyautogui.press(button, interval=1)


def main() -> None:
    parser = get_argument_parser()
    args = parser.parse_args()
    logger = get_logger(debug=args.debug)
    print("Monitoring started, press CTRL + C to exit")
    while True:
        time.sleep(args.interval)
        idle_time = get_idle_time()
        logger.debug("Idle time is %s seconds", idle_time)
        if idle_time > args.threshold:
            logger.info("Idle since %s seconds, making user active", args.threshold)
            make_user_active(button=args.button)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)