create table Users(
	user_id	int primary key,
	user_name varchar(20) not NULL,
	age date not NULL,
	weight int not NULL,
	activity int not NULL);
	
create table Complex(
	complex_name varchar(20) primary key);

create table Messenger(
	messenger_name varchar(20) primary key);
	
create table Exercise(
	exercise_name varchar(20) primary key,
	time_length int not NULL,
	kcal int not NULL);

create table User_has_messenger(
	messenger_name varchar(10) not NULL references Messenger(messenger_name),
	user_id	int not NULL references Users(user_id) ,
	address varchar(20) not NULL,
	primary key (messenger_name,user_id));

create table Complex_has_exercise(
	complex_name varchar(20) not NULL references Complex(complex_name),
	exercise_name varchar(20) not NULL references Exercise(exercise_name),
	repeater int not NULL,
	primary key (complex_name,exercise_name));

create table User_do_complex(
	user_id	int not NULL references Users(user_id),
	complex_name varchar(20) not NULL references Complex(complex_name),
	time_start datetime not NULL,
	status varchar(10) not NULL,
	primary key (complex_name,user_id,time_start));
