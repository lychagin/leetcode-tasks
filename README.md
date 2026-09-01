# leetcode-tasks

Solving LeetCode problems.

Решения разложены по темам. В каждой папке лежит `README.md` с разбором: общие
приёмы темы, шаблоны кода, пошаговый разбор каждой задачи, сводная таблица
сложности и список частых ошибок.

| Тема | Задач | Ключевые приёмы |
|---|---|---|
| [BinarySearch](BinarySearch/README.md) | 10 | два шаблона цикла, поиск границы, бинарный поиск по ответу |
| [BitManipulation](BitManipulation/README.md) | 5 | XOR, маски, `n & (n - 1)` |
| [HashTables](HashTables/README.md) | 4 | словарь как индекс, счётчики, взаимно однозначное соответствие |
| [Intervals](Intervals/README.md) | 3 | сортировка по началу/концу, слияние, жадность |
| [LinkedList](LinkedList/README.md) | 8 | fast & slow, разворот на месте, dummy head |
| [Matrix](Matrix/README.md) | 5 | транспонирование, поворот, обход по слоям, диагонали |
| [PrefixSum](PrefixSum/README.md) | 5 | префиксные суммы 1D и 2D, префикс + хеш-таблица |
| [Sort](Sort/README.md) | 10 | все базовые сортировки, разбиение Ломуто и Хоара, heap/bucket/radix |
| [Tree](Tree/README.md) | 4 | обходы DFS, спуск по BST, перепривязка через возврат |
| [TwoPointers](TwoPointers/README.md) | 12 | встречные и попутные указатели, слияние, заполнение с конца |

`Other/` — черновики вне тем.

Тесты — `pytest` из корня репозитория:

```bash
python -m pytest -q
```
