import sys
import collections
from collections import defaultdict


def print_q(id, result, id2cands):
    cands = id2cands[id]
    assert len(cands) == 2
    assert result in cands
    for cand in cands:
        if cand == result:
            print('{}\t{}'.format(id + '-1', cand))
        else:
            print('{}\t{}'.format(id + '-0', cand))


id2result = defaultdict(list)
id2cands = dict()


for line in sys.stdin:
    line = line.strip()
    id = line.split('\t')[0]
    cands = line.split('\t')[3].split('@')[:-1]
    ans = line.split('\t')[-2]
    if 'check' in id:
        continue
    if len(cands) != 2:
        continue
    id2result[id].append(ans)
    id2cands[id] = cands

for id, ans in id2result.items():
    c = collections.Counter(ans)
    if c['[日本語として破綻している文がある]'] > 0:
        continue
    for k, v in c.items():
        if v > 8:
            print_q(id, k, id2cands)
