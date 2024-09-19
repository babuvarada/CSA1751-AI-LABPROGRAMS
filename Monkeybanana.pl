% Initial state: monkey is at 'floor', box is at 'room_corner', banana is hanging from the ceiling, and the monkey does not have the banana.

% Define initial state
state(at_floor, at_room_corner, at_room_corner, no_banana).

% Actions:
% move the monkey to a new position
move(state(at_floor, MonkeyPos, BoxPos, no_banana), move_to_box, state(at_floor, BoxPos, BoxPos, no_banana)).

% climb the box
move(state(at_floor, BoxPos, BoxPos, no_banana), climb_box, state(at_box, BoxPos, BoxPos, no_banana)).

% grab the banana
move(state(at_box, BoxPos, BoxPos, no_banana), grab_banana, state(at_box, BoxPos, BoxPos, has_banana)).

% Define a plan to achieve the goal (getting the banana)
plan(State, State, []). % If the current state is the goal state, the plan is empty.
plan(State1, GoalState, [Action|Actions]) :-
    move(State1, Action, State2),  % perform an action
    plan(State2, GoalState, Actions). % recursively find a plan from the new state

% Goal state: Monkey has the banana.
goal_state(state(_, _, _, has_banana)).

% Function to solve the problem
solve(Plan) :-
    state(InitialState),
    goal_state(GoalState),
    plan(InitialState, GoalState, Plan).
