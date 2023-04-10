
#Most chosen players in each category
SELECT 
    Agent_name, Game_Type, map, Game_Rank, Matches
FROM
    agent_stats a
WHERE
    matches = (SELECT 
            MAX(matches)
        FROM
            agent_stats b
        WHERE
            a.Game_Type = b.Game_Type
                AND a.Map = b.Map
                AND a.Game_Rank = b.Game_Rank); 
