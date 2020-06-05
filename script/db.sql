create table users
(
    id bigint(20) not null auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    primary key(id)
);

insert into users (first_name,last_name) values ('achmad','soekarno');
insert into users (first_name,last_name) values ('mohammad','hatta');

