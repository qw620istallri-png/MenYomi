"""Order in which words are first met: the words seen most on real menus come first, and each new kanji
is reused right away by the words that share it (焼 → 焼鳥, 焼魚, 焼物), so every kanji learned pays off.
Rare kanji (outside the jōyō list) and old or unusual spellings wait until the end."""
import re

# the very first words, picked by hand: what you see on nearly every wall menu
CORE = ['定食', '焼鳥', '唐揚げ', '刺身', '枝豆', '冷奴', '味噌汁', '生ビール', '日本酒', '焼魚', '親子丼', '牛丼', '天丼',
        'ご飯', '大盛', '並', 'お品書き', '本日のおすすめ', '飲物', '焼物', '揚物', '一品料理', '麺類', '醤油ラーメン',
        '味噌ラーメン', '塩ラーメン', '餃子', '炒飯', 'うどん', '蕎麦', 'ざる蕎麦', '天ぷら']

def order(menu, kd):
    W, T, R = menu['W'], menu['T'], menu['R']
    phrases = set(menu['PHRASES']['signs']) | set(menu['PHRASES']['talk'])
    rare_forms = set(menu.get('CANON', {}).values()) | {v for alts in menu.get('VARIANTS', {}).values() for v, p in alts if p < .2}
    freq = {w: 0 for w in W}
    for t in T.values():
        for sec in t['sections']:
            freq[sec[0]] = freq.get(sec[0], 0) + 1
            for w in sec[1]: freq[w] = freq.get(w, 0) + 1
    for reg in R.values():
        for w in reg['items']: freq[w] = freq.get(w, 0) + 1
    for w in menu['MENTIONS']: freq[w] = freq.get(w, 0) + 1
    kanji = lambda w: {c for c in w if re.match(r'[一-鿿]', c)}
    rare = lambda c: not (kd.get(c) and kd[c][5] in {'1', '2', '3', '4', '5', '6', '8', 'S'})  # S: secondary-school jōyō
    words = [w for w in W if w not in phrases]
    out = [w for w in CORE if w in W]; known = set().union(*(kanji(w) for w in out)) if out else set()
    rest = [w for w in words if w not in out]; idx = {w: i for i, w in enumerate(rest)}
    while rest:
        def score(w):
            ks = kanji(w); new = ks - known
            return (6 * min(freq.get(w, 0), 4) + 3 * min(len(ks & known), 2) - 3 * len(new) - 8 * sum(rare(c) for c in new)
                    - 40 * (w in rare_forms), -idx[w])
        best = max(rest, key=score); rest.remove(best); out.append(best); known |= kanji(best)
    return out
