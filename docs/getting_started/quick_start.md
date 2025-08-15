# QuantumMind Quick Start Guide

Get up and running with QuantumMind in minutes!

## 🎯 Prerequisites

- Python 3.8 or higher
- 8GB+ RAM (16GB+ recommended)
- Git
- Optional: GPU for neural network acceleration
- Optional: Access to quantum cloud services

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mupoese/QuantumMind-Programming-Language.git
cd QuantumMind-Programming-Language
```

### 2. Run the Installation Script
```bash
chmod +x scripts/installation/install-quantummind.sh
./scripts/installation/install-quantummind.sh
```

This script will:
- Create a Python virtual environment
- Install all required dependencies
- Set up quantum computing frameworks
- Install neural network libraries
- Configure the development environment

### 3. Activate the Environment
```bash
source venv/bin/activate
```

### 4. Verify Installation
```bash
quantummind --version
python -c "import quantummind; print('✅ QuantumMind installed successfully!')"
```

## 🚀 Your First Program

### Hello Quantum World
Create a file called `hello.qm`:

```quantummind
// hello.qm - Your first QuantumMind program
import quantummind as qm

conscious main() {
    print("🌟 Welcome to QuantumMind!")
    
    // Create a quantum superposition
    qubit q = |0⟩ + |1⟩ / √2
    print(f"Created qubit: {q}")
    
    // Apply a quantum gate
    hadamard(q)
    
    // Measure the qubit
    result = observe(q)
    print(f"Measurement result: {result}")
    
    // Create uncertainty
    maybe<string> greeting = maybe("Hello!", confidence: 0.9)
    
    if probably(greeting.confidence > 0.8) {
        print(f"High confidence: {greeting.value}")
    }
    
    print("✨ QuantumMind program completed!")
}
```

### Run the Program
```bash
quantummind run hello.qm
```

Expected output:
```
🌟 Welcome to QuantumMind!
Created qubit: <Qubit(|+⟩)>
Measurement result: 0
High confidence: Hello!
✨ QuantumMind program completed!
```

## 🧠 Neural Network Example

Create `neural_hello.qm`:

```quantummind
// neural_hello.qm - Neural network example
import quantummind as qm

conscious main() {
    print("🧠 Neural Network Example")
    
    // Create a simple neural network
    neural_net model = transformer(
        layers: 2,
        hidden_size: 64,
        vocab_size: 1000
    )
    
    print(f"Created model: {model}")
    
    // Create some input data
    input_text = "Hello, QuantumMind!"
    embedding = encode_text(input_text)
    
    // Forward pass
    output = model.forward(embedding)
    print(f"Model output shape: {output.shape}")
    
    print("🎉 Neural network example completed!")
}
```

Run with:
```bash
quantummind run neural_hello.qm
```

## ⚛️🧠 Hybrid Quantum-Neural Example

Create `hybrid_hello.qm`:

```quantummind
// hybrid_hello.qm - Quantum-AI hybrid computation
import quantummind as qm

conscious main() {
    print("⚛️🧠 Quantum-AI Hybrid Example")
    
    // Create quantum and neural components
    qubit q = |0⟩
    neural_net model = simple_net(input_size: 2, output_size: 1)
    
    // Parallel quantum-classical computation
    @resource(adaptive: true)
    result = parallel_think {
        quantum_branch: () -> {
            hadamard(q)
            measurement = observe(q)
            return f"Quantum: {measurement}"
        },
        
        neural_branch: () -> {
            input_data = tensor([0.5, 0.3])
            output = model.forward(input_data)
            return f"Neural: {output.item():.3f}"
        }
    }
    
    // Get the final result
    final_result = observe(result)
    print(f"🎊 Hybrid result: {final_result}")
    
    print("🚀 Hybrid computation completed!")
}
```

Run with:
```bash
quantummind run hybrid_hello.qm
```

## 🛠️ Development Mode

For active development, use the development mode with file watching:

```bash
quantummind dev --watch examples/
```

This will:
- Watch for file changes
- Automatically recompile and run programs
- Provide detailed error messages
- Enable hot reloading

## 📚 Next Steps

1. **Explore Examples**: Check out more examples in the `examples/` directory
2. **Read Documentation**: Browse the comprehensive docs in `docs/`
3. **Language Reference**: Learn about QuantumMind syntax and features
4. **Tutorials**: Follow step-by-step tutorials for advanced topics
5. **Community**: Join our community discussions and contribute

## 🔧 Configuration

### Custom Configuration
Create a `quantummind.yaml` file:

```yaml
# quantummind.yaml
runtime:
  max_memory_gb: 16
  max_cpu_cores: 8
  
quantum:
  default_backend: qiskit_aer
  max_qubits: 20
  
neural:
  device: cuda  # or cpu, mps
  mixed_precision: true
```

### Environment Variables
```bash
export QUANTUMMIND_CONFIG_PATH=./quantummind.yaml
export QUANTUMMIND_LOG_LEVEL=DEBUG
export QUANTUMMIND_ENV=development
```

## 🚨 Troubleshooting

### Common Issues

**ImportError: No module named 'quantummind'**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate
pip install -e .
```

**Quantum backend not found**
```bash
# Install quantum packages
pip install qiskit cirq pennylane
```

**CUDA out of memory**
```bash
# Use CPU for neural networks
export QUANTUMMIND_NEURAL_DEVICE=cpu
```

### Getting Help

- Check the [Troubleshooting Guide](../reference/troubleshooting_guide.md)
- Search [GitHub Issues](https://github.com/mupoese/QuantumMind-Programming-Language/issues)
- Ask in [GitHub Discussions](https://github.com/mupoese/QuantumMind-Programming-Language/discussions)

## 🎉 Congratulations!

You've successfully set up QuantumMind and run your first quantum-AI hybrid programs! 

Ready to explore the quantum-powered future of programming? 🚀⚛️🧠