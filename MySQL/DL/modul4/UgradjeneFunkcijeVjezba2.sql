select count(users.name),statuses.name from users join statuses on users.
status = statuses.id group by statuses.name;
