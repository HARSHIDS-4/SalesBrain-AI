import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROPOSALS_DIR = BASE_DIR / 'data' / 'proposals'
OUT_PATH = BASE_DIR / 'data' / 'vector_chunks.json'

chunks = []
for path in sorted(PROPOSALS_DIR.glob('*.json')):
    with open(path, 'r', encoding='utf-8') as f:
        doc = json.load(f)
    text = f"""
Proposal ID: {doc['proposal_id']}
Insurer: {doc['insurer']}
Product: {doc['product_name']}
Type: {doc['proposal_type']}
Name: {doc['proposer_details']['full_name']}
Age: {doc['proposer_details']['age']}
Occupation: {doc['proposer_details']['occupation']}
Annual Income: {doc['proposer_details']['annual_income']}
City: {doc['proposer_details']['contact']['city']}
State: {doc['proposer_details']['contact']['state']}
Sum Assured: {doc['policy_details']['sum_assured']}
Plan Variation: {doc['policy_details']['plan_variation']}
Nominee: {doc['nominee_details']['name']} ({doc['nominee_details']['relationship']})
Existing Diseases: {', '.join(doc['health_declarations']['existing_diseases']) if doc['health_declarations']['existing_diseases'] else 'none'}
Hospitalization History: {doc['health_declarations']['hospitalization_last_3_years']}
Smoker: {doc['health_declarations']['smoker']}
Alcohol: {doc['health_declarations']['alcohol']}
Source Form: {doc['metadata']['source_form']}
""".strip()
    chunks.append({
        'chunk_id': f"{doc['proposal_id']}-summary",
        'proposal_id': doc['proposal_id'],
        'source_file': str(path.relative_to(BASE_DIR)),
        'text': text,
        'metadata': {
            'insurer': doc['insurer'],
            'product_name': doc['product_name'],
            'proposal_type': doc['proposal_type'],
            'source_form': doc['metadata']['source_form']
        },
        'original_document': doc
    })

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(chunks, f, indent=2)

print(f'Wrote {len(chunks)} vector-ready chunks to {OUT_PATH}')
