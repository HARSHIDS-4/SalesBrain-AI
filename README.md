# Insurance Proposal Starter Repo

This repo contains 5 dummy but unique proposal entries as separate JSON files, along with parsing code that prepares the records in a structured format for downstream work.

## Included
- 5 dummy but unique proposal JSON files
- separate JSON files under `data/proposals/`
- `data/proposals_index.json` listing all proposal files
- normalized schema for ingestion/reference
- parsing and chunking code that preserves original document structure
- source notes for the three named proposal forms

## Structure

```text
insurance-proposal-repo/
├── README.md
├── data/
│   ├── proposals/
│   └── proposals_index.json
├── docs/
│   └── source_notes.md
└── scripts/
    ├── parse_and_chunk.py
    └── schema.json
```

## What is ready now
- 5 unique dummy entries
- 5 separate proposal JSON files
- parsing code retained
- no Mongo code included
- no vector index build code included
