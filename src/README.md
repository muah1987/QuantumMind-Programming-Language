# QuantumMind Framework - Source Code

This directory contains the complete source code implementation of the QuantumMind programming language framework.

## Structure Overview

- **core/**: Core type system, memory management, and fundamental utilities
- **compiler/**: Bootstrap compiler, lexer, parser, semantic analysis, and code generation
- **runtime/**: Execution engine, scheduler, coordination, and monitoring systems
- **quantum/**: Quantum computing backends, circuits, algorithms, and error correction
- **neural/**: Neural network architectures, training, inference, and interpretability
- **parallel/**: Parallel processing coordination, distribution, and hybrid systems
- **resources/**: Resource discovery, allocation, monitoring, and optimization
- **tools/**: Development tools, debugger, profiler, visualizer, and language server
- **cli/**: Command-line interface and utilities
- **stdlib/**: Standard library with quantum, neural, math, and utility functions

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Build the compiler: `python -m quantummind.compiler.bootstrap.transpiler`
3. Run examples: `python -m quantummind.cli.main run examples/getting_started/01_hello_quantum_world.qm`

## Development

See the development documentation in `docs/contributing/development_setup.md` for detailed setup instructions.