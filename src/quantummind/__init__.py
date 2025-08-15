"""
QuantumMind Programming Language Framework

A quantum-inspired programming language designed specifically for AI systems, 
combining quantum computing principles with natural language processing and 
machine learning paradigms.

This package provides:
- Quantum-aware type system with superposition variables
- AI-native neural network types and operations  
- Resource-aware parallel processing
- Hybrid quantum-classical execution
- Natural language integration
- Consciousness and introspection capabilities

Example:
    >>> import quantummind as qm
    >>> q = qm.qubit("my_qubit", "|0⟩")
    >>> model = qm.neural_net("my_model", "transformer")
    >>> result = qm.parallel_think({
    ...     "quantum": lambda: qm.quantum_algorithm(q),
    ...     "neural": lambda: model.forward(data)
    ... })
"""

__version__ = "1.0.0-alpha"
__author__ = "QuantumMind Development Team"
__license__ = "Apache 2.0 with Quantum Computing Extensions"

# Core imports
from .core import *
from .runtime.core.runtime_engine import QuantumMindRuntime
from .compiler.bootstrap.transpiler import QuantumMindCompiler

# High-level API
from .cli.main import QuantumMindAPI

# Initialize the framework
runtime = None

def initialize(config=None):
    """Initialize the QuantumMind runtime system."""
    global runtime
    if runtime is None:
        runtime = QuantumMindRuntime()
        runtime.initialize_system(config)
    return runtime

def get_runtime():
    """Get the current runtime instance."""
    global runtime
    if runtime is None:
        runtime = initialize()
    return runtime

# Convenience functions for common operations
def qubit(name, initial_state="|0⟩"):
    """Create a new qubit variable."""
    return get_runtime().core_engines.quantum_core.create_qubit(name, initial_state)

def neural_net(name, architecture):
    """Create a new neural network."""
    return get_runtime().core_engines.neural_core.create_neural_net(name, architecture)

def parallel_think(branches):
    """Execute parallel superposition of computation branches."""
    return get_runtime().core_engines.parallel_core.parallel_superposition("auto", branches)

def shutdown():
    """Gracefully shutdown the QuantumMind runtime."""
    global runtime
    if runtime is not None:
        runtime.shutdown()
        runtime = None