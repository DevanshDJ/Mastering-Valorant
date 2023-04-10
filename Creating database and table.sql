drop database if exists Valorant;

create database if not exists Valorant;

use Valorant;

drop table if exists agent_stats;
Create table agent_stats
(
    Agent_Name		 		varchar(30) 	not null,
    Agent_Role 				varchar(30)		not null,
    Game_Type 				varchar(30)		not null,
    Map 					varchar(30)		not null,
    Game_Rank				varchar(30)		not null,
    KD						float			not null,
    K						float			not null,
    D						float			not null,
    A						float			not null,
    Win_Percent				float			not null,
    Pick_Percent			float			not null,
    Avg_Score				float			not null,
    First_Blood_Percent		float			not null,
    Matches					int				not null
);

select * from agent_stats;

Alter table agent_stats add primary key (Agent_Name, Game_Type, Map, Game_Rank);

create table ability_stats 
(
	Agent_Name		 		varchar(30) 	not null,
    Game_Type 				varchar(30)		not null,
    Map 					varchar(30)		not null,
    Game_Rank				varchar(30)		not null,
    1st_Ability				float			not null,
    2nd_Ability				float			not null,
    3rd_Ability				float			not null,
    Ultimate				float			not null,
    Matches					int				not null,
    Foreign key (Agent_Name, Game_Type, Map, Game_Rank) references agent_stats (Agent_Name, Game_Type, Map, Game_Rank)
);

select * from ability_stats;


Alter table ability_stats rename column 1st_Ability to First_Ability;
Alter table ability_stats rename column 2nd_Ability to Second_Ability;
Alter table ability_stats rename column 3rd_Ability to Third_Ability;



