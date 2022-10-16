CREATE DATABASE pagination;

USE pagination;

CREATE TABLE users (
  id int NOT NULL auto_increment,
  first_name varchar(255),
  last_name varchar(255),
  date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

INSERT INTO users (first_name, last_name, date_added)  VALUES ('Tyler', 'Spradley', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('David', 'Desmarais', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Miles', 'Harlow', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Becca', 'Kingman', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Rotana', 'Greger', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Cinzia', 'Derige', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Karen', 'Boyce', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Don', 'Ringer', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Dane', 'Schuette', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Melessa', 'Steinhauer', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Stefan', 'Hartmark', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Patrick', 'Hensley', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Ryan', 'Tavelli', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Maciej', 'Froehner', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Andrew', 'Edlin', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Victor', 'Hunsberger', now());
INSERT INTO users (first_name, last_name, date_added)
 VALUES ('Immanuel', 'Lackey', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Kelly', 'Fryzel', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Warren', 'Shipon', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Michael', 'Yathirajadasan', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Roman', 'Summerlin', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('John', 'Hullo', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Ian', 'Nordberg', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Rich', 'Ardinger', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Uli', 'Zubenko', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Cathy', 'Cheung', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Juliann', 'Glasier', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Ryan', 'Steel', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Douglas', 'Hunnie', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Heather', 'Trautmann', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Miranda', 'Lares', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Mark', 'Antiquera', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Nick', 'Ji', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Patrick', 'Walkinshaw', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Samuel', 'Jacobsen', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Jason', 'Fruhling', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Jacob', 'Seguel', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Shawn', 'Lervik', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Alfonso', 'Staib', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Sergio', 'Pellicer', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Brian', 'Martone', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Shellie', 'Jemielity', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('John', 'Threadgill', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Paul', 'Tannehill', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Lori', 'Loomis', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Muhammed', 'Knotts', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Allyson', 'Kjelstad', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Tara', 'Wigmanich', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Patrick', 'Baillargeon', now());
INSERT INTO users (first_name, last_name, date_added)  VALUES ('Louise', 'Sublewski', now());
