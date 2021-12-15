CREATE TABLE RANGER
(
   NUM              INT              not null AUTO_INCREMENT,
   PRESENCE         INT,
   DISTANCE         FLOAT,
   TEMPS			DATETIME,
   primary key (NUM)
);

CREATE TABLE REFERENCE 
(
   NUM              INT              not null AUTO_INCREMENT,
   DISTANCE         FLOAT,
   SON             INT,
   TEMPS            DATETIME,
   primary key (NUM)
);

CREATE TABLE SOUND 
(
   NUM              INT             not null AUTO_INCREMENT,
   SON             INT             not null,
   TEMPS            DATETIME,
   primary key (NUM)
);