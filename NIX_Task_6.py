"""
 Task_6:
Дана строка из имён, в формате "Денис, Олег, Вася, Петя,Дима,Женя".
Разбейте строку так, чтобы получился список имён.
Заметьте: после запятой не всегда есть пробел
(он не должен входить в имена, которые попадут в список)
"""


def get_list_names(mstr):
	mlist = []
	temp_word = ''

	for i in range(len(mstr)):
		if mstr[i] != ',' and mstr[i] != ' ':
			temp_word += mstr[i]
		if mstr[i] == ',' or i == len(mstr) - 1:
			mlist.append(temp_word)
			temp_word = ''
	return mlist


print(get_list_names("Денис, Олег, Вася, Петя,Дима,Женя"))
