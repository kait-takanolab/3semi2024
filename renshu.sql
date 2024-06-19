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

INSERT INTO topic (id, title) VALUES (1, "Artificial Intelligence");

INSERT INTO sentene (id, sentence, topic_id) VALUES(1, "Artificial intelligence (AI) is an information technology that functions like the human brain." ,1);