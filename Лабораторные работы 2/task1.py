src = not False and True or False and not True

# TODO расписать упрощение выражения

result = (not False and True) or (not False and not True)
result = ((not False) and True) or ((not False) and (not True))
result = ((not False) and True) or ((not False) and (not True)),
result = (True and True) or (True and False),
result = True or False
result = True
  # TODO подставить результат выражения

print(src == result)
