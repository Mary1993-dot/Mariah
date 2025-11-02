"""Q&A Agent for answering questions about code."""


class QnAAgent:
    """Agent responsible for answering questions about code."""
    
    def __init__(self):
        """Initialize the QnAAgent."""
        self.knowledge_base = {}
    
    def add_knowledge(self, topic, information):
        """
        Add knowledge to the agent's knowledge base.
        
        Args:
            topic: Topic or key for the information
            information: Information to store
        """
        self.knowledge_base[topic] = information
    
    def answer_question(self, question):
        """
        Answer a question based on the knowledge base.
        
        Args:
            question: Question to answer
            
        Returns:
            Answer string or None if no answer found
        """
        # Simple keyword matching
        for topic, info in self.knowledge_base.items():
            if topic.lower() in question.lower():
                return info
        
        return "I don't have information about that topic."
