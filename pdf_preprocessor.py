import string
from typing import List, Dict

# This code was automatically generated at 2019-05-20 14:25:48.928633

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from numpy import array

_clf = LogisticRegression()
_clf.coef_ = array([[-1.98476537, -0.574191  ,  0.23003166,  0.22442564, -0.17128219,
         0.35692281,  1.08296874, -0.29254168, -0.86373763, -0.64891859,
         0.52238215, -0.95513122,  0.64648898, -1.92479586,  0.72445132,
        -0.14225727,  0.21422565,  0.39098398, -0.73026064, -1.19914687,
        -0.2767895 ,  0.        , -1.52567924, -0.45360343,  0.46024434,
        -0.4957314 , -1.68586662,  0.34014256,  0.21487248,  0.        ,
         1.37223976, -0.05350732, -0.14732666,  1.64406728,  0.90695969,
         0.48877281,  0.18663683, -0.51551458,  2.54937969,  0.        ,
         0.        ,  0.        ,  0.03302935,  0.04662906, -0.53539238,
        -1.54945831,  0.01135887]])
_clf.classes_ = array([False,  True])
_clf.intercept_ = [-2.08485069]

_v = DictVectorizer()
_v.feature_names_ = ['first_chars= ', 'first_chars="a', "first_chars=' ", "first_chars='A", 'first_chars=(0', 'first_chars=(A', 'first_chars=(a', 'first_chars=)]', 'first_chars=, ', 'first_chars=. ', 'first_chars=0', 'first_chars=0 ', 'first_chars=0,', 'first_chars=0.', 'first_chars=00', 'first_chars=0:', 'first_chars=0\\', 'first_chars=@', 'first_chars=A', 'first_chars=A ', 'first_chars=A,', 'first_chars=A-', 'first_chars=A.', 'first_chars=A0', 'first_chars=A=', 'first_chars=AA', 'first_chars=Aa', 'first_chars=[0', 'first_chars=[A', 'first_chars=[a', 'first_chars=\\A', 'first_chars=a ', 'first_chars=a(', 'first_chars=a-', 'first_chars=a.', 'first_chars=a0', 'first_chars=aA', 'first_chars=a[', 'first_chars=aa', 'isalpha', 'isdigit', 'islower', 'mean_len', 'prev_len', 'punct= ', 'punct=.', 'this_len']
_v.vocabulary_ = {'first_chars= ': 0, 'first_chars="a': 1, "first_chars=' ": 2, "first_chars='A": 3, 'first_chars=(0': 4, 'first_chars=(A': 5, 'first_chars=(a': 6, 'first_chars=)]': 7, 'first_chars=, ': 8, 'first_chars=. ': 9, 'first_chars=0': 10, 'first_chars=0 ': 11, 'first_chars=0,': 12, 'first_chars=0.': 13, 'first_chars=00': 14, 'first_chars=0:': 15, 'first_chars=0\\': 16, 'first_chars=@': 17, 'first_chars=A': 18, 'first_chars=A ': 19, 'first_chars=A,': 20, 'first_chars=A-': 21, 'first_chars=A.': 22, 'first_chars=A0': 23, 'first_chars=A=': 24, 'first_chars=AA': 25, 'first_chars=Aa': 26, 'first_chars=[0': 27, 'first_chars=[A': 28, 'first_chars=[a': 29, 'first_chars=\\A': 30, 'first_chars=a ': 31, 'first_chars=a(': 32, 'first_chars=a-': 33, 'first_chars=a.': 34, 'first_chars=a0': 35, 'first_chars=aA': 36, 'first_chars=a[': 37, 'first_chars=aa': 38, 'isalpha': 39, 'isdigit': 40, 'islower': 41, 'mean_len': 42, 'prev_len': 43, 'punct= ': 44, 'punct=.': 45, 'this_len': 46}


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


def _line_to_features(line: str, i: int, lines: List[str]) -> Dict[str, object]:
    features = {}
    this_len = len(line)
    mean_len = _mean_in_window(lines, i)
    if i > 1:
        prev_len = len(lines[-1]) - 1
        l_char = _last_char(lines[-1])
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
        x.append(_line_to_features(line, i, lines))
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
        x.append(_line_to_features(line, i, lines))
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
