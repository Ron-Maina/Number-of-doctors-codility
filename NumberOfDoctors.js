function solution(A){
    let new_array = []
    let doctors = []
    let  multiple_hospitals = []

    for (let sub_array of A){
        new_array = new_array.concat(Array.from(new Set(sub_array)))
    }
    new_array.forEach(element => {
        if (doctors.includes(element)){
            multiple_hospitals.push(element)

        } else {
            doctors.push(element)
        }
        
    })
    console.log((new Set(multiple_hospitals)).size)
    
}
solution([ [1, 1, 5, 2, 3], [4, 5, 6, 4, 3], [9, 4, 4, 1, 5] ])
solution([ [1, 2, 2], [3, 1, 4] ])
solution([ [4, 3], [5, 5], [6, 2] ])