SELECT quarter FROM scoring GROUP BY quarter HAVING SUM(points) > 10;

SELECT team, SUM(points) FROM scoring, players 
  WHERE player=name GROUP BY team