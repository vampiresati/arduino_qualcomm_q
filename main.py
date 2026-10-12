from arduino.app_utils import App, Bridge, Logger
from arduino.app_bricks.keyword_spotting import KeywordSpotting

logger = Logger("wake_word_detection")

spotter = KeywordSpotting()


def on_wake_word():
    logger.info("Wake word detected")
    Bridge.call("on_alexa_led", True)


def off_wake_word():
    logger.info("Wake word detected")
    Bridge.call("off_alex_led", True)


spotter.on_detect("turn_on_alexa", on_wake_word)
spotter.on_detect("turn_off_alexa", off_wake_word)


App.run()
