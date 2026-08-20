# Непокрытые виды сортировок — что решать дальше

Актуальное покрытие папки `Sort` — см. §13 в [README.md](README.md).
Ниже — только то, на что **пока нет решённой задачи**, и предложения для тренировки.

## Таблица (raw markdown — можно копировать в трекер/заметки)

```markdown
| Вид сортировки | Задача | Уровень | Ссылка | Почему именно она |
|---|---|---|---|---|
| Быстрая сортировка (Quick Sort) | 912. Sort an Array | medium | https://leetcode.com/problems/sort-an-array/ | Третий метод в уже существующий файл рядом с bubble/heap. Обязателен рандомный пивот — иначе TLE на отсортированном тесте |
| Quickselect (k-й по величине) | 215. Kth Largest Element in an Array | medium | https://leetcode.com/problems/kth-largest-element-in-an-array/ | k-й элемент за `O(n)` в среднем без полной сортировки; фаза partition переиспользуется из quick sort |
```

## Отрендеренный вид

| Вид сортировки | Задача | Уровень | Ссылка | Почему именно она |
|---|---|---|---|---|
| Быстрая сортировка (Quick Sort) | 912. Sort an Array | medium | https://leetcode.com/problems/sort-an-array/ | Третий метод в уже существующий файл рядом с bubble/heap. Обязателен рандомный пивот — иначе TLE на отсортированном тесте |
| Quickselect (k-й по величине) | 215. Kth Largest Element in an Array | medium | https://leetcode.com/problems/kth-largest-element-in-an-array/ | k-й элемент за `O(n)` в среднем без полной сортировки; фаза partition переиспользуется из quick sort |

## Дополнительно (по желанию)

| Тема | Задача | Уровень | Ссылка |
|---|---|---|---|
| Top-k через кучу / quickselect с расстояниями | 973. K Closest Points to Origin | medium | https://leetcode.com/problems/k-closest-points-to-origin/ |
| Фаза merge без доп. массива | 88. Merge Sorted Array | easy | https://leetcode.com/problems/merge-sorted-array/ |

> ⚠️ **Про ссылки.** Большинство «учебных» сортировок формально можно сдать на одной
> и той же задаче [912. Sort an Array](https://leetcode.com/problems/sort-an-array/),
> но там `n ≤ 5·10⁴`, поэтому все `O(n²)` алгоритмы (bubble, selection, insertion)
> получают **TLE**. Для них нужны задачи с маленьким входом — так, сортировка
> выбором сделана на 2418, где `n ≤ 1000`.

## Уже покрыто (для контекста)

| Вид сортировки | Задача | Файл |
|---|---|---|
| Пузырьковая (Bubble) | 912 | `e912_Bubble_Sort_an_Array.py` |
| Выбором (Selection) | 2418 | `e2418_Sort_the_People.py` |
| Пирамидальная (Heap) | 912 | `e912_Bubble_Sort_an_Array.py` |
| Вставками (Insertion) | 147 | `e147_Insertion_Sort_list.py` |
| Слиянием (Merge) | 148 | `e148_Sort_List.py` |
| Подсчётом (Counting) | 75 | `e75_Sort_Colors.py` |
| Поразрядная (Radix) | 164 | `e164_Maximum_Gap_Radix_Sort.py` |
| Блочная (Bucket) | 347, 451 | `e347_Top_K_Frequent_Elements_Block_Sort.py`, `e451_Sort_Characters_By_Frequency_Bucket_sort.py` |
| Timsort | 451, 2418 | `e451_Sort_Characters_By_Frequency_Bucket_sort.py`, `e2418_Sort_the_People.py` |
| Partition / голландский флаг | 905, 75 | `e905_Sort_Array_By_Parity.py`, `e75_Sort_Colors.py` |
