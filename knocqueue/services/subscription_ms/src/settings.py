import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MIGRATION_PATH = os.path.join(ROOT, *['..', 'migrations'])
