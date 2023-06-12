# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re
import pprint
text = 'Исследование специалистов из Университета Ноттингем Трент показало, что употребление 60 мл напитка \
с куркумой два раза в день ускоряет восстановление у спортсменов. Результаты исследования были опубликованы в журнале Frontiers in Nutrition.\
Активным ингредиентом куркумы является куркумин, который обладает противовоспалительными свойствами. Это снижает содержание провоспалительных \
белков в крови, которые повышаются в ответ на стресс, такой как интенсивные физические нагрузки. \
В работе приняли участие 24 профессиональных футболистов. Их разделили на две группы: первая употребляла напиток после матча, \
а вторая – нет. Болезненность в мышцах и маркеры воспаления в крови измерялись в течение трех дней после матча. Первая группа \
быстрее восстановилась чем группа, которая не употребляла куркуму.\
«Наше исследование показывает, что добавка с куркумой, употребляемая в виде небольшой порции напитка по 60 мл два раза в день, \
может уменьшить степень воспаления и болезненности мышц», – заключили авторы.'



my_dict = dict()
#\W — совпадает с не буквенным символом.
words = re.sub(r'\W', ' ', text).lower().split()
# print(words)
for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1



pprint.pprint(my_dict)