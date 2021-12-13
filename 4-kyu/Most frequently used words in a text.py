from collections import Counter
import re

def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [k for k, v in c.most_common(3)]
