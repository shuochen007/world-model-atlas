#!/usr/bin/env python3
"""Build a dependency-free, standalone HTML tutorial from tracked source files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
models = []
for filename in ('base-models.json', 'world-models.json', 'wam-models.json'):
    path = ROOT / filename
    if path.exists():
        models.extend(json.loads(path.read_text(encoding='utf-8')))

required = {'id','name','year','type','org','question','summary','input','output',
            'training','inference','innovation','connection','limit','steps','sources'}
ids = set()
for model in models:
    assert not required - model.keys(), (model.get('id'), required - model.keys())
    assert model['id'] not in ids, model['id']
    ids.add(model['id'])
    assert model['type'] in ('gen','rep','wm','wam')
    assert len(model['steps']) >= 3
    assert all(len(s) == 2 for s in model['steps'])
    assert all(len(s) == 2 and s[1].startswith('https://') for s in model['sources'])

order = ['ddpm','ldm','dit','flow','vdm','svd','sora','cogvideo','wan21','wan22',
         'ijepa','vjepa','vjepa2','dreamer','genie','genie2','genie3','cosmos1','cosmos2',
         'cosmos3','diffpolicy','unipi','videovla','dreamzero','lingbot','lingbot2','gigaworld','giga1','gigapolicy','gigapolicy05']
models.sort(key=lambda model: order.index(model['id']) if model['id'] in order else 99)
html = (ROOT / 'template.html').read_text(encoding='utf-8')
data = 'const MODELS = ' + json.dumps(models, ensure_ascii=False, separators=(',', ':')) + ';'
for marker, content in [('/* INLINE_CSS */', (ROOT/'styles.css').read_text(encoding='utf-8')),
                        ('/* INLINE_DATA */', data.replace('</script', '<\\/script')),
                        ('/* INLINE_APP */', (ROOT/'app.js').read_text(encoding='utf-8'))]:
    assert html.count(marker) == 1
    html = html.replace(marker, content)
(ROOT/'index.html').write_text(html, encoding='utf-8')
print(f'Built index.html: {len(models)} models, {len(html.encode("utf-8")):,} bytes')
