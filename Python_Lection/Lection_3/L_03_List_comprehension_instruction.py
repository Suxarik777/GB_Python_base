# List comprehension

# быстрое создание списков

[exp for item in iterable] # выражение - некий итерируемый объект (в том числе список, словарь, range)
# на выходе получаем полноценный список

            # Выборка
[exp for item in iterable(if conditional)] # например вконце if - что конкретно мы выбираем

# последняя конструкция самая сложная но на начальном этапе лучше не использовать
# сложно читать
[exp <if conditional> for item in iterable(if conditional)]