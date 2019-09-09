CREATE TABLE RefereeGame (
	MatchId int(10) NOT NULL,
	RefereeId int(10) NOT NULL,
	RefereeName varchar(100),
	PRIMARY KEY(MatchId, RefereeId)
)

CREATE TABLE PlayerGame(
	MatchId int(10) NOT NULL,
	PlayerId int(10) NOT NULL,
	ShirtNo int(3),
	PlayerName varchar(100),
	Position varchar(8),
	Started int(1),
	SubOutPlayerId int(10),
	SubInMinute int(3),
	SubInHalf varchar(12),
	Height int(3),
	Weight int(3),
	Age int(3),
	ManOfMatch varchar(5),
	Field varchar(4),
	PRIMARY KEY(MatchId, PlayerId)
)

CREATE TABLE Game(
	MatchId int(10) NOT NULL,
	League varchar(100),
	Season varchar(12),
	VenueName varchar(100),
	Attendance int(6),
	StartDate datetime,
	StartTime datetime,
	WeatherCode int(2),
	HomeTeamId int(10) NOT NULL,
	HomeTeamName varchar(100),
	HomeTeamManager varchar(100),
	HomeAvgAge double, 
	AwayTeamId int(10) NOT NULL,
	AwayTeamName varchar(100),
	AwayTeamManager varchar(100),
	AwayAvgAge double,
	HomeGoals int(2),
	AwayGoals int(2),
	HomeHTGoals int(2),
	AwayHTGoals int(2),
	HomeFTGoals int(2),
	AwayFTGoals int(2),
	PRIMARY KEY(MatchId, HomeTeamId, AwayTeamId)
)

CREATE TABLE Events(
	MatchId int(10) NOT NULL,
	EventId int(20),
	EventMatchId int(10),
	Minute int(3),
	Second int(2),
	TeamId int(10),
	PlayerId int(10),
	StartX double,
	EndX double,
	StartY double,
	EndY double,
	Half varchar(12),
	Type varchar(100),
	Outcome varchar(100)
)