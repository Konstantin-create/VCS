"""
Tools for print help text in commands
Functions:
    - Get ignore template by name
"""

python = \
'''# Python ignores
# Cache
__pycache__

# Enviroments
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

def get_ignore_template(template: str) -> str:
    """Get ignore template by name"""
    if template not in templates:
        return None
    return templates[template]
