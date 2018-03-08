CREATE SCHEMA IF NOT EXISTS myneect;
CREATE TABLE IF NOT EXISTS myneect.new_users(
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(200) NOT NULL,
  mail VARCHAR(100) NOT NULL UNIQUE,
  token CHAR(22) NOT NULL,
  token_used BOOLEAN NOT NULL DEFAULT FALSE
);