import json

d = json.load(open('scratch/speed_batch5_raw.json', encoding='utf-8'))
words_curr = [
    'concurrence', 'concurrency', 'concurrent', 'concurrently', 'concurring',
    'countercurrent', 'currajong', 'currant', 'currawong', 'currency',
    'current', 'currently', 'currentness', 'curricular', 'curriculum',
    'currier', 'currish', 'currishly', 'curry', 'currycomb',
    'extracurricular', 'incurrence', 'incurring', 'noncurrent', 'nonoccurrence',
    'occurrence', 'occurrent', 'recurrence', 'recurrent', 'recurrently',
    'recurring', 'undercurrent'
]

for w in words_curr:
    qs = d.get(w, {}).get('quotes', [])
    print(f"{w} ({len(qs)}):")
    for q in qs[:3]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:100]}...")
