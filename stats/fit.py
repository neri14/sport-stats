import logging

from garmin_fit_sdk import Decoder,Stream


class FIT:
    def __init__(self, path):
        self.messages = None

        self.load_fit_file(path)


    def load_fit_file(self, path):
        logging.info(f"Loading FIT file from {path}")
        stream = Stream.from_file(path)
        logging.debug(f"Decoding FIT file")
        decoder = Decoder(stream)
        logging.debug(f"Reading messages from FIT file")
        self.messages, errors = decoder.read()

        for e in errors:
            logging.error(f"{e}")

        logging.info(f"FIT file loaded successfully")

