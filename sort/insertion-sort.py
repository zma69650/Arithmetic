
'''
insertion sort: 
when loop begins promise the orgin that tmp[i] exists
when loop continues promise that tmp[1-j] is ok
the loop can be halt 
'''

def insertion_sort(requied_sort_list):
	tmp = requied_sort_list	
	for j in range(1,len(tmp)):
		key = tmp[j]
                i = j - 1
                while i > 0 and tmp[i] > key:
			tmp[i+1] = tmp[i]
			i = i - 1
			tmp[i+1] = key
	return tmp
	
'''
first alter min from n-1 bacause there is one as reference
next alter min from n-2
...
'''
   												
def alter_sort(requied_sort_list):
	tmp = requied_sort_list
	for j in range(1,len(tmp)-1):
 		i = j + 1
		while i < len(tmp):
			if(tmp[j] > tmp[i]):
				key = tmp[i]
				tmp[i] = tmp[j]
				tmp[j] = key
			i = i + 1 
	return tmp		
	


'''
MERGE-sort

'''
def merge_sort(collection):

    def merge(left, right):
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

	




def main():
	s_list = [2,1,4,3]	
	print(merge_sort(s_list))
	





if __name__ == '__main__':
	main()
