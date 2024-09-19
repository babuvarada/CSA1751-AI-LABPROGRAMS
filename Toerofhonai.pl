% move(NumberOfDisks, SourcePeg, DestinationPeg, AuxiliaryPeg, Moves)
% Move NumberOfDisks from SourcePeg to DestinationPeg using AuxiliaryPeg
move(0, _, _, _, []) :- !.  % No disks to move
move(N, Source, Destination, Auxiliary, [Move|Moves]) :-
    N > 0,
    M is N - 1,
    move(M, Source, Auxiliary, Destination, Moves), % Move N-1 disks to auxiliary peg
    Move = move_disk(N, Source, Destination), % Move the Nth disk to destination peg
    move(M, Auxiliary, Destination, Source, Moves). % Move N-1 disks from auxiliary to destination

% Print the moves in a readable format
print_moves([]).
print_moves([move_disk(Disk, From, To)|Moves]) :-
    format('Move disk ~w from ~w to ~w~n', [Disk, From, To]),
    print_moves(Moves).

% Function to solve the Tower of Hanoi problem
tower_of_hanoi(N) :-
    move(N, source, destination, auxiliary, Moves),
    print_moves(Moves).
