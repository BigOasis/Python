def solution(s: str) -> int:
    word2num = {
        "zero":"0","one":"1","two":"2","three":"3","four":"4",
        "five":"5","six":"6","seven":"7","eight":"8","nine":"9"
    }
    buf = []
    out = []

    for ch in s:
        if ch.isdigit():
            out.append(ch)
        else:
            buf.append(ch)
            w = "".join(buf)
            if w in word2num:
                out.append(word2num[w])
                buf.clear()

    return int("".join(out))