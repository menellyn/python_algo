## РЕАЛИЗАЦИЯ БИНАРНОГО ДЕРЕВА ПОИСКА

### Типы ключевых пространств и информации

Ключ - "an unsigned integer".

Информация - "a string with variable length (null-terminated)".

---

- Узел дерева содержит ключ, указатели на правое и левое поддеревья и указатель на информационное поле.
- В таблице не могут храниться записи с одинаковыми ключами.

---

**Предусмотреть следующие операции:**

- Включение нового элемента в таблицу без нарушения свойств упорядоченности.
- Удаление  из  таблицы  элемента, заданного своим ключом, без нарушения свойств упорядоченности таблицы (если элементов несколько, то удаляется наиболее старый элемента).
- Поиск информации по заданному ключу; если элементов с одинаковым ключем может быть несколько, в качестве результата возвращаются все элементы с заданным ключем.
- Вывод всего содержимого таблицы в прямом порядке следования ключей, превышающих заданный (если ключ не указан - вывод всей таблицы).
- Поиск элемента, наиболее близкого по значению к заданному ключу, но не совпадающему с ним (если таких элементов несколько – действовать по аналогии с операцией поиска по ключу).