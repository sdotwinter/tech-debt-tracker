import json

def print_report(items, as_json=False):
    if as_json:
        print(json.dumps(items, indent=2)); return
    if not items:
        print('No debt items found.'); return
    print('id  score  status  area         title')
    print('-'*72)
    for x in items:
        print(f"{str(x['id'])[:3]:3} {str(x['score'])[:6]:6} {x['status'][:6]:6} {x['area'][:12]:12} {x['title'][:40]}")
