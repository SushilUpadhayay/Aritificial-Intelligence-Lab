% Facts
gender(sushil, male).
gender(sushila, female).
gender(aakash, male).
gender(pooja, female).

loves(sushil, pooja).
loves(aakash, pooja).
loves(sushil, sushila).
loves(sushila, aakash).

%Rules
jealous(X, Y):-
    loves(X, Z), loves(Y, Z),X \=Y, gender(X, GX), gender(Z, GZ), GX \=GZ.

