
# Урок 10


# # Изменяем картеж
# #
# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# # print(ptl1)


# # Вложенный картеж (распаковываем)
# #
# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6))),
# )
# print(countries, end='\n\n')
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name, 'население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, 'население =', city_population)


#
