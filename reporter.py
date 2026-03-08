import json
from scoring import score

def to_markdown(rows):
    out=['# Tech Debt Report','', '| ID | Title | Area | Priority |', '|---|---|---|---|']
    for r in rows:
        pr=score(r[3],r[4],r[5])
        out.append(f'| {r[0]} | {r[1]} | {r[2]} | {pr} |')
    return '\n'.join(out)

def to_json(rows):
    data=[]
    for r in rows:
        data.append({'id':r[0],'title':r[1],'area':r[2],'impact':r[3],'effort':r[4],'risk':r[5],'notes':r[6],'priority':score(r[3],r[4],r[5])})
    return json.dumps(data, indent=2)
