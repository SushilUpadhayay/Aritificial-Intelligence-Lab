%base case
factorial(0, 1).
factorial(N, result):-
    N>0,
    N1 is N-1,
    factorial(N1, TempResult),
    result is N*TempResult.
