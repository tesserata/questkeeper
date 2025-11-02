-- Outbox
-- depends: 00009-idempotency-keys

CREATE TABLE questkeeper.outbox (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  aggregate_type   text NOT NULL,
  aggregate_id     text NOT NULL,
  event_type       text NOT NULL,
  payload          jsonb NOT NULL,
  headers          jsonb NOT NULL DEFAULT '{}',

  status           text NOT NULL DEFAULT 'pending',
  attempts         integer NOT NULL DEFAULT 0,
  available_at     timestamptz NOT NULL DEFAULT now(),
  next_attempt_at  timestamptz,
  last_error       text,

  created_at       timestamptz NOT NULL DEFAULT now(),
  updated_at       timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX ON questkeeper.outbox (status, available_at);
CREATE INDEX ON questkeeper.outbox (aggregate_type, aggregate_id);

CREATE TABLE questkeeper.outbox_dlq (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  original_outbox_id uuid,
  aggregate_type   text NOT NULL,
  aggregate_id     text NOT NULL,
  event_type       text NOT NULL,
  payload          jsonb NOT NULL,
  headers          jsonb NOT NULL DEFAULT '{}',
  error            text,
  created_at       timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX ON questkeeper.outbox_dlq (aggregate_type, created_at DESC);