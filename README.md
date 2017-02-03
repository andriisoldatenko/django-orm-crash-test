# Django ORM Crash tests
## Set of tests to check Django ORM



## How to run postgresql 
```bash
docker pull sameersbn/postgresql:9.6
```

```bash
docker run --name postgresql -itd --restart always \
  --publish 5432:5432 \
  --volume /Users/andrii/docker/postgresql:/var/lib/postgresql \
  --env 'DB_USER=university_user' --env 'DB_PASS=university_password' \
  --env 'DB_NAME=university_db' \
  sameersbn/postgresql:9.6
```

For more info please visit [docker-postgresql#getting-started](https://github.com/sameersbn/docker-postgresql#getting-started)
