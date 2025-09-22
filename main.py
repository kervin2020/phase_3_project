#!/usr/bin/env python3
"""
Main entry point for the Library Management System
"""

import sys
import os

# Add the lib directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from cli import main

if __name__ == "__main__":
    main()
