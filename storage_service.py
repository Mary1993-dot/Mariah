def save_docs(repo_name: str, docs: dict):
    """Save documentation to files."""
    import os
    import json
    
    # Create output directory
    output_dir = f"output/{repo_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save documentation as JSON
    with open(f"{output_dir}/documentation.json", "w") as f:
        json.dump(docs, f, indent=2)
    
    print(f"[Storage] Documentation saved to {output_dir}")