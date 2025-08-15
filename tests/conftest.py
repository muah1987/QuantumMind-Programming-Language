"""
QuantumMind Test Suite Configuration

Pytest configuration and shared test utilities for the QuantumMind framework.
"""

import pytest
import sys
import os
from pathlib import Path

# Add src directory to path for testing
sys.path.insert(0, str(Path(__file__).parent / "src"))

@pytest.fixture(scope="session")
def quantummind_runtime():
    """Fixture to provide a test QuantumMind runtime instance."""
    import quantummind as qm
    
    # Initialize with test configuration
    runtime = qm.initialize({
        'runtime': {
            'max_memory_gb': 2,
            'max_cpu_cores': 2,
            'enable_distributed': False
        },
        'quantum': {
            'default_backend': 'simulator',
            'max_qubits': 8
        },
        'neural': {
            'device': 'cpu',
            'mixed_precision': False
        }
    })
    
    yield runtime
    
    # Cleanup
    qm.shutdown()

@pytest.fixture
def sample_quantum_circuit():
    """Fixture providing a sample quantum circuit for testing."""
    return """
    // Sample quantum circuit
    qubit q1 = |0⟩
    qubit q2 = |0⟩
    
    hadamard(q1)
    cnot(q1, q2)
    
    measurement = observe(q1, q2)
    """

@pytest.fixture
def sample_neural_network():
    """Fixture providing a sample neural network for testing."""
    return """
    // Sample neural network
    neural_net model = transformer(
        layers: 2,
        hidden_size: 64,
        vocab_size: 100
    )
    
    input_data = tensor([1, 2, 3, 4])
    output = model.forward(input_data)
    """

@pytest.fixture
def sample_hybrid_program():
    """Fixture providing a sample hybrid quantum-classical program."""
    return """
    // Sample hybrid program
    qubit q = |0⟩
    neural_net model = simple_net(input_size: 2, output_size: 1)
    
    @resource(adaptive: true)
    result = parallel_think {
        quantum_branch: () -> quantum_feature_extraction(q),
        neural_branch: () -> model.forward([0.5, 0.3])
    }
    
    final_result = observe(result)
    """

# Test markers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "quantum: marks tests as requiring quantum simulation"
    )
    config.addinivalue_line(
        "markers", "neural: marks tests as requiring neural network frameworks"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "performance: marks tests as performance benchmarks"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow running"
    )

def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their location."""
    for item in items:
        # Mark quantum tests
        if "quantum" in str(item.fspath):
            item.add_marker(pytest.mark.quantum)
        
        # Mark neural tests
        if "neural" in str(item.fspath):
            item.add_marker(pytest.mark.neural)
        
        # Mark integration tests
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        
        # Mark performance tests
        if "performance" in str(item.fspath):
            item.add_marker(pytest.mark.performance)
            item.add_marker(pytest.mark.slow)