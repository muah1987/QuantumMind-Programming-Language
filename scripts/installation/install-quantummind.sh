#!/bin/bash
# QuantumMind Installation Script
# Installs the QuantumMind framework and its dependencies

set -e

echo "🚀 QuantumMind Framework Installation"
echo "====================================="

# Check Python version
echo "🐍 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
min_version="3.8.0"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "❌ Error: Python 3.8+ required. Found: $python_version"
    exit 1
fi
echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "📁 Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install core dependencies
echo "📚 Installing core dependencies..."
pip install -r requirements.txt

# Install quantum computing dependencies
echo "⚛️  Installing quantum computing frameworks..."
pip install qiskit cirq pennylane

# Install neural network dependencies
echo "🧠 Installing neural network frameworks..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install tensorflow jax jaxlib

# Install development dependencies
echo "🛠️  Installing development dependencies..."
pip install pytest black flake8 mypy jupyterlab

# Install QuantumMind in development mode
echo "🔧 Installing QuantumMind framework..."
pip install -e .

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p logs
mkdir -p build
mkdir -p data
mkdir -p models

# Run installation verification
echo "✅ Running installation verification..."
python3 -c "import quantummind; print('QuantumMind imported successfully')"

# Set up development environment
echo "🔧 Setting up development environment..."
if [ ! -f ".env" ]; then
    cat > .env << EOF
# QuantumMind Development Environment Configuration
QUANTUMMIND_ENV=development
QUANTUMMIND_LOG_LEVEL=DEBUG
QUANTUMMIND_CONFIG_PATH=config/development/
EOF
    echo "✅ Environment configuration created"
fi

echo ""
echo "🎉 QuantumMind installation completed successfully!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run a test program: quantummind run examples/getting_started/01_hello_quantum_world.qm"
echo "3. Start development server: quantummind dev --watch examples/"
echo "4. Read the documentation: docs/getting_started/quick_start.md"
echo ""
echo "For support, visit: https://github.com/mupoese/QuantumMind-Programming-Language"