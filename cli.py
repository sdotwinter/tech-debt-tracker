import argparse
from pathlib import Path
from store import init_db, add_item, list_items, close_item
from scoring import score_rows
from reporter import print_report

def run(argv=None):
    p=argparse.ArgumentParser(prog='tech-debt-tracker', description='Track and prioritize tech debt items.')
    sub=p.add_subparsers(dest='cmd', required=True)
    a=sub.add_parser('add'); a.add_argument('title'); a.add_argument('--area', default='general'); a.add_argument('--impact', type=int, default=5); a.add_argument('--effort', type=int, default=5); a.add_argument('--risk', type=int, default=5); a.add_argument('path', nargs='?', default='.')
    b=sub.add_parser('list'); b.add_argument('path', nargs='?', default='.'); b.add_argument('--status', choices=['all','open','closed'], default='all'); b.add_argument('--json', action='store_true')
    c=sub.add_parser('close'); c.add_argument('item_id', type=int); c.add_argument('path', nargs='?', default='.')
    d=sub.add_parser('report'); d.add_argument('path', nargs='?', default='.'); d.add_argument('--json', action='store_true')
    args=p.parse_args(argv)
    root=Path(getattr(args,'path','.')).resolve(); init_db(root)
    if args.cmd=='add':
        add_item(root,args.title,args.area,args.impact,args.effort,args.risk); print('Debt item added'); return 0
    if args.cmd=='close':
        close_item(root,args.item_id); print('Debt item closed'); return 0
    rows=list_items(root, status=getattr(args,'status','all'))
    scored=score_rows(rows)
    print_report(scored, as_json=getattr(args,'json',False))
    return 0
