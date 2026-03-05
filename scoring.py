def priority_score(impact:int, effort:int, risk:int) -> float:
    effort=max(1,effort)
    return round((impact*2 + risk*1.5) / effort, 2)

def score_rows(rows):
    out=[]
    for r in rows:
        score=priority_score(r[3],r[4],r[5])
        out.append({'id':r[0],'title':r[1],'area':r[2],'impact':r[3],'effort':r[4],'risk':r[5],'status':r[6],'score':score})
    out.sort(key=lambda x:x['score'], reverse=True)
    return out
