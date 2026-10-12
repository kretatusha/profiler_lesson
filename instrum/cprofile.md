Какой разговор о профилировании питона обходится без описания cProfile — одного из стандартных модулей Python?

```bash
python -m cProfile -s time run_code.py 10001
```

```bash
python -m cProfile -o run_code.prof run_code.py 10001
```

.prof — бинарный файл статистики cProfile. Откройте его встроенным модулем pstats:
```bash
python -m pstats instrum/get_prime_numbers.prof
```
Откроется интерактивная консоль. Полезные команды:
sort cumulative
stats 20
callers
callees
quit