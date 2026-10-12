
```bash
pip install plop
```

To profile an entire Python script, run:

```bash
python -m plop.collector run_code.py
```

This will write the profile to ./profiles/[timestamp]. Add -f flamegraph for flamegraph output.

To use the viewer for the default .plop output format, , run:

```bash
python -m plop.viewer --datadir=profiles
```