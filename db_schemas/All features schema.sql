CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar,
  "role" varchar,
  "created_at" timestamp
);

CREATE TABLE "channels" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "messages" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "channel_id" integer,
  "text" text,
  "ts" timestamp,
  "reply_count" integer,
  "reaction_count" integer,
  "mention_count" integer
);

CREATE TABLE "replies" (
  "id" integer PRIMARY KEY,
  "message_id" integer,
  "user_id" integer,
  "ts" timestamp
);

CREATE TABLE "reactions" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "message_id" integer,
  "created_at" timestamp
);

CREATE TABLE "events" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "channel_id" integer,
  "message_id" integer,
  "reply_id" integer,
  "reaction_id" integer,
  "ts" timestamp,
  "time_difference_minutes" float
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

ALTER TABLE "replies" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "replies" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");

ALTER TABLE "reactions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "reactions" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");

ALTER TABLE "events" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "events" ADD FOREIGN KEY ("channel_id") REFERENCES "channels" ("id");

ALTER TABLE "events" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");

ALTER TABLE "events" ADD FOREIGN KEY ("reply_id") REFERENCES "replies" ("id");

ALTER TABLE "events" ADD FOREIGN KEY ("reaction_id") REFERENCES "reactions" ("id");
