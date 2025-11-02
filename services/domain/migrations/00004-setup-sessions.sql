-- Sessions
-- depends: 00003-setup-events

CREATE TABLE questkeeper.sessions (
  session_id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),,
  server_id           bigint NOT NULL,
  event_id            uuid FOREIGN KEY REFERENCES questkeeper.events(event_id),
  gm_user_id          bigint NOT NULL,
  role_mentions       text[] NOT NULL DEFAULT '{}',

  title               text NOT NULL,
  summary             text NOT NULL DEFAULT '',
  system              questkeeper.game_system NOT NULL,

  vtt_link            text,
  location            text,
  additional_links    text[] NOT NULL DEFAULT '{}',

  starts_at           timestamptz NOT NULL,
  duration_minutes    integer NOT NULL CHECK (duration_minutes >= 0),
  timezone            text NOT NULL,

  capacity            integer NOT NULL CHECK (capacity >= 0),

  channel_id          bigint,
  message_id          bigint,

  status              questkeeper.session_status NOT NULL DEFAULT 0, -- DRAFT by default

  version             bigint NOT NULL DEFAULT 0,

  created_at          timestamptz NOT NULL DEFAULT now(),
  updated_at          timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX ON questkeeper.sessions (server_id);
CREATE INDEX ON questkeeper.sessions (gm_user_id);
CREATE INDEX ON questkeeper.sessions (event_id);
CREATE INDEX ON questkeeper.sessions (status);
CREATE INDEX ON questkeeper.sessions (starts_at);
CREATE INDEX ON questkeeper.sessions (server_id, status, starts_at);