# genpark-conjugate-gradient-krylov-subspace-solver-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-conjugate-gradient-krylov-subspace-solver-skill?style=social)](https://github.com/alphaparkinc/genpark-conjugate-gradient-krylov-subspace-solver-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Conjugate Gradient Krylov Subspace Iterative Solver for SPD Linear Systems

Part of the **GenPark Autonomous Numerical Linear Algebra & Matrix Decompositions Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Symmetric Positive-Definite Linear System Ax = b] --> B[Initialize Initial Residual r_0 = b - Ax_0 and Search Direction p_0 = r_0]
    B --> C[Compute Matrix-Vector Product Ap_k]
    C --> D[Optimal Step Size alpha_k = r_k^T r_k / p_k^T A p_k]
    D --> E[Update State Vector x_{k+1} = x_k + alpha_k p_k]
    E --> F[Update Residual r_{k+1} = r_k - alpha_k A p_k]
    F --> G[Gram-Schmidt Conjugate Direction beta_k = r_{k+1}^T r_{k+1} / r_k^T r_k]
    G --> H[Update Search Direction p_{k+1} = r_{k+1} + beta_k p_k]
    H --> I{Residual Below Tolerance Epsilon?}
    I -->|No| C
    I -->|Yes| J[Exact Optimal Solution Vector x in <= N Iterations]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies (no NumPy or SciPy required).
- **Production-Grade Design**: Type annotations, partial pivoting, Gram-Schmidt stabilization.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-conjugate-gradient-krylov-subspace-solver-skill.git
cd genpark-conjugate-gradient-krylov-subspace-solver-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
