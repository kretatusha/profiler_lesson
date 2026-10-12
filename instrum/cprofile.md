Какой разговор о профилировании питона обходится без описания cProfile — одного из стандартных модулей Python?

```bash
python -m cProfile -s time run_code.py 10001
```

```bash
python -m cProfile -o run_code.prof run_code.py 10001
```