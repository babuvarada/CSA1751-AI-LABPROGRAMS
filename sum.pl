% sum(N, Sum) succeeds if Sum is the sum of integers from 1 to N
sum(0, 0). % base case: sum of integers from 1 to 0 is 0
sum(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum(N1, SubSum),
    Sum is N + SubSum.
