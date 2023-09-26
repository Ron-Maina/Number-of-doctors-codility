def solution(A):
    new_array = []
    
    # doctors in more than one hospital
    doctors = []

    for sub_array in A:
        new_array = new_array + list(set(sub_array))

    for doctor in new_array:
        # checking the occurrence of elements
        count = new_array.count(doctor)
        if count > 1:
            if doctor not in doctors:
                doctors.append(doctor)
                
    print(f'Doctors in more than one hospital: {doctors}')
    print(f'Number of doctors in more than one hospital: {len(doctors)}')


solution([ [1, 1, 5, 2, 3], [4, 5, 6, 4, 3], [9, 4, 4, 1, 5] ])
solution([ [1, 2, 2], [3, 1, 4] ])
solution([ [4, 3], [5, 5], [6, 2] ])