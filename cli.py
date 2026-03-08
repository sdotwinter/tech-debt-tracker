import argparse
from store import add_item, list_items
from scoring import score
from reporter import to_markdown, to_json

def run(argv=None):
    p=argparse.ArgumentParser(prog='tech-debt-tracker')
    sub=p.add_subparsers(dest='cmd', required=True)

    a=sub.add_parser('add')
    a.add_argument('--title', required=True)
    a.add_argument('--area', required=True)
    a.add_argument('--impact', type=int, required=True)
    a.add_argument('--effort', type=int, required=True)
    a.add_argument('--risk', type=int, required=True)
    a.add_argument('--notes', default='')

    sub.add_parser('list')

    r=sub.add_parser('report')
    r.add_argument('--format', choices=['md','json'], default='md')

    args=p.parse_args(argv)

    if args.cmd=='add':
        add_item(args.title,args.area,args.impact,args.effort,args.risk,args.notes)
        print('Added debt item')
        return 0

    rows=list_items()
    if args.cmd=='list':
        if not rows:
            print('No debt items yet.'); return 0
        for r in rows:
            print(f"#{r[0]} {r[1]} [{r[2]}] priority={score(r[3],r[4],r[5])}")
        return 0

    if args.cmd=='report':
        print(to_json(rows) if args.format=='json' else to_markdown(rows))
        return 0

    return 0
