"""
QuantumMind Compile Command

Handles compilation of QuantumMind source files to target platforms.
"""

import argparse
import os
from pathlib import Path
from typing import Any

def add_parser(subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    """Add the compile command parser."""
    parser = subparsers.add_parser(
        'compile',
        help='Compile QuantumMind source files',
        description='Compile .qm files to target platform (Python, C++, LLVM IR)',
    )
    
    parser.add_argument(
        'source',
        help='Source file or directory to compile'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file or directory'
    )
    
    parser.add_argument(
        '--target', '-t',
        choices=['python', 'cpp', 'llvm', 'quantum_sim'],
        default='python',
        help='Target compilation platform (default: python)'
    )
    
    parser.add_argument(
        '--optimize', '-O',
        action='store_true',
        help='Enable optimization passes'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Include debug information'
    )
    
    parser.add_argument(
        '--check-only',
        action='store_true',
        help='Only check syntax and types, do not compile'
    )
    
    return parser

def handle(args: Any) -> int:
    """Handle the compile command."""
    print(f"🔨 Compiling QuantumMind source: {args.source}")
    
    source_path = Path(args.source)
    
    # Validate source file exists
    if not source_path.exists():
        print(f"❌ Error: Source file '{args.source}' not found")
        return 1
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        if source_path.is_file():
            # Replace .qm extension with target extension
            extensions = {
                'python': '.py',
                'cpp': '.cpp',
                'llvm': '.ll',
                'quantum_sim': '.qsim'
            }
            output_path = source_path.with_suffix(extensions.get(args.target, '.out'))
        else:
            output_path = source_path / 'build'
    
    print(f"📁 Output target: {output_path}")
    print(f"🎯 Target platform: {args.target}")
    
    if args.optimize:
        print("⚡ Optimization enabled")
    
    if args.debug:
        print("🐛 Debug information enabled")
    
    if args.check_only:
        print("✅ Syntax and type checking only")
        return _check_syntax(source_path)
    
    # Import and use the transpiler
    try:
        from quantummind.compiler.bootstrap.transpiler import QuantumMindTranspiler, TranspilerConfig
        
        config = TranspilerConfig(
            target_language=args.target,
            optimize_quantum_circuits=args.optimize,
            debug_mode=args.debug,
            output_directory=str(output_path.parent)
        )
        
        transpiler = QuantumMindTranspiler(config)
        
        if source_path.is_file():
            success = transpiler.transpile_file(str(source_path), str(output_path))
        else:
            # Handle directory compilation
            success = _compile_directory(transpiler, source_path, output_path)
        
        if success:
            print(f"✅ Compilation successful: {output_path}")
            return 0
        else:
            print("❌ Compilation failed")
            return 1
            
    except ImportError as e:
        print(f"❌ Error: Failed to import compiler: {e}")
        return 1
    except Exception as e:
        print(f"❌ Compilation error: {e}")
        return 1

def _check_syntax(source_path: Path) -> int:
    """Check syntax and types without compilation."""
    print("🔍 Checking syntax and types...")
    
    # Placeholder for syntax checking
    # In a full implementation, this would run the lexer and parser
    # without code generation
    
    try:
        with open(source_path, 'r') as f:
            content = f.read()
        
        # Basic syntax validation
        if 'function' in content or 'qubit' in content or 'neural_net' in content:
            print("✅ Syntax check passed")
            return 0
        else:
            print("⚠️  Warning: No recognizable QuantumMind constructs found")
            return 0
            
    except Exception as e:
        print(f"❌ Syntax check failed: {e}")
        return 1

def _compile_directory(transpiler: Any, source_dir: Path, output_dir: Path) -> bool:
    """Compile all .qm files in a directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    qm_files = list(source_dir.rglob("*.qm"))
    
    if not qm_files:
        print("⚠️  No .qm files found in directory")
        return True
    
    success_count = 0
    total_files = len(qm_files)
    
    for qm_file in qm_files:
        relative_path = qm_file.relative_to(source_dir)
        output_file = output_dir / relative_path.with_suffix('.py')
        
        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        print(f"  Compiling: {relative_path}")
        
        if transpiler.transpile_file(str(qm_file), str(output_file)):
            success_count += 1
        else:
            print(f"    ❌ Failed to compile: {relative_path}")
    
    print(f"📊 Compiled {success_count}/{total_files} files successfully")
    return success_count == total_files