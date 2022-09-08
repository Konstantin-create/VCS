"""
Tools for print help text in commands
Functions:
    - Get ignore template by name
"""
# Imports
from __future__ import annotations  # For python < 3.10

python = \
    '''# Python ignores
    # Cache
    __pycache__
    
    # Environments
    venv/
    env/
    .venv/
    .env/
    
    # Pyinstaller
    .spec
    .manifest
    '''

templates = {
    'python': python
}


def get_ignore_template(template: str) -> str | None:
    """Get ignore template by name"""

    if template not in templates:
        return None
    return templates[template]
