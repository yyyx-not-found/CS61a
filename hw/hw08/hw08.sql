CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
    WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name FROM dogs AS a, parents, dogs AS b
    WHERE a.name=parents.child AND b.name=parents.parent
    ORDER BY b.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS a, b.child AS b
    FROM parents AS a, parents AS b
    WHERE a.child<b.child AND a.parent=b.parent;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a||" and "||b||" are "||size_a.size||" siblings"
    FROM siblings, size_of_dogs AS size_a, size_of_dogs AS size_b
    WHERE a=size_a.name AND b=size_b.name AND size_a.size=size_b.size;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper 
  SELECT name, height, height, 1 FROM dogs;

INSERT INTO stacks_helper
  SELECT dogs||", "||name, stack_height+height, height, 2
    FROM stacks_helper, dogs WHERE height>last_height;

INSERT INTO stacks_helper
  SELECT dogs||", "||name, stack_height+height, height, 3
    FROM stacks_helper, dogs WHERE height>last_height AND n=2;

INSERT INTO stacks_helper
  SELECT dogs||", "||name, stack_height+height, height, 4
    FROM stacks_helper, dogs WHERE height>last_height AND n=3;


CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper
    WHERE stack_height>=170 AND n=4 ORDER BY stack_height;

