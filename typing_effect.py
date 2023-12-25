import sys, time

def typing_effect(sentence):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

    time.sleep(1)