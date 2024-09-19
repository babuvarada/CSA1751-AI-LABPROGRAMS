% Database of people and their dates of birth

% Format: person(Name, date_of_birth(Day, Month, Year)).
person('John Doe', date_of_birth(15, june, 1990)).
person('Jane Smith', date_of_birth(22, august, 1985)).
person('Alice Johnson', date_of_birth(5, march, 1992)).
person('Bob Brown', date_of_birth(12, december, 2000)).

% Query to retrieve someone's DOB based on their name
get_dob(Name, Day, Month, Year) :-
    person(Name, date_of_birth(Day, Month, Year)).
