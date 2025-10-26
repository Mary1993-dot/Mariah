"""Update Agent for managing code updates and documentation."""


class UpdateAgent:
    """Agent responsible for coordinating updates between documentation and code analysis."""
    
    def __init__(self, doc_agent, ingestion_agent):
        """
        Initialize the UpdateAgent.
        
        Args:
            doc_agent: DocumentationAgent instance
            ingestion_agent: IngestionAgent instance
        """
        self.doc_agent = doc_agent
        self.ingestion_agent = ingestion_agent
    
    def update_documentation(self):
        """
        Update documentation for all code files.
        
        Returns:
            Number of files documented
        """
        code_files = self.ingestion_agent.analyze_code()
        count = 0
        
        for file_path in code_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
                
                import os
                file_name = os.path.basename(file_path).replace(".py", "")
                self.doc_agent.generate_doc(code, file_name)
                count += 1
            except Exception as e:
                print(f"⚠️  Error processing {file_path}: {e}")
        
        return count
    
    def sync_changes(self):
        """Synchronize changes between code and documentation."""
        print("🔄 Synchronizing changes...")
        documented = self.update_documentation()
        print(f"✅ Synchronized {documented} files")
        return documented
