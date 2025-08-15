import logging
import sys


def setup_logger() -> None:
    is_tty = sys.stderr.isatty()
    RESET = "\x1b[0m"
    COLORS = {
        logging.DEBUG: "\x1b[36m",    # cyan
        logging.INFO: "\x1b[32m",     # green
        logging.WARNING: "\x1b[33m",  # yellow
        logging.ERROR: "\x1b[31m",    # red
        logging.CRITICAL: "\x1b[35m", # magenta
    }

    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            fmt = "%(levelname)s: %(message)s"
            base = logging.Formatter(fmt)
            msg = base.format(record)
            if is_tty:
                color = COLORS.get(record.levelno, "")
                return f"{color}{msg}{RESET}"
            return msg

    root = logging.getLogger()
    # clear existing handlers to avoid duplicate output when reloading
    for h in list(root.handlers):
        root.removeHandler(h)

    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    root.addHandler(handler)
    root.setLevel('DEBUG')


def set_log_level(level: str) -> None:
    root = logging.getLogger()
    root.setLevel(level)
    
    for h in root.handlers:
        try:
            h.setLevel(level)
        except Exception:
            pass

