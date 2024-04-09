When you navigate through the maze, print the steps that you take in the following manner. An example output is shown below with explanation. Each line below ends with a new line.

 

Start at ( 2 , 0 ) – enter into the maze from the cell at (2,0) coordinates.

North North East East East Stuck at ( 0 , 3 ) – starting from cell at (2,0), navigate to the North cell at (1,0). Then navigate to North cell (0,0), East cell (0,1), East cell (0,2), East cell (0,3) until you are stuck. Note that the order of the directions of traversing is defined as North, East, South, West.

Back to ( 0 , 2 ) – Since you could not continue from the cell at (0,3), get back to the cell at (0,2) where you can take a different path.

South East Stuck at ( 1 , 3 ) – starting from the cell at (0,2), move to South cell (1,2). Then move to East cell at (1,3) where you are stuck.

Back to ( 1 , 2 ) – backtrack to cell at (1,2) where you can take a different path.

.…

Stuck at ( 7 , 13 ) – you are stuck at the cell (7,13)

Back to ( 8 , 13 ) – backtrack to cell at (8,13) where you can take a different path.

South South South Leaving at ( 11 , 13 ) - starting from the cell at (8,13), move to the South cell (9,13). Then move to the South cell at (10,13), and to the South cell (11,13) where you can leave the maze.

 

The expected output after traversing the above maze is below:


For example:

Result
Start at ( 2 , 0 )
North North East East East Stuck at ( 0 , 3 )
Back to ( 0 , 2 )
South East Stuck at ( 1 , 3 )
Back to ( 1 , 2 )
West Stuck at ( 1 , 1 )
Back to ( 1 , 2 )
Stuck at ( 1 , 2 )
Back to ( 0 , 2 )
Stuck at ( 0 , 2 )
Back to ( 0 , 1 )
Stuck at ( 0 , 1 )
Back to ( 0 , 0 )
Stuck at ( 0 , 0 )
Back to ( 1 , 0 )
Stuck at ( 1 , 0 )
Back to ( 2 , 0 )
East East Stuck at ( 2 , 2 )
Back to ( 2 , 1 )
South South South South East South South East North North North North North North East North North East East South East East North East East Stuck at ( 0 , 10 )
Back to ( 0 , 9 )
Stuck at ( 0 , 9 )
Back to ( 0 , 8 )
West Stuck at ( 0 , 7 )
Back to ( 0 , 8 )
Stuck at ( 0 , 8 )
Back to ( 1 , 8 )
South East East East South West West South West South South West North North West West West South South South South South East East South East South South Stuck at ( 12 , 7 )
Back to ( 11 , 7 )
Stuck at ( 11 , 7 )
Back to ( 10 , 7 )
Stuck at ( 10 , 7 )
Back to ( 10 , 6 )
South West North West West West South South West North North Stuck at ( 10 , 1 )
Back to ( 11 , 1 )
West South South East East East North North East South East East Stuck at ( 12 , 6 )
Back to ( 12 , 5 )
South East East East North East East North West West North East East North North North North North North East East North North East North North West West South East Stuck at ( 1 , 12 )
Back to ( 1 , 11 )
West West Stuck at ( 1 , 9 )
Back to ( 1 , 10 )
Stuck at ( 1 , 10 )
Back to ( 1 , 11 )
Stuck at ( 1 , 11 )
Back to ( 0 , 11 )
Stuck at ( 0 , 11 )
Back to ( 0 , 12 )
Stuck at ( 0 , 12 )
Back to ( 0 , 13 )
Stuck at ( 0 , 13 )
Back to ( 1 , 13 )
Stuck at ( 1 , 13 )
Back to ( 2 , 13 )
South South South Stuck at ( 5 , 13 )
Back to ( 4 , 13 )
Stuck at ( 4 , 13 )
Back to ( 3 , 13 )
Stuck at ( 3 , 13 )
Back to ( 2 , 13 )
Stuck at ( 2 , 13 )
Back to ( 2 , 12 )
Stuck at ( 2 , 12 )
Back to ( 3 , 12 )
Stuck at ( 3 , 12 )
Back to ( 4 , 12 )
Stuck at ( 4 , 12 )
Back to ( 4 , 11 )
Stuck at ( 4 , 11 )
Back to ( 4 , 10 )
Stuck at ( 4 , 10 )
Back to ( 5 , 10 )
West South South Stuck at ( 7 , 9 )
Back to ( 6 , 9 )
Stuck at ( 6 , 9 )
Back to ( 5 , 9 )
Stuck at ( 5 , 9 )
Back to ( 5 , 10 )
Stuck at ( 5 , 10 )
Back to ( 6 , 10 )
Stuck at ( 6 , 10 )
Back to ( 7 , 10 )
East North North East South South South East North North Stuck at ( 6 , 13 )
Back to ( 7 , 13 )
Stuck at ( 7 , 13 )
Back to ( 8 , 13 )
South South South Leaving at ( 11 , 13 )
