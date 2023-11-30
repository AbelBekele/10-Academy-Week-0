CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar
);

CREATE TABLE "channels" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "messages" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "channel_id" integer,
  "timestamp" timestamp,
  "text" text,
  "subtype" varchar
);

CREATE TABLE "sentiment_analysis" (
  "id" integer PRIMARY KEY,
  "message_id" integer,
  "sentiment_score" float
);

CREATE TABLE "topic_modeling" (
  "id" integer PRIMARY KEY,
  "message_id" integer,
  "topic_id" integer,
  "word" varchar
);

ALTER TABLE "messages" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "messages" ADD FOREIGN KEY ("channel_id") REFERENCES "channels" ("id");

ALTER TABLE "sentiment_analysis" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");

ALTER TABLE "topic_modeling" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");
