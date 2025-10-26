"""Main runner script for Codebase Genius."""
from agents.ingestion_agent import IngestionAgent
from agents.doc_agent import DocumentationAgent
from agents.qa_agent import QnAAgent
from agents.update_agent import UpdateAgent
import os


def run():
    """Main entry point for Codebase Genius."""
    print("🚀 Launching Codebase Genius...")

    root_dir = os.getcwd()
    ingestion_agent = IngestionAgent(root_dir=root_dir)
    doc_agent = DocumentationAgent()
    update_agent = UpdateAgent(doc_agent, ingestion_agent)

    # Step 1: Analyze and document
    print("📄 Generating documentation...")
    code_data = ingestion_agent.analyze_code()
    for file_path in code_data:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        file_name = os.path.basename(file_path).replace(".py", "")
        doc_agent.generate_doc(code, file_name)
    print("✅ Documentation generated!")


if __name__ == "__main__":
    run()
