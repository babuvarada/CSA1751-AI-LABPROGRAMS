% Planets facts: planet(Name, DistanceFromSunInMillionKm, DiameterInKm, HasMoons).
planet(mercury, 57.9, 4879, no).
planet(venus, 108.2, 12104, no).
planet(earth, 149.6, 12742, yes).
planet(mars, 227.9, 6779, yes).
planet(jupiter, 778.3, 139820, yes).
planet(saturn, 1427, 116460, yes).
planet(uranus, 2871, 50724, yes).
planet(neptune, 4495, 49244, yes).

% Rules to query the database:
% Find if a planet has moons
has_moons(Planet) :-
    planet(Planet, _, _, yes).

% Find planets within a certain distance from the Sun (in million km)
close_to_sun(Planet, MaxDistance) :-
    planet(Planet, Distance, _, _),
    Distance =< MaxDistance.

% Find planets larger than a certain diameter (in km)
larger_than(Planet, MinDiameter) :-
    planet(Planet, _, Diameter, _),
    Diameter > MinDiameter.

% Find planets by their names
find_planet(PlanetName) :-
    planet(PlanetName, Distance, Diameter, Moons),
    format('Planet: ~w, Distance from Sun: ~w million km, Diameter: ~w km, Has Moons: ~w~n', [PlanetName, Distance, Diameter, Moons]).
