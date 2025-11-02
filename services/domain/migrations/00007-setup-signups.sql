-- Signups
-- depends: 00006-setup-character-history

CREATE TABLE questkeeper.signups (
  session_id    uuid FOREIGN KEY REFERENCES questkeeper.sessions(session_id),
  user_id       bigint NOT NULL,
  character_id  uuid FOREIGN KEY REFERENCES questkeeper.characters(character_id),
  seat          questkeeper.seat NOT NULL,

  version       bigint NOT NULL DEFAULT 0,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now(),

  PRIMARY KEY (session_id, user_id)
);

CREATE INDEX ON questkeeper.signups (session_id, seat);
CREATE INDEX ON questkeeper.signups (character_id);