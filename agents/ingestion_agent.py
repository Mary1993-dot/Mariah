"""Ingestion Agent for analyzing code files."""
import os
from pathlib import Path


class IngestionAgent:
    """Agent responsible for ingesting and analyzing code files."""
    
    def __init__(self, root_dir):
        """
        Initialize the IngestionAgent.
        
        Args:
            root_dir: Root directory to analyze
        """
        self.root_dir = root_dir
    
    def analyze_code(self):
        """
        Analyze all Python files in the root directory.
        
        Returns:
            List of Python file paths found in the root directory
        """
        python_files = []
        
        # Walk through the directory structure
        for root, dirs, files in os.walk(self.root_dir):
            # Skip hidden directories and common non-code directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', 'env', 'node_modules']]
            
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    python_files.append(file_path)
        
        return python_files
