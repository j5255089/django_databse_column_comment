# django_er
1. generate ER by django modules use mermaid
2. auto add comment for columns of MySQL or PostgreSQL.the property `verbose_name`,`help_text`,`choices` of the django model will be used as ```comment``` for columns


## pre use
1. install the package
```
pip install git+https://github.com/j5255089/django_er.git
```

2. in `settings.py` add app
```
INSTALLED_APPS += [
    'django_er',
]
```

## generate ER
```
python manage.py er -o er.html auth
```
> `auth` is a app label

then open er.html with web browser

## add comment to database

### Database Supported

- MySQL
- PostgreSQL

### How to use

the model
```
name = models.CharField(max_length=200, verbose_name="名称", blank=True, default=None)
age = models.SmallIntegerField(verbose_name="年龄", blank=True, default=None)
```

next, type command
```
python manage.py addcomments
```

finally, the info will be printed, all the models created will be processed
```
## MySQL 
-- FOR test_student.name 
        ALTER TABLE test_student
        MODIFY COLUMN `name` varchar(200) COLLATE utf8mb4_bin NOT NULL  COMMENT '名称'
-- FOR test_student.age 
        ALTER TABLE test_student
        MODIFY COLUMN `age` smallint(6) NOT NULL  COMMENT '年龄'

## PostgreSQL
-- FOR test_student.name 
        COMMENT ON COLUMN test_student.name IS '名称'
-- FOR test_student.age 
        COMMENT ON COLUMN test_student.age IS '年龄'

```

## If any bug
you can fix by yourself or commit your issue here, I will fix it
