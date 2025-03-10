CREATE TABLE business (
	business_id char(22),
	name varchar(60) NOT NULL,
	address varchar(75),
	city varchar(30) NOT NULL,
	postal_code varchar(7),
	stars decimal(2,1) CHECK (stars >= 1 AND stars <= 5),
	review_count int DEFAULT 0 CHECK (review_count >= 0),
	PRIMARY KEY (business_id)
);


CREATE TABLE checkin (
	checkin_id int,
	business_id char(22) NOT NULL FOREIGN KEY REFERENCES business(business_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(checkin_id)
);


CREATE TABLE user_yelp (
	user_id char(22),
	name varchar(35) NOT NULL,
	review_count int DEFAULT 0,
	yelping_since DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	useful int DEFAULT 0 CHECK (useful >= 0),
	funny int DEFAULT 0 CHECK (funny >= 0),
	cool int DEFAULT 0 CHECK (cool >= 0),
	fans int DEFAULT 0 CHECK (fans >= 0),
	average_stars decimal(3,2) CHECK (average_stars >= 1 AND average_stars <= 5)
	PRIMARY KEY (user_id)
);


CREATE TABLE tip (
	tip_id int,
	user_id char(22) NOT NULL FOREIGN KEY REFERENCES user_yelp(user_id),
	business_id char(22) NOT NULL FOREIGN KEY REFERENCES business(business_id),
	date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	compliment_count int DEFAULT 0 CHECK (compliment_count >= 0),
	PRIMARY KEY (tip_id)
);


CREATE TABLE friendship (
	user_id char(22) FOREIGN KEY REFERENCES user_yelp(user_id),
	friend char(22) FOREIGN KEY REFERENCES user_yelp(user_id),
	PRIMARY KEY (user_id, friend)
);


CREATE TABLE review (
	review_id char(22),
	user_id char(22) NOT NULL FOREIGN KEY REFERENCES user_yelp(user_id),
	business_id char(22) NOT NULL FOREIGN KEY REFERENCES business(business_id),
	stars int NOT NULL CHECK (stars >= 1 AND stars <= 5), 
	useful int DEFAULT 0 CHECK (useful >= 0),
	funny int DEFAULT 0 CHECK (funny >= 0),
	cool int DEFAULT 0 CHECK (cool >= 0),
	date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (review_id)
);

git 




BULK INSERT dbo.business
FROM  'd:\userdata\Data\business.csv'
WITH (fieldterminator = ',', rowterminator = '\n', firstrow = 2);

BULK INSERT dbo.checkin
FROM  'd:\userdata\Data\checkin.csv'
WITH (fieldterminator = ',', rowterminator = '\n', firstrow = 2);

BULK INSERT dbo.user_yelp
FROM  'd:\userdata\Data\user_yelp.csv'
WITH (fieldterminator = ',', rowterminator = '\n', firstrow = 2);

BULK INSERT dbo.tip
FROM  'd:\userdata\Data\tip.csv'
WITH (fieldterminator = ',', rowterminator = '\n', firstrow = 2);

BULK INSERT dbo.friendship
FROM  'd:\userdata\Data\friendship.csv'
WITH (fieldterminator = ',', rowterminator = '\n', firstrow = 2);

BULK INSERT dbo.review
FROM  'd:\userdata\Data\review.csv'
WITH (fieldterminator = ',', rowterminator = '\n', firstrow = 2);