desc student;
+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| admno   | int(11)     | NO   | PRI | NULL    | auto_increment |
| name    | varchar(30) | YES  |     | NULL    |                |
| fname   | varchar(30) | YES  |     | NULL    |                |
| class   | varchar(15) | YES  |     | NULL    |                |
| section | varchar(10) | YES  |     | NULL    |                |
| status  | char(15)    | YES  |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+

Students ka taale banana ke liye , tu alag se bana lia hai toh koi baat nhi and jab tu banega table toh jo jo chiz autoincrement main rehne ka zaroorat hai for example adm no. who sab apne aap hojaaega I guess

desc marks;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| admno   | int(11)     | YES  |     | NULL    |       |
| term    | varchar(20) | YES  |     | NULL    |       |
| session | varchar(20) | YES  |     | NULL    |       |
| phy     | int(3)      | YES  |     | NULL    |       |
| chem    | int(3)      | YES  |     | NULL    |       |
| math    | int(3)      | YES  |     | NULL    |       |
| eng     | int(3)      | YES  |     | NULL    |       |
| comp    | int(3)      | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
Yes marks display ka sample query
