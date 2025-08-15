# QuantumMind Examples

This directory contains examples demonstrating the capabilities of the QuantumMind programming language.

## Getting Started Examples

- `01_hello_quantum_world.qm` - Basic quantum and neural operations
- `02_first_neural_network.qm` - Simple neural network training
- `03_parallel_computation.qm` - Parallel processing examples
- `04_resource_management.qm` - Resource allocation examples
- `05_hybrid_quantum_classical.qm` - Quantum-classical hybrid algorithms

## Quantum Computing Examples

Basic quantum operations, algorithms, and error correction examples.

## Neural Networks Examples

Deep learning, training techniques, and model architectures.

## Running Examples

```bash
# Compile and run an example
quantummind run examples/getting_started/01_hello_quantum_world.qm

# Compile only
quantummind compile examples/getting_started/01_hello_quantum_world.qm

# Development mode with watching
quantummind dev --watch examples/
```

## Prerequisites

- QuantumMind framework installed
- Python 3.8+ with required dependencies
- Access to quantum simulators (optional for quantum examples)
- GPU access (optional for neural network examples)