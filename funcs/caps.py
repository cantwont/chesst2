def uncapitalize_except_first(sentence):
    words = sentence.split()
    if not words:
        return ''

    words[0] = words[0].capitalize()
    words[1:] = [word.lower() for word in words[1:]]

    return ' '.join(words)