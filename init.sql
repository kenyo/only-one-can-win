CREATE TABLE subreddits (
  ID SERIAL PRIMARY KEY,
  display_name VARCHAR(255) NOT NULL,
  subscribers INTEGER NOT NULL,
  active_user_count INTEGER NOT NULL,
  icon_img VARCHAR(255),
  timestamp TIMESTAMP
);
