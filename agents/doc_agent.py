"""Documentation Agent for generating documentation."""
import os


class DocumentationAgent:
    """Agent responsible for generating documentation for code."""
    
    def __init__(self, output_dir="docs"):
        """
        Initialize the DocumentationAgent.
        
        Args:
            output_dir: Directory where documentation will be saved
        """
        self.output_dir = output_dir
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_doc(self, code, file_name):
        """
        Generate documentation for a given code file.
        
        Args:
            code: The source code to document
            file_name: Name of the file (without extension)
        """
        # Create a simple documentation format
        doc_content = f"# Documentation for {file_name}\n\n"
        doc_content += "## Code Analysis\n\n"
        
        # Count lines
        lines = code.split('\n')
        doc_content += f"- Total lines: {len(lines)}\n"
        
        # Find functions
        functions = [line.strip() for line in lines if line.strip().startswith('def ')]
        if functions:
            doc_content += f"- Functions found: {len(functions)}\n"
            doc_content += "\n## Functions\n\n"
            for func in functions:
                doc_content += f"- `{func}`\n"
        
        # Find classes
        classes = [line.strip() for line in lines if line.strip().startswith('class ')]
        if classes:
            doc_content += f"\n## Classes\n\n"
            for cls in classes:
                doc_content += f"- `{cls}`\n"
        
        # Add original code
        doc_content += "\n## Source Code\n\n```python\n"
        doc_content += code
        doc_content += "\n```\n"
        
        # Save documentation
        doc_path = os.path.join(self.output_dir, f"{file_name}.md")
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(doc_content)
        
        print(f"📝 Generated documentation: {doc_path}")
