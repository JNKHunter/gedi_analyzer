### Run Tests
`python -m unittest discover -s tests -p "test_*.py"`

### Conda
conda deactivate
conda activate scispacy

### Start worker
celery -A tasks worker --loglevel=INFO
