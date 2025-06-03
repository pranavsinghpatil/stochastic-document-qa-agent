"""
API Utilities

This module contains utility functions for the API endpoints.
"""
from typing import Dict, Any

def format_response(response_data: Dict[str, Any], status: str = "success") -> Dict[str, Any]:
    """
    Format API response in a consistent structure.
    
    Args:
        response_data (dict): The data to include in the response
        status (str): Status of the response (success/error)
        
    Returns:
        dict: Formatted response
    """
    return {
        "status": status,
        "data": response_data,
        "timestamp": "2025-06-02T19:00:00Z"  # TODO: Use actual timestamp
    }

def validate_question(question: str) -> bool:
    """
    Validate if the question is acceptable.
    
    Args:
        question (str): The question to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not question or not question.strip():
        return False
    return len(question.strip()) > 2
