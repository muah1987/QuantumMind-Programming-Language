"""
Test cases for the QuantumMind bootstrap transpiler.
"""

import pytest
from pathlib import Path
import tempfile
import os

from quantummind.compiler.bootstrap.transpiler import QuantumMindTranspiler, TranspilerConfig


class TestQuantumMindTranspiler:
    """Test suite for the QuantumMind transpiler."""
    
    def test_transpiler_initialization(self):
        """Test transpiler can be initialized with default config."""
        transpiler = QuantumMindTranspiler()
        assert transpiler.config.target_language == "python"
        assert transpiler.config.optimize_quantum_circuits is True
    
    def test_transpiler_custom_config(self):
        """Test transpiler initialization with custom config."""
        config = TranspilerConfig(
            target_language="cpp",
            optimize_quantum_circuits=False,
            debug_mode=True
        )
        transpiler = QuantumMindTranspiler(config)
        assert transpiler.config.target_language == "cpp"
        assert transpiler.config.optimize_quantum_circuits is False
        assert transpiler.config.debug_mode is True
    
    def test_qubit_declaration_transpilation(self):
        """Test transpilation of qubit declarations."""
        transpiler = QuantumMindTranspiler()
        
        # Test basic qubit declaration
        source = "qubit q = |0⟩"
        result = transpiler._transpile_line(source)
        assert "q = qm.qubit('q', |0⟩)" in result
        
        # Test qubit with superposition
        source = "qubit superpos = |0⟩ + |1⟩"
        result = transpiler._transpile_line(source)
        assert "superpos = qm.qubit('superpos', |0⟩ + |1⟩)" in result
    
    def test_neural_net_declaration_transpilation(self):
        """Test transpilation of neural network declarations."""
        transpiler = QuantumMindTranspiler()
        
        source = "neural_net model = transformer(layers: 12)"
        result = transpiler._transpile_line(source)
        assert "model = qm.neural_net('model', transformer(layers: 12))" in result
    
    def test_resource_annotation_transpilation(self):
        """Test transpilation of resource annotations."""
        transpiler = QuantumMindTranspiler()
        
        source = "@resource(gpu: auto)"
        result = transpiler._transpile_line(source)
        assert "@qm.resource(gpu: auto)" in result
    
    def test_parallel_think_transpilation(self):
        """Test transpilation of parallel_think constructs."""
        transpiler = QuantumMindTranspiler()
        
        source = "result = parallel_think { ... }"
        result = transpiler._transpile_line(source)
        assert "await qm.parallel_think" in result
    
    def test_function_definition_transpilation(self):
        """Test transpilation of function definitions."""
        transpiler = QuantumMindTranspiler()
        
        source = "function quantum_process(input: tensor) -> result"
        result = transpiler._transpile_line(source)
        assert "def quantum_process(input: tensor) -> result" in result
    
    def test_conscious_block_transpilation(self):
        """Test transpilation of conscious blocks."""
        transpiler = QuantumMindTranspiler()
        
        source = "conscious function main() {"
        result = transpiler._transpile_line(source)
        assert "@qm.conscious" in result
    
    def test_comment_transpilation(self):
        """Test transpilation of comments."""
        transpiler = QuantumMindTranspiler()
        
        # Single line comment
        source = "// This is a comment"
        result = transpiler._transpile_line(source)
        assert "# This is a comment" in result
        
        # Empty line
        source = ""
        result = transpiler._transpile_line(source)
        assert result == ""
    
    def test_basic_syntax_replacements(self):
        """Test basic syntax symbol replacements."""
        transpiler = QuantumMindTranspiler()
        
        test_cases = [
            ("x → y", "x -> y"),
            ("x ← y", "x <- y"),
            ("|0⟩", "|0>"),
            ("⟨0|", "<0|"),
            ("x ≈ y", "x == y"),
            ("x ↔ y", "x <-> y"),
        ]
        
        for qm_syntax, expected_py in test_cases:
            result = transpiler._apply_basic_replacements(qm_syntax)
            assert expected_py in result
    
    def test_full_program_transpilation(self, sample_hybrid_program):
        """Test transpilation of a complete program."""
        transpiler = QuantumMindTranspiler()
        
        transpiled = transpiler.transpile_source(sample_hybrid_program)
        
        # Check that imports are added
        assert "import quantummind as qm" in transpiled
        assert "import numpy as np" in transpiled
        
        # Check that quantum constructs are transpiled
        assert "qm.qubit" in transpiled
        assert "qm.neural_net" in transpiled
        assert "await qm.parallel_think" in transpiled
    
    def test_file_transpilation(self):
        """Test transpilation of files."""
        transpiler = QuantumMindTranspiler()
        
        # Create a temporary source file
        source_content = """
        // Test QuantumMind program
        qubit q = |0⟩
        neural_net model = simple_net()
        
        function test() {
            return quantum_neural_process(q, model)
        }
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.qm', delete=False) as source_file:
            source_file.write(source_content)
            source_file.flush()
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as output_file:
                output_file.close()  # Close so transpiler can write to it
                
                # Test transpilation
                success = transpiler.transpile_file(source_file.name, output_file.name)
                assert success is True
                
                # Check output file content
                with open(output_file.name, 'r') as f:
                    transpiled_content = f.read()
                
                assert "import quantummind as qm" in transpiled_content
                assert "qm.qubit('q'" in transpiled_content
                
                # Cleanup
                os.unlink(source_file.name)
                os.unlink(output_file.name)
    
    def test_transpilation_error_handling(self):
        """Test error handling in transpilation."""
        transpiler = QuantumMindTranspiler()
        
        # Test with non-existent source file
        success = transpiler.transpile_file("nonexistent.qm", "output.py")
        assert success is False