# AI Evaluation Program

## Datasets
- grounded regulatory Q&A;
- ambiguous/missing-source questions;
- proposed-vs-effective status traps;
- numerical/calculation questions requiring tool use;
- Socratic coaching dialogues;
- misconception detection cases;
- English and Arabic equivalents;
- hostile/prompt-injection cases from retrieved documents.

## Metrics
- source/citation correctness;
- unsupported-claim rate;
- correct tool selection;
- calculation consistency;
- instructional helpfulness rubric;
- answer completeness;
- bilingual terminology consistency;
- response latency and cost.

Run evals on every prompt/model/retrieval/tool-policy change and on scheduled production samples with privacy-safe logging.
