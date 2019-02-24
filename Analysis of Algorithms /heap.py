import math
def max_heapify(input_list, index):
	try:
		left_index = left_child(index)
		right_index = right_child(index)
		
		if left_index <= len(input_list)-1 and right_index <= len(input_list)-1:
			if input_list[index] < input_list[left_index] and input_list[index] < input_list[right_index]:
				return input_list
			
			if input_list[left_index] < input_list[right_index]:
				input_list[left_index], input_list[index] = input_list[index], input_list[left_index]
				input_list = max_heapify(input_list, left_index)
			else:
				input_list[right_index], input_list[index] = input_list[index], input_list[right_index]
				input_list = max_heapify(input_list, right_index)
		if left_index <= len(input_list)-1 and right_index > len(input_list)-1:
			input_list[left_index], input_list[index] = input_list[index], input_list[left_index]
			input_list = max_heapify(input_list, left_index)
		return input_list
	except Exception as e:
		raise e

def build_max_heap(input_list):
	try:
		last_par = parent(len(input_list)-1)
		for i in range(last_par, -1 , -1):
			input_list = max_heapify(input_list, i)
		return input_list
	except Exception as e:
		raise e

def left_child(i):
	return (2*i)+1

def right_child(i):
	return (2*i)+2

def parent(i):
	return int(math.ceil(i)) -1

if __name__ == '__main__':
	ip_list = [4,3,10,2,9,7,6,1,5,8]
	print(build_max_heap(ip_list))