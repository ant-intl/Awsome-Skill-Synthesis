# Maintaining the survey catalogue

The catalogue follows the six literature taxonomy figures in *From Heterogeneous Evidence to Reusable Procedures: A Survey of Agent Skill Synthesis*.

## Files

- `data/papers.json` holds one record per paper, including its description and links.
- `data/taxonomy.json` maps papers to the categories in Figures 4, 6, 8, 10, 11, and 13.
- `data/source_manifest.json` records the survey snapshot and synchronization date.
- `scripts/build_readme.py` validates these records and generates `README.md` using the Python standard library.

## Updating an entry

1. Edit the paper's record in `data/papers.json`. Keep its ID stable; the initial IDs match the survey bibliography keys.
2. Write one factual sentence explaining its contribution to skill construction, representation, use, evaluation, or evolution. For foundational papers, describe the mechanism relevant to the taxonomy.
3. Use a direct paper page or publisher DOI. Add a code link when the authors' paper, project page, or repository establishes the connection. Record that evidence under `code_provenance`. Label project pages and datasets separately.
4. Update the relevant lists in `data/taxonomy.json`. A paper may occur in multiple categories; list it once within each category.
5. Update the synchronization date when incorporating a new survey snapshot.
6. Regenerate and check the catalogue:

   ```bash
   python3 scripts/build_readme.py
   python3 scripts/build_readme.py --check
   ```

When the manuscript source is available locally, also check every category against its corresponding figure node:

```bash
python3 scripts/build_readme.py --check --survey-source /path/to/arxiv/source
```

## Matching the survey

Keep the published category hierarchy when adding entries. In particular, synthesis methods and utilization have four direct categories; representations have secondary categories under structured, executable, and internalized skills; evaluation separates metrics and benchmarks; evolution has secondary categories under reorganization.

Use full titles and paper identifiers to distinguish similarly named systems, including SkillSmith, SkillFlow, SkillTrace, and GraSP/GRASP. Updated arXiv titles can differ from titles in the manuscript bibliography without indicating a different paper.

The README omits unconfirmed code links. An omitted link does not establish that no implementation exists. A repository referenced as a dependency or baseline is not the paper's implementation. If an author link becomes unavailable, retain its provenance in the data and remove it from the displayed `code_url` until resolved.

Check external links when adding or revising them. The local validator checks structure, coverage, and README consistency; it does not make network requests. Paper years initially follow the survey bibliography, with explicit corrections where primary publication records establish an error.
