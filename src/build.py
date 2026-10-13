"""src/ 데이터로 index.html을 다시 만듭니다.  사용법: python3 src/build.py"""
import json, pathlib
S = pathlib.Path(__file__).parent
data = [l.rstrip('\n').split('|') for l in (S/'data.txt').read_text(encoding='utf-8').splitlines() if l.strip()]
desc = dict(l.split('|', 1) for l in (S/'desc/all.txt').read_text(encoding='utf-8').splitlines() if '|' in l)
D = [r[:6] + [desc[r[0]]] for r in data]
yt = {k: [a, b] for k, a, b in (l.strip().split('|') for l in (S/'yt.txt').read_text().splitlines() if l.strip())}
html = (S/'template.html').read_text(encoding='utf-8').replace('__DATA__', json.dumps(D, ensure_ascii=False)).replace('__YT__', json.dumps(yt))
(S.parent/'index.html').write_text(html, encoding='utf-8')
print('index.html 생성:', len(D), '일,', len(yt), '일 영상')
