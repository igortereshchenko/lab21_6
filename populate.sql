INSERT INTO Users (user_id, user_name, age, weight, activity)
VALUES (1, 'Bob', '2000-01-18', 88, 8);

INSERT INTO Users (user_id, user_name, age, weight, activity)
VALUES (2, 'Boba', '2003-11-18', 90, 3);

INSERT INTO Users (user_id, user_name, age, weight, activity)
VALUES (3, 'Boben', '2000-05-19', 70, 10);

INSERT INTO Complex (complex_name)
VALUES ('morning start');

INSERT INTO Complex (complex_name)
VALUES ('hard sestem');

INSERT INTO Complex (complex_name)
VALUES ('for you');

INSERT INTO Messenger (messenger_name)
VALUES ('telegram');

INSERT INTO Messenger (messenger_name)
VALUES ('ukr.net');

INSERT INTO Messenger (messenger_name)
VALUES ('viber');

INSERT INTO Exercise (exercise_name, time_length, kcal)
VALUES ('push ups', 6, 4);

INSERT INTO Exercise (exercise_name, time_length, kcal)
VALUES ('squats', 3, 3);

INSERT INTO Exercise (exercise_name, time_length, kcal)
VALUES ('Superman', 10, 5);

INSERT INTO User_has_messenger (messenger_name, user_id, address)
VALUES ('ukr.net', 1, 'bobsuper@ukr.net');

INSERT INTO User_has_messenger (messenger_name, user_id, address)
VALUES ('telegram', 2, '@misterbobi');

INSERT INTO User_has_messenger (messenger_name, user_id, address)
VALUES ('telegram', 3, '@bobbbentop');

INSERT INTO Complex_has_exercise (complex_name, exercise_name, repeater)
VALUES ('for you', 'Superman', 20);

INSERT INTO Complex_has_exercise (complex_name, exercise_name, repeater)
VALUES ('for you', 'squats', 15);

INSERT INTO Complex_has_exercise (complex_name, exercise_name, repeater)
VALUES ('hard sestem', 'push ups', 100);

INSERT INTO User_do_complex ( user_id, complex_name, time_start, status)
VALUES (1, 'for you', '2019-10-25 23:59:59' 'rejected');

INSERT INTO User_do_complex ( user_id, complex_name, time_start, status)
VALUES (2, 'for you', '2019-10-25 23:59:59' 'rejected');

INSERT INTO User_do_complex ( user_id, complex_name, time_start, status)
VALUES (2, 'for you', '2019-10-25 13:00:00' 'done');