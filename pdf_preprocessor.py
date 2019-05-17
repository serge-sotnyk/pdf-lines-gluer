import string
from typing import List, Dict

# This code was automatically generated at 2019-05-17 17:56:24.195381

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from numpy import array

_clf = LogisticRegression()
_clf.coef_ = array([[-1.92428293, -0.57402104,  0.2315162 ,  0.22349134, -0.21893115,
         0.40302487,  1.06171059, -0.3000657 , -0.80354834, -0.59474902,
         0.54936339, -0.95955689,  0.65555019, -1.90063708,  0.72334064,
        -0.17199479,  0.15464983,  0.31376216, -0.66997325, -1.18498478,
        -0.270456  ,  0.        , -1.5816989 , -0.43472727,  0.49956562,
        -0.46305976, -1.72074182,  0.27111279,  0.22436558,  0.        ,
         1.32364416,  0.04193252, -0.14462101,  1.64987425,  0.89867317,
         0.50371394,  0.2192005 , -0.50426949,  2.57259903,  0.        ,
         0.        ,  0.        ,  0.02742372,  0.07301828,  0.03715351,
        -0.49300996, -1.40821851,  0.01243852]])
_clf.classes_ = array([False,  True])
_clf.intercept_ = [-1.90122847]

_v = DictVectorizer()
_v.feature_names_ = ['first_chars= ', 'first_chars="a', "first_chars=' ", "first_chars='A", 'first_chars=(0', 'first_chars=(A', 'first_chars=(a', 'first_chars=)]', 'first_chars=, ', 'first_chars=. ', 'first_chars=0', 'first_chars=0 ', 'first_chars=0,', 'first_chars=0.', 'first_chars=00', 'first_chars=0:', 'first_chars=0\\', 'first_chars=@', 'first_chars=A', 'first_chars=A ', 'first_chars=A,', 'first_chars=A-', 'first_chars=A.', 'first_chars=A0', 'first_chars=A=', 'first_chars=AA', 'first_chars=Aa', 'first_chars=[0', 'first_chars=[A', 'first_chars=[a', 'first_chars=\\A', 'first_chars=a ', 'first_chars=a(', 'first_chars=a-', 'first_chars=a.', 'first_chars=a0', 'first_chars=aA', 'first_chars=a[', 'first_chars=aa', 'isalpha', 'isdigit', 'islower', 'mean_len', 'prev_glued', 'prev_len', 'punct= ', 'punct=.', 'this_len']
_v.vocabulary_ = {'first_chars= ': 0, 'first_chars="a': 1, "first_chars=' ": 2, "first_chars='A": 3, 'first_chars=(0': 4, 'first_chars=(A': 5, 'first_chars=(a': 6, 'first_chars=)]': 7, 'first_chars=, ': 8, 'first_chars=. ': 9, 'first_chars=0': 10, 'first_chars=0 ': 11, 'first_chars=0,': 12, 'first_chars=0.': 13, 'first_chars=00': 14, 'first_chars=0:': 15, 'first_chars=0\\': 16, 'first_chars=@': 17, 'first_chars=A': 18, 'first_chars=A ': 19, 'first_chars=A,': 20, 'first_chars=A-': 21, 'first_chars=A.': 22, 'first_chars=A0': 23, 'first_chars=A=': 24, 'first_chars=AA': 25, 'first_chars=Aa': 26, 'first_chars=[0': 27, 'first_chars=[A': 28, 'first_chars=[a': 29, 'first_chars=\\A': 30, 'first_chars=a ': 31, 'first_chars=a(': 32, 'first_chars=a-': 33, 'first_chars=a.': 34, 'first_chars=a0': 35, 'first_chars=aA': 36, 'first_chars=a[': 37, 'first_chars=aa': 38, 'isalpha': 39, 'isdigit': 40, 'islower': 41, 'mean_len': 42, 'prev_glued': 43, 'prev_len': 44, 'punct= ': 45, 'punct=.': 46, 'this_len': 47}

def preprocess_pdf(text: str) -> str:
    return _preprocess_pdf(text, _clf, _v)

# end of automatically generated code


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


def _line_to_features(line: str, i: int, lines: List[str], y: List[bool]) -> Dict[str, object]:
    features = {}
    this_len = len(line)
    mean_len = _mean_in_window(lines, i)
    if i > 1:
        prev_len = len(lines[-1]) - 1
        l_char = _last_char(lines[-1])
    else:
        prev_len = 0
        l_char = ' '
    prev_glued = 0  # How many lines before was glued
    for p in range(i - 1, max(-1, i - 10), -1):  # Calc only up to ten items in the sequence
        if y[p]:
            prev_glued += 1
        else:
            break
    features.update(
        {
            'this_len': this_len,
            'mean_len': mean_len,
            'prev_len': prev_len,
            'prev_glued': prev_glued,
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
        x.append(_line_to_features(line, i, lines, y))
    return x, y


_HYPHEN_CHARS = {
    '\u002D',  # HYPHEN-MINUS
    '\u00AD',  # SOFT HYPHEN
    '\u2010',  # HYPHEN
    '\u2011',  # NON-BREAKING HYPHEN
}


def _preprocess_pdf(text: str, clf, v) -> str:
    lines = [s.strip() for s in text.strip().splitlines()]
    y_pred = []
    for i, line in enumerate(lines):
        x_one_sample = _line_to_features(line, i, lines, y_pred)
        x_one_sample_features = v.transform([x_one_sample])
        y_one_pred = clf.predict(x_one_sample_features)
        y_pred.append(y_one_pred[0])

    corrected_acc = []
    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0 or not y_pred[i]:
            corrected_acc.append(line)
        else:
            prev_line = corrected_acc[-1]
            if prev_line[-1] in _HYPHEN_CHARS:
                corrected_acc[-1] = prev_line[:-1]
            else:
                corrected_acc[-1] += ' '
            corrected_acc[-1] += line

    corrected = '\n'.join(corrected_acc)
    return corrected
