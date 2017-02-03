--
-- Create model Course
--
CREATE TABLE course (
    number varchar(5) NOT NULL PRIMARY KEY,
    title varchar(10) NOT NULL,
    credits integer NOT NULL
);

CREATE TABLE professor (
    id serial NOT NULL PRIMARY KEY,
    first_name varchar(10) NOT NULL,
    last_name varchar(10) NOT NULL,
    departament varchar(10) NOT NULL,
    salary integer NOT NULL,
    rank varchar(10) NOT NULL,
    age integer NOT NULL
);

ALTER TABLE teach
    ADD CONSTRAINT "teach_course_id_bebbbd64_fk_course_number"
    FOREIGN KEY (course_id) REFERENCES course ("number")
    DEFERRABLE INITIALLY DEFERRED;