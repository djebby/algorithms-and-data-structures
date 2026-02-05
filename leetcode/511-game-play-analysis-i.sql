-- https://leetcode.com/problems/game-play-analysis-i/
CREATE TABLE IF NOT EXISTS Activity (player_id INT, device_id INT, event_date DATE, games_played INT);
TRUNCATE TABLE Activity;
INSERT INTO Activity VALUES (1, 2, '2016-03-01', 5), (1, 2, '2016-05-02', 6), (2, 3, '2017-06-25', 1), (3, 1, '2016-03-02', 0), (3, 4, '2018-07-03', 5);

-- PostgreSQL query statement below
SELECT player_id, min(event_date) as first_login
FROM Activity
GROUP BY player_id;
