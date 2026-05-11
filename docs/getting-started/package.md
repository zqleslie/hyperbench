# Package structure

Hyperbench organization.

## Package structures

Hyperbench is organized as a Python package with the following structure:

```bash
.
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── hooks
│   │   └── .pre-commit-config.yaml
│   ├── labeler.yaml
│   ├── pull_request_template.md
│   └── workflows
│       ├── ci.yaml
│       ├── coverage.yaml
│       ├── docs.yaml
│       └── management.yaml
├── .gitignore
├── .venv
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
├── SECURITY.md
├── agents
│   ├── SKILLS.md
│   └── references
│       ├── package.md
│       ├── standard-lib.md
│       ├── testing.md
│       └── type-system.md
├── configs
├── docs
├── examples
│   ├── early_stopping.py
│   ├── ...
│   └── villain.py
├── hyperbench
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── dataset.py
│   │   ├── datasets
│   │   ├── hif.py
│   │   ├── loader.py
│   │   ├── sampling.py
│   │   └── supported_datasets.py
│   ├── hlp
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── common_neighbors_hlp.py
│   │   ├── gcn_hlp.py
│   │   ├── hgnn_hlp.py
│   │   ├── hgnnp_hlp.py
│   │   ├── hnhn_hlp.py
│   │   ├── hypergcn_hlp.py
│   │   ├── mlp_hlp.py
│   │   ├── nhp_hlp.py
│   │   ├── node2vec_common.py
│   │   ├── node2vecgcn_hlp.py
│   │   ├── node2vecslp_hlp.py
│   │   └── villain_hlp.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── common_neighbors.py
│   │   ├── gcn.py
│   │   ├── hgnn.py
│   │   ├── hgnnp.py
│   │   ├── hnhn.py
│   │   ├── hypergcn.py
│   │   ├── mlp.py
│   │   ├── nhp.py
│   │   ├── node2vec.py
│   │   └── villain.py
│   ├── nn
│   │   ├── __init__.py
│   │   ├── aggregator.py
│   │   ├── conv.py
│   │   ├── enricher.py
│   │   ├── loss.py
│   │   └── scorer.py
│   ├── tests
│   ├── train
│   │   ├── __init__.py
│   │   ├── latex_logger.py
│   │   ├── markdown_logger.py
│   │   ├── negative_sampler.py
│   │   ├── negative_sampling_scheduler.py
│   │   └── trainer.py
│   ├── types
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   ├── hdata.py
│   │   ├── hypergraph.py
│   │   └── model.py
│   └── utils
│       ├── __init__.py
│       ├── data_utils.py
│       ├── file_utils.py
│       ├── hif_utils.py
│       ├── nn_utils.py
│       ├── node_utils.py
│       ├── schema
│       ├── sparse_utils.py
│       └── url_utils.py
├── hyperbench_logs
│   ├── experiment_0
│   │   ├── common_neighbors
│   │   ├── comparison
│   │   └── mlp
├── pyproject.toml
├── uv.lock
└── zensical.toml
```

## Getting support
If you need help with using hyperbench, please check out the following resources:
- [Documentation](https://hyperbench.readthedocs.io/en/latest/): comprehensive guides, API reference, and examples.
- [GitHub Discussions](https://www.github.com/hypernetwork-research-group/hyperbench/discussions): ask questions, share ideas, and connect with the community.
- [GitHub Issues](https://www.github.com/hypernetwork-research-group/hyperbench/issues): report bugs or request features (please check existing issues first).

## Community

hyperbench is developed as an open-source project with contributions from researchers and practitioners in the field of hypergraph learning. We welcome contributions of all kinds, including code, documentation, examples, and discussions.
If you’re interested in contributing, please visit the [contributing guide](https://www.github.com/hypernetwork-research-group/hyperbench/blob/main/CONTRIBUTING.md) for more information on how to get involved.

## Development team

@ddevin96
@tizianocitro

## Institutional partners

University of Salerno

## License

MIT license. See [LICENSE](https://github.com/hypernetwork-research-group/hyperbench/blob/main/LICENSE)
