from app.processors.message_censor import MessageCensor


def test_censor_message():
    censor = MessageCensor()
    censor.banned_words.data = ["плохо", "ужасно"]
    message = "Это плохо и ужасно"
    censored = censor.censor_message(message)
    assert censored == "Это ***** и ******"


def test_case_insensitive_censoring():
    censor = MessageCensor()
    censor.banned_words.data = ["плохо"]
    message = "Это Плохо и ПЛОХО"
    censored = censor.censor_message(message)
    assert censored == "Это ***** и *****"


def test_update_banned_words():
    censor = MessageCensor()
    censor.banned_words.data = []
    censor.update_banned_words(["новое"])
    assert "новое" in censor.banned_words.data
