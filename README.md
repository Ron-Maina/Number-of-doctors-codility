# Number-of-doctors-codility
* There are N hospitals, numbered from 0 to N−1. You are given a schedule of work in each of the hospitals for the following M days. The schedule is provided in the form of a two-dimensional array A containing N rows, each row representing the schedule of one hospital, and M columns, each column representing one day. Integer A[K][L] (for K within the range [0..N−1] and L within the range [0..M−1]) represents the ID of the doctor working at hospital K on day L. Note that sometimes an individual doctor may work at more than one hospital even on the same day.
Write a function:
int solution(int **A, int N, int M);
that, given a matrix A consisting of N rows and M columns representing the hospitals' schedules, finds the number of doctors working at more than one hospital.
Examples:

* Given A = [ [1, 2, 2], [3, 1, 4] ], the function should return 1.
The doctor with ID 1 works at both hospitals. The doctor with ID 2 works only at hospital number 0, while the doctors with IDs 3 and 4 work only at hospital number 1.

* Given A = [ [1, 1, 5, 2, 3], [4, 5, 6, 4, 3], [9, 4, 4, 1, 5] ], the function should return 4.
The doctors with IDs 1, 3, 4 and 5 work at more than one hospital.

* Given A = [ [4, 3], [5, 5], [6, 2] ], the function should return 0. 
* Each doctor works only at one hospital.

* Write an efficient algorithm for the following assumptions:
* N and M are integers within the range [1..1,000];
each element of matrix A is an integer within the range [1..N*M].