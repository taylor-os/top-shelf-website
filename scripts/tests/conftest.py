"""
conftest.py — add scripts/ to sys.path so tests can import expire_samples.
"""
import sys
import os

# scripts/tests/ → scripts/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
