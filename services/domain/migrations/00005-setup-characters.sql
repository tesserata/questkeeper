-- Characters
-- depends: 00004-setup-sessions

CREATE TABLE questkeeper.characters (
  character_id  uuid PRIMARY KEY DEFAULT gen_random_uuid(),,
  user_id       bigint NOT NULL,

  system        questkeeper.game_system NOT NULL,

  level         integer NOT NULL DEFAULT 1 CHECK (level >= 0),
  name          text NOT NULL,
  race          text,
  class         text,
  subclass      text,
  notes         text,

  version       bigint NOT NULL DEFAULT 0,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX ON questkeeper.characters (user_id);
CREATE INDEX ON questkeeper.characters (system);