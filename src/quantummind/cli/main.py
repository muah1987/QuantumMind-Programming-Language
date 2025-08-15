#!/usr/bin/env python3
"""
QuantumMind Command Line Interface

Main entry point for the QuantumMind programming language CLI tools.
Provides compilation, execution, development, and deployment commands.
"""

import sys
import argparse
import os
from typing import List, Optional

# Add the src directory to the path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from quantummind import __version__
from .commands import compile_cmd, run_cmd, dev_cmd, pkg_cmd, system_cmd, docs_cmd, quantum_cmd, deploy_cmd

class QuantumMindCLI:
    """Main CLI application for QuantumMind."""
    
    def __init__(self):
        self.parser = self._create_parser()
        
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the main argument parser."""
        parser = argparse.ArgumentParser(
            prog='quantummind',
            description='QuantumMind Programming Language - Quantum-AI Hybrid Development Platform',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Examples:
  quantummind compile hello_world.qm          # Compile a QuantumMind program
  quantummind run hello_world.qm              # Compile and run a program
  quantummind dev --watch src/                # Development mode with file watching
  quantummind quantum --backends              # List available quantum backends
  quantummind system --status                 # Check system status
  quantummind deploy --cloud aws              # Deploy to cloud

For more information, visit: https://github.com/mupoese/QuantumMind-Programming-Language
            '''
        )
        
        parser.add_argument(
            '--version', 
            action='version', 
            version=f'QuantumMind {__version__}'
        )
        
        parser.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='Enable verbose output'
        )
        
        parser.add_argument(
            '--config', '-c',
            type=str,
            help='Path to configuration file'
        )
        
        # Create subparsers for commands
        subparsers = parser.add_subparsers(
            dest='command',
            help='Available commands',
            metavar='COMMAND'
        )
        
        # Add individual command parsers
        compile_cmd.add_parser(subparsers)
        run_cmd.add_parser(subparsers)
        dev_cmd.add_parser(subparsers)
        pkg_cmd.add_parser(subparsers)
        system_cmd.add_parser(subparsers)
        docs_cmd.add_parser(subparsers)
        quantum_cmd.add_parser(subparsers)
        deploy_cmd.add_parser(subparsers)
        
        return parser
    
    def run(self, args: Optional[List[str]] = None) -> int:
        """
        Run the CLI with the given arguments.
        
        Args:
            args: Command line arguments. If None, uses sys.argv
            
        Returns:
            Exit code (0 for success, non-zero for error)
        """
        try:
            parsed_args = self.parser.parse_args(args)
            
            # Handle case where no command is specified
            if not parsed_args.command:
                self.parser.print_help()
                return 1
            
            # Set up global configuration
            if parsed_args.verbose:
                import logging
                logging.basicConfig(level=logging.DEBUG)
            
            # Route to appropriate command handler
            command_handlers = {
                'compile': compile_cmd.handle,
                'run': run_cmd.handle,
                'dev': dev_cmd.handle,
                'pkg': pkg_cmd.handle,
                'system': system_cmd.handle,
                'docs': docs_cmd.handle,
                'quantum': quantum_cmd.handle,
                'deploy': deploy_cmd.handle,
            }
            
            handler = command_handlers.get(parsed_args.command)
            if handler:
                return handler(parsed_args)
            else:
                print(f"Unknown command: {parsed_args.command}")
                return 1
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return 130
        except Exception as e:
            print(f"Error: {e}")
            if parsed_args.verbose if 'parsed_args' in locals() else False:
                import traceback
                traceback.print_exc()
            return 1

def main() -> int:
    """Main entry point for the CLI."""
    cli = QuantumMindCLI()
    return cli.run()

if __name__ == '__main__':
    sys.exit(main())