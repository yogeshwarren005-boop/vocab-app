import json

with open('scratch/all_clusters_status.json', encoding='utf-8') as f:
    data = json.load(f)

# Update Body in status:
data['Cluster Body'] = {'total': 551, 'pristine': 551, 'problem': 0, 'pass': True}
with open('scratch/all_clusters_status.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

remaining = {k: v for k, v in data.items() if not v.get('pass')}
print(f"Total remaining clusters: {len(remaining)}")
for k, v in sorted(remaining.items(), key=lambda x: x[1]['total'], reverse=True):
    print(f"  {k}: {v['total']} words (problem: {v['problem']})")
