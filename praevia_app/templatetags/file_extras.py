# /home/siisi/atmp/praevia_app/templatetags/file_extras.py

import os
from django import template

register = template.Library()


@register.filter
def basename(value):
    """Return the final component of a file path."""
    return os.path.basename(value)
