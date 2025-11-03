-- Events
-- depends: 00002-setup-enums

CREATE TABLE questkeeper.events (
  event_id        uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  server_id       bigint NOT NULL,

  role_mentions   text[] NOT NULL DEFAULT '{}',

  title           text NOT NULL,
  summary         text NOT NULL DEFAULT '',
  system          questkeeper.game_system NOT NULL,

  time_start      timestamptz NOT NULL,
  time_end        timestamptz NOT NULL CHECK (ends_at >= starts_at),

  channel_id      bigint,
  message_id      bigint,

  status          questkeeper.event_status NOT NULL DEFAULT 0,

  version         bigint NOT NULL DEFAULT 0,
  created_at      timestamptz NOT NULL DEFAULT now(),
  updated_at      timestamptz NOT NULL DEFAULT now()
);


CREATE INDEX IF NOT EXISTS events_server_id_idx ON questkeeper.events (server_id);
CREATE INDEX IF NOT EXISTS events_status_idx     ON questkeeper.events (status);
CREATE INDEX IF NOT EXISTS events_time_idx       ON questkeeper.events (starts_at, ends_at);
CREATE INDEX IF NOT EXISTS events_server_status_start_idx
  ON questkeeper.events (server_id, status, starts_at);
