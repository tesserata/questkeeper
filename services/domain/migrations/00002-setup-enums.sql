-- Enums
-- depends: 00001-init

CREATE DOMAIN questkeeper.game_system AS varchar
  CHECK (VALUE IN (
    'Pathfinder 1E',
    'Pathfinder 2E',
    'D&D 5E',
    'DSA 5E'
  ));

CREATE DOMAIN questkeeper.seat AS varchar
  CHECK (VALUE IN ('Main','Reserve'));

CREATE DOMAIN questkeeper.schedule_status AS varchar
  CHECK (VALUE IN ('Draft', 'Scheduled', 'Cancelled', 'Completed'));

CREATE DOMAIN questkeeper.app_role AS varchar
  CHECK (VALUE IN (
    'Server administrator',
    'Game master',
    'Player'
  ));
