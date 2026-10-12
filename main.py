from arduino.app_utils import App, Bridge, Logger
from arduino.app_bricks.keyword_spotting import KeywordSpotting

logger = Logger("wake_word_detection")

spotter = KeywordSpotting()


def on_wake_word():
    logger.info("Turn on wake word detected")
    Bridge.call("on_alexa_led")


def off_wake_word():
    logger.info("Turn off wake word detected")
    Bridge.call("off_alexa_led")


spotter.on_detect("turn_on_alexa", on_wake_word)
spotter.on_detect("turn_off_alexa", off_wake_word)


App.run()
