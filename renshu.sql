CREATE TABLE student (
  student_id varchar(8) PRIMARY KEY,
  name varchar(256)
);

INSERT INTO student (student_id, name) VALUES ('2221000', '神奈川はなこ');

CREATE TABLE topic (
  id INT PRIMARY KEY,
  title TEXT
);

CREATE TABLE sentence (
  id INT PRIMARY KEY,
  sentence TEXT,
  audio_path TEXT,
  topic_id INT,
  FOREIGN KEY(topic_id) REFERENCES topic(id)
);