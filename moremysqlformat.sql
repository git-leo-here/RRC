mysql> use ip_project;
Database changed
mysql> show tables;
+----------------------+
| Tables_in_ip_project |
+----------------------+
| exam                 |
| student              |
| subject              |
+----------------------+


mysql> desc exam_10C;
+----------+------------+------+-----+---------+-------+
| Field    | Type       | Null | Key | Default | Extra |
+----------+------------+------+-----+---------+-------+
| sub_code | varchar(3) | NO   |     | NULL    |       |
| roll_no  | int        | NO   |     | NULL    |       |
| marks    | int        | YES  |     | NULL    |       |
| test     | varchar(3) | NO   |     | NULL    |       |
+----------+------------+------+-----+---------+-------+


mysql> desc student;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| roll_no | int         | NO   | PRI | NULL    |       |
| name    | varchar(20) | NO   |     | NULL    |       |
| stream  | varchar(5)  | NO   |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+


mysql> desc subject;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| sub_code | varchar(3)  | NO   | PRI | NULL    |       |
| name     | varchar(30) | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
