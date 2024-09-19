% Facts
parent(john, mary).
parent(mary, susan).
parent(susan, tom).

% Rules
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Queries for testing:
% ?- grandparent(john, tom).     % Expected result: true.
% ?- ancestor(john, tom).        % Expected result: true.
