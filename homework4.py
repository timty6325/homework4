import random
def knn_distance(arr, q, k):
	distances_tuples = []

	for element in arr:
		distance = abs(element - q)
		distances_tuples.append((distance, element))

	def partition(tuples, start, stop):
		pivot_ind = random.randint(start, stop)
		tuples[pivot_ind], tuples[stop] = tuples[stop], tuples[pivot_ind]

		middle_barrier = start
		end_barrier = start
		pivot_distance = tuples[stop][0]
	
		while end_barrier < stop:
			if tuples[end_barrier][0] <= pivot_distance:
				tuples[end_barrier], tuples[middle_barrier] = tuples[middle_barrier], tuples[end_barrier]
				middle_barrier += 1
				end_barrier += 1
			else:
				end_barrier +=1

		tuples[middle_barrier], tuples[stop] = tuples[stop], tuples[middle_barrier]

		return middle_barrier

	def quickselect(tuples, start, stop, target_index):
		while start <= stop:
			pivot_index = partition(tuples, start, stop)

			if pivot_index == target_index:
				return tuples[pivot_index]

			elif target_index < pivot_index:
				stop = pivot_index - 1
				
			else:
				start = pivot_index + 1
	target_index = k - 1

	return quickselect(distances_tuples, 0, len(distances_tuples) - 1, target_index)



			

			

		

	
	
	

		
