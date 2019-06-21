import string
from typing import List, Dict
# inject code here #


def _mean_in_window(lines, i) -> float:
    start = max(i - 5, 0)
    finish = min(i + 5, len(lines) - 1)
    sm, count = 0, 0
    for n in range(start, finish):
        sm += len(lines[n]) - 1  # minus one-char prefix
        count += 1
    return sm / max(count, 1)


def _last_char(line: str) -> str:
    return ' ' if len(line) < 1 else line[-1]


def _last_char_features(l_char: str) -> Dict[str, object]:
    res = {
        'isalpha': l_char.isalpha(),
        'isdigit': l_char.isdigit(),
        'islower': l_char.islower(),
        'punct': l_char if l_char in string.punctuation else ' ',
    }
    return res


def _first_chars(line: str) -> str:
    if len(line) < 1:
        chars = ' '
    elif len(line) < 2:
        chars = line[0]
    else:
        chars = line[:2]
    res = []
    for c in chars:
        if c.isdigit():
            res.append('0')
        elif c.isalpha():
            res.append('a' if c.islower() else 'A')
        else:
            res.append(c)
    return ''.join(res)


def _line_to_features(line: str, i: int, lines: List[str], annotated: bool) -> Dict[str, object]:
    features = {}
    this_len = len(line)
    mean_len = _mean_in_window(lines, i)
    if i > 0:
        prev_len = len(lines[i-1]) - (1 if annotated else 0)
        l_char = _last_char(lines[i-1])
    else:
        prev_len = 0
        l_char = ' '
    features.update(
        {
            'this_len': this_len,
            'mean_len': mean_len,
            'prev_len': prev_len,
            'first_chars': _first_chars(line),
        })
    features.update(_last_char_features(l_char))
    return features


def _featurize_text_with_annotation(text: str) -> (List[object], List[bool]):
    lines = text.strip().splitlines()
    x, y = [], []
    for i, line in enumerate(lines):
        y.append(line[0] == '+')  # True, if line should be glued with previous
        line = line[1:]
        x.append(_line_to_features(line, i, lines, True))
    return x, y


_HYPHEN_CHARS = {
    '\u002D',  # HYPHEN-MINUS
    '\u00AD',  # SOFT HYPHEN
    '\u2010',  # HYPHEN
    '\u2011',  # NON-BREAKING HYPHEN
}


def _preprocess_pdf(text: str, clf, v) -> str:
    lines = [s.strip() for s in text.strip().splitlines()]
    x = []
    for i, line in enumerate(lines):
        x.append(_line_to_features(line, i, lines, False))
    if not x:
        return ''
    
    x_features = v.transform(x)
    y_pred = clf.predict(x_features)

    corrected_acc = []
    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0 or not y_pred[i]:
            corrected_acc.append(line)
        else:
            prev_line = corrected_acc[-1]
            if prev_line != '' and prev_line[-1] in _HYPHEN_CHARS:
                corrected_acc[-1] = prev_line[:-1]
            else:
                corrected_acc[-1] += ' '
            corrected_acc[-1] += line

    corrected = '\n'.join(corrected_acc)
    return corrected
