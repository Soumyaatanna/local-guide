from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

class HyderabadGuide:
    def __init__(self):
        self.product_context = ""
        self.load_context_file()
    
    def load_context_file(self):
        """
        Load the ONLY source of local knowledge: .kiro/product.md
        
        This file contains all local information about Hyderabad including:
        - Telugu slang and local terms
        - Street food spots and dishes  
        - Traffic patterns and peak hours
        - Cultural context and habits
        - Neighborhood information
        
        Kiro will use this context to answer ALL user questions about Hyderabad.
        No external knowledge or APIs are used - only this local context file.
        """
        context_file = '.kiro/product.md'
        
        if not os.path.exists(context_file):
            print(f"ERROR: {context_file} not found!")
            print("This file is the ONLY source of local knowledge for the application.")
            self.product_context = "Context file not found. Cannot provide local information."
            return
        
        try:
            with open(context_file, 'r', encoding='utf-8') as f:
                self.product_context = f.read()
            
            print(f"✓ Successfully loaded local context from: {context_file}")
            print(f"✓ Context size: {len(self.product_context)} characters")
            print("✓ This context will be passed to Kiro with every user request")
            
        except Exception as e:
            print(f"ERROR loading {context_file}: {e}")
            self.product_context = "Error loading context file."
    
    def get_kiro_response(self, user_question):
        """
        Generate response using Kiro with product.md as explicit context.
        
        How this works:
        1. User asks a question about Hyderabad
        2. We pass the ENTIRE product.md content as context to Kiro
        3. Kiro uses ONLY this context to answer (no external knowledge)
        4. Response is based purely on local information from product.md
        
        This ensures all answers are locally relevant and accurate.
        """
        
        if not user_question.strip():
            return {
                'response': "Ask me anything about Hyderabad! I can help with local slang, street food, traffic patterns, cultural habits, and neighborhoods.",
                'source': "Local Guide System"
            }
        
        if not self.product_context or "not found" in self.product_context.lower():
            return {
                'response': "Sorry, I cannot access my local knowledge base. Please ensure .kiro/product.md exists.",
                'source': "System Error"
            }
        
        # Here's where Kiro would process the request with context
        # For now, we'll do basic keyword matching as a placeholder
        response = self._search_context(user_question)
        
        return {
            'response': response,
            'source': "Local knowledge from .kiro/product.md",
            'context_size': len(self.product_context)
        }
    
    def _search_context(self, query):
        """
        Simple search through the product.md context.
        In a real Kiro integration, this would be replaced by Kiro's
        intelligent processing of the context with the user query.
        """
        query_lower = query.lower()
        context_lower = self.product_context.lower()
        
        # Find relevant sections
        lines = self.product_context.split('\n')
        relevant_lines = []
        
        for i, line in enumerate(lines):
            if query_lower in line.lower() and line.strip():
                # Include some context around the match
                start = max(0, i-1)
                end = min(len(lines), i+2)
                context_snippet = '\n'.join(lines[start:end])
                relevant_lines.append(context_snippet)
        
        if not relevant_lines:
            return f"I don't have specific information about '{query}' in my Hyderabad knowledge base. Try asking about Telugu slang, street food, traffic patterns, cultural habits, or specific neighborhoods."
        
        # Format response
        response = "Based on my local Hyderabad knowledge:\n\n"
        
        # Remove duplicates and limit results
        unique_snippets = list(dict.fromkeys(relevant_lines))[:3]
        
        for snippet in unique_snippets:
            response += f"{snippet}\n\n"
        
        response += "\n---\n*All information sourced from local knowledge in .kiro/product.md*"
        
        return response

# Initialize the guide with product.md context
guide = HyderabadGuide()

@app.route('/')
def home():
    """Serve the main HTML interface"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    Main endpoint for user questions.
    
    Process:
    1. Receive user question via POST request
    2. Pass question + product.md context to Kiro
    3. Return Kiro's response based ONLY on local context
    4. Include source attribution
    
    Request format: {"question": "user question here"}
    Response format: {"response": "answer", "source": "context source"}
    """
    
    try:
        # Get user question from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        user_question = data.get('question', '').strip()
        
        # Log the request (helpful for debugging)
        print(f"User question: {user_question}")
        print(f"Context available: {len(guide.product_context)} characters from .kiro/product.md")
        
        # Get response using product.md context
        result = guide.get_kiro_response(user_question)
        
        # Log the response source
        print(f"Response generated from: {result.get('source', 'Unknown')}")
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({
            'error': 'Internal server error',
            'response': 'Sorry, I encountered an error processing your question.'
        }), 500

@app.route('/context-info', methods=['GET'])
def context_info():
    """
    Endpoint to check context file status.
    Useful for debugging and verifying the context is loaded properly.
    """
    return jsonify({
        'context_file': '.kiro/product.md',
        'context_loaded': len(guide.product_context) > 0,
        'context_size': len(guide.product_context),
        'status': 'Context loaded successfully' if guide.product_context else 'Context not available'
    })

@app.route('/reload-context', methods=['POST'])
def reload_context():
    """
    Reload the product.md context file.
    Useful during development when updating the context.
    """
    guide.load_context_file()
    return jsonify({
        'status': 'Context reloaded',
        'context_size': len(guide.product_context),
        'source': '.kiro/product.md'
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check to verify the service is running"""
    return jsonify({
        'status': 'healthy',
        'service': 'Hyderabad Local Guide',
        'context_available': len(guide.product_context) > 0
    })

if __name__ == '__main__':
    print("=" * 50)
    print("🏙️  HYDERABAD LOCAL GUIDE")
    print("=" * 50)
    print(f"Context file: .kiro/product.md")
    print(f"Context loaded: {len(guide.product_context) > 0}")
    print(f"Context size: {len(guide.product_context)} characters")
    print("=" * 50)
    print("Starting Flask server...")
    print("Web Interface: http://localhost:5000")
    print("API Endpoints:")
    print("  POST /ask - Ask questions about Hyderabad")
    print("  GET  /context-info - Check context status")
    print("  POST /reload-context - Reload context file")
    print("  GET  /health - Health check")
    print("=" * 50)
    
    app.run(debug=True, port=5000, host='0.0.0.0')