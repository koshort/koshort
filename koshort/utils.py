"""Utility functions for text processing."""
import re
import importlib


def delete_links(string):
    """Delete links from input string
    
    Args:
        string (str): string to delete links
    
    Returns:
        str: string without links
    """

    return re.sub(r'http\S+', '', string)


def delete_mentions(string):
    """Delete at marks from input string
    
    Args:
        string (str): string to delete at marks
    
    Returns:
        str: string without at marks.
    """

    return re.sub(r'@\S+', '', string)
