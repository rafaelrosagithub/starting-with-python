def sample_responses(input_text):
    if input_text in ("hi", "hello"):
        return "Hey, what's up"
    elif "channel" in input_text:
        return "Youtube link: https://youtube.com"
    return "Do not understand you."