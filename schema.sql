drop table if exists user;
create table user (
  id integer primary key autoincrement,
  title text not null,
  ’text’ text not null
  first_name text not null,
  last_name text not null,
  username text not null,
  email text not null,
  password 
);
