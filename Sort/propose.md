# Покрытие видов сортировок

**Все основные виды сортировок закрыты.** Подробные разборы — в
[README.md](README.md), таблица покрытия там же в §15.

## Что покрыто

```markdown
| Вид сортировки | Задача | Файл |
|---|---|---|
| Пузырьковая (Bubble) | 912 | e912_Bubble_Sort_an_Array.py |
| Выбором (Selection) | 2418 | e2418_Sort_the_People.py |
| Вставками (Insertion) | 147 | e147_Insertion_Sort_list.py |
| Пирамидальная (Heap) | 912 | e912_Bubble_Sort_an_Array.py |
| Слиянием (Merge) | 148 | e148_Sort_List.py |
| Быстрая (Quick) | 912 | e912_Bubble_Sort_an_Array.py |
| Quickselect | 215 | e215_Kth_Largest_Element_in_an_Array.py |
| Подсчётом (Counting) | 75 | e75_Sort_Colors.py |
| Поразрядная (Radix) | 164 | e164_Maximum_Gap_Radix_Sort.py |
| Блочная (Bucket) | 347, 451 | e347_Top_K_Frequent_Elements_Block_Sort.py, e451_Sort_Characters_By_Frequency_Bucket_sort.py |
| Timsort | 451, 2418 | e451_Sort_Characters_By_Frequency_Bucket_sort.py, e2418_Sort_the_People.py |
| Partition / голландский флаг | 905, 75 | e905_Sort_Array_By_Parity.py, e75_Sort_Colors.py |
```

| Вид сортировки | Задача | Файл |
|---|---|---|
| Пузырьковая (Bubble) | 912 | `e912_Bubble_Sort_an_Array.py` |
| Выбором (Selection) | 2418 | `e2418_Sort_the_People.py` |
| Вставками (Insertion) | 147 | `e147_Insertion_Sort_list.py` |
| Пирамидальная (Heap) | 912 | `e912_Bubble_Sort_an_Array.py` |
| Слиянием (Merge) | 148 | `e148_Sort_List.py` |
| Быстрая (Quick) | 912 | `e912_Bubble_Sort_an_Array.py` |
| Quickselect | 215 | `e215_Kth_Largest_Element_in_an_Array.py` |
| Подсчётом (Counting) | 75 | `e75_Sort_Colors.py` |
| Поразрядная (Radix) | 164 | `e164_Maximum_Gap_Radix_Sort.py` |
| Блочная (Bucket) | 347, 451 | `e347_...Block_Sort.py`, `e451_...Bucket_sort.py` |
| Timsort | 451, 2418 | `e451_...Bucket_sort.py`, `e2418_Sort_the_People.py` |
| Partition / голландский флаг | 905, 75 | `e905_Sort_Array_By_Parity.py`, `e75_Sort_Colors.py` |

Плюс две шпаргалки по схемам разбиения, на которых стоят quick sort и quickselect:
`hoar_scheme_partition.py` (схема Хоара) и `lomuto_scheme_devision.py` (схема Ломуто).

## Куда двигаться дальше

| Тема | Задача | Уровень | Ссылка | Зачем |
|---|---|---|---|---|
| Трёхпутевое разбиение | 75. Sort Colors | medium | https://leetcode.com/problems/sort-colors/ | голландский флаг как partition для quick sort на дубликатах |
| Top-k через кучу | 973. K Closest Points to Origin | medium | https://leetcode.com/problems/k-closest-points-to-origin/ | альтернатива bucket sort и quickselect |
| Слияние k списков | 23. Merge k Sorted Lists | hard | https://leetcode.com/problems/merge-k-sorted-lists/ | развитие 148: слияние `k` списков кучей |
| Слияние на месте | 88. Merge Sorted Array | easy | https://leetcode.com/problems/merge-sorted-array/ | фаза merge без доп. массива, см. `../TwoPointers` |
| Порядковые статистики | 462. Minimum Moves to Equal Array Elements II | medium | https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/ | медиана через quickselect за `O(n)` |

> ⚠️ **Про ссылки.** Большинство «учебных» сортировок формально сдаются на одной и
> той же задаче [912. Sort an Array](https://leetcode.com/problems/sort-an-array/),
> но там `n ≤ 5·10⁴`, поэтому все `O(n²)` алгоритмы (bubble, selection, insertion)
> получают **TLE**. Для них нужны задачи с маленьким входом — так, сортировка
> выбором сделана на 2418, где `n ≤ 1000`.
