import string
from typing import List, Dict

# This code was automatically generated at 2019-06-21 11:25:37.215412

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from numpy import array

_clf = LogisticRegression()
_clf.coef_ = array([[-3.09925498, -1.2233267 ,  0.11772731,  0.11320903, -0.61476615,
         0.16965524,  0.74448574, -0.04194057, -1.35630572, -0.24676336,
         0.41220109, -0.35504167,  0.92710423, -2.1255104 ,  0.08247018,
         0.73824089,  0.31262326,  0.41799742, -0.60178821, -0.33976708,
        -0.03794846,  0.        , -0.91812391, -0.2121092 ,  0.19453728,
        -0.60672439, -0.92668671,  0.12330509,  0.04666124,  0.        ,
         1.68901669, -0.67069155, -0.45640558,  1.05191066,  1.03483933,
         0.73240274,  0.17867271, -0.07407496,  2.06098403,  0.42573062,
        -0.38634422,  0.7109839 , -0.02934711,  0.05490663,  0.02008552,
         0.05069223,  0.        ,  0.2016651 , -0.28770706, -0.88722735,
        -0.26507582,  0.52628048, -1.28404466, -1.96447254,  0.07607324,
         0.70359565,  0.35094977,  0.01376572]])
_clf.classes_ = array([False,  True])
_clf.intercept_ = [-2.75918545]

_v = DictVectorizer()
_v.feature_names_ = ['first_chars= ', 'first_chars="a', "first_chars=' ", "first_chars='A", 'first_chars=(0', 'first_chars=(A', 'first_chars=(a', 'first_chars=)]', 'first_chars=, ', 'first_chars=. ', 'first_chars=0', 'first_chars=0 ', 'first_chars=0,', 'first_chars=0.', 'first_chars=00', 'first_chars=0:', 'first_chars=0\\', 'first_chars=@', 'first_chars=A', 'first_chars=A ', 'first_chars=A,', 'first_chars=A-', 'first_chars=A.', 'first_chars=A0', 'first_chars=A=', 'first_chars=AA', 'first_chars=Aa', 'first_chars=[0', 'first_chars=[A', 'first_chars=[a', 'first_chars=\\A', 'first_chars=a ', 'first_chars=a(', 'first_chars=a-', 'first_chars=a.', 'first_chars=a0', 'first_chars=aA', 'first_chars=a[', 'first_chars=aa', 'isalpha', 'isdigit', 'islower', 'mean_len', 'prev_len', 'punct= ', 'punct="', 'punct=%', 'punct=(', 'punct=)', 'punct=*', 'punct=,', 'punct=-', 'punct=.', 'punct=:', 'punct=;', 'punct=@', 'punct=]', 'this_len']
_v.vocabulary_ = {'first_chars= ': 0, 'first_chars="a': 1, "first_chars=' ": 2, "first_chars='A": 3, 'first_chars=(0': 4, 'first_chars=(A': 5, 'first_chars=(a': 6, 'first_chars=)]': 7, 'first_chars=, ': 8, 'first_chars=. ': 9, 'first_chars=0': 10, 'first_chars=0 ': 11, 'first_chars=0,': 12, 'first_chars=0.': 13, 'first_chars=00': 14, 'first_chars=0:': 15, 'first_chars=0\\': 16, 'first_chars=@': 17, 'first_chars=A': 18, 'first_chars=A ': 19, 'first_chars=A,': 20, 'first_chars=A-': 21, 'first_chars=A.': 22, 'first_chars=A0': 23, 'first_chars=A=': 24, 'first_chars=AA': 25, 'first_chars=Aa': 26, 'first_chars=[0': 27, 'first_chars=[A': 28, 'first_chars=[a': 29, 'first_chars=\\A': 30, 'first_chars=a ': 31, 'first_chars=a(': 32, 'first_chars=a-': 33, 'first_chars=a.': 34, 'first_chars=a0': 35, 'first_chars=aA': 36, 'first_chars=a[': 37, 'first_chars=aa': 38, 'isalpha': 39, 'isdigit': 40, 'islower': 41, 'mean_len': 42, 'prev_len': 43, 'punct= ': 44, 'punct="': 45, 'punct=%': 46, 'punct=(': 47, 'punct=)': 48, 'punct=*': 49, 'punct=,': 50, 'punct=-': 51, 'punct=.': 52, 'punct=:': 53, 'punct=;': 54, 'punct=@': 55, 'punct=]': 56, 'this_len': 57}


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
