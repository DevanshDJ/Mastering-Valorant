#Combining Data from 2 tables
SELECT 
    a.Agent_name, a.Agent_Role, a.Game_Type, a.Map, a.Game_Rank, a.KD, a.K, a.D, a.A, a.Win_Percent, a.Pick_Percent,
    a.Avg_Score, a.First_Blood_Percent, a.Matches, b.First_Ability, b.Second_Ability, b.Third_Ability, b.Ultimate, b.Matches
FROM
    agent_stats a
        JOIN
    ability_stats b 
    ON 	   (a.Agent_name = b.Agent_name
        AND a.Game_Type = b.Game_Type
        AND a.Map = b.Map
        AND a.Game_Rank = b.Game_Rank);