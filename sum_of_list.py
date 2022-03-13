def sum_of_list(numbers):
	#sum_num = 0
	#for number in numbers:
	#	sum_num += number
	#return sum_num
	return sum(numbers)

list_sum=[]
while True:
	a = input('您要加總的數字為:(輸入完畢請輸入q)')
	if a == 'q':
		break
	a = int(a)
	list_sum.append(a)
print('數字總合為', sum_of_list(list_sum))
