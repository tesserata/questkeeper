-- Character history
-- depends: 00005-setup-characters

CREATE TABLE questkeeper.character_history (
  character_id  uuid FOREIGN KEY REFERENCES questkeeper.characters(character_id),
  session_id    uuid FOREIGN KEY REFERENCES questkeeper.sessions(session_id),
  event_id      uuid,
  created_at    timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (character_id, session_id)
);

CREATE INDEX ON questkeeper.character_history (character_id, created_at DESC);
CREATE INDEX ON questkeeper.character_history (session_id);