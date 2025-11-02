-- Server settings
-- depends: 00007-setup-signups

CREATE TABLE questkeeper.server_settings (
  server_id                        bigint PRIMARY KEY,
  default_announcement_channel_id  bigint,
  default_system                   questkeeper.game_system NOT NULL DEFAULT 1,  -- e.g., PATHFINDER_2E
  dm_notifications_enabled         boolean NOT NULL DEFAULT true,
  mentionable_roles                text[] NOT NULL DEFAULT '{}',

  version       bigint NOT NULL DEFAULT 0,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX ON questkeeper.server_settings (default_system);


CREATE TABLE questkeeper.server_role_mapping (
  server_id        bigint NOT NULL,
  discord_role_id  bigint NOT NULL,
  app_role         questkeeper.app_role NOT NULL,

  created_at       timestamptz NOT NULL DEFAULT now(),
  updated_at       timestamptz NOT NULL DEFAULT now(),

  PRIMARY KEY (server_id, discord_role_id),
  FOREIGN KEY (server_id) REFERENCES questkeeper.server_settings(server_id)
);

CREATE INDEX ON questkeeper.server_role_mapping (server_id);