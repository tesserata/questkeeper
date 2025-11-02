-- Idempotency keys
-- depends: 00008-setup-server-settings

CREATE TABLE questkeeper.idempotency_keys (
  idempotency_key   text PRIMARY KEY,
  server_id         bigint NOT NULL,
  request_hash      text NOT NULL,
  status            text NOT NULL,
  response_code     integer,
  response_body_hash text,
  meta              jsonb NOT NULL DEFAULT '{}',
  created_at        timestamptz NOT NULL DEFAULT now(),
  locked_at         timestamptz,
  processed_at      timestamptz
);

CREATE INDEX ON questkeeper.idempotency_keys (server_id, created_at DESC);
