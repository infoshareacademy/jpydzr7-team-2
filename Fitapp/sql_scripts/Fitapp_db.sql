CREATE DATABASE Fitapp;

USE Fitapp;

CREATE TABLE IF NOT EXISTS Users
(
	id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    age SMALLINT NOT NULL,
    password VARCHAR(100),
    weight DECIMAL(5,2) NOT NULL,
    height INT NOT NULL,
    gender ENUM('M', 'K') NOT NULL,
    status ENUM('ACTIVE', 'NOT_ACTIVE') NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS User_bmi_history
(
	id INT NOT NULL,
    user_id INT NOT NULL,
    bmi_value FLOAT NOT NULL,
    category ENUM('Niedowaga', 'W normie', 'Nadwaga', 'Otyłość') NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS s_activity_type
(
	code VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    calories_per_minute INT NOT NULL,
    status ENUM('ACTIVE', 'NOT_ACTIVE') NOT NULL
);
ALTER TABLE s_activity_type
	ADD UNIQUE KEY code(code);

CREATE TABLE IF NOT EXISTS Trainings
(
	id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    activity_type VARCHAR(100) NOT NULL,
    duration INT NOT NULL,
    calories_burned INT NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT false,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (activity_type) REFERENCES s_activity_type(code)
);

CREATE TABLE IF NOT EXISTS Meals
(
	id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    meal_type ENUM('Śniadanie', 'Lunch', 'Obiad', 'Przekąska', 'Kolacja') NOT NULL,
    name VARCHAR(100) NOT NULL,
    calories INT NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

INSERT INTO s_activity_type (code, name, calories_per_minute) VALUES
('RUN', 'Bieganie', 12),
('WALK', 'Spacer', 4),
('GYM', 'Siłownia', 8),
('BIKE', 'Jazda na rowerze', 8),
('SWIM', 'Pływanie', 15),
('FITNESS', 'Fitness', 9),
('SQUASH', 'Gra w squasha', 17);

COMMIT;





