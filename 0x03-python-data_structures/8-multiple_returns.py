#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sent = None
    else:
        sent = sentence[0]
    return ((len(sentence)), sent)
