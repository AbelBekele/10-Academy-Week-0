CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar,
  "role" varchar,
  "created_at" timestamp
);

CREATE TABLE "messages" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "timestamp" timestamp,
  "text" text,
  "reply_count" integer,
  "reaction_count" integer,
  "mention_count" integer
);

CREATE TABLE "channels" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "reactions" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "message_id" integer,
  "created_at" timestamp
);

CREATE TABLE "replies" (
  "id" integer PRIMARY KEY,
  "message_id" integer,
  "user_id" integer,
  "created_at" timestamp
);

ALTER TABLE "messages" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "reactions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "reactions" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");

ALTER TABLE "replies" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "replies" ADD FOREIGN KEY ("message_id") REFERENCES "messages" ("id");
