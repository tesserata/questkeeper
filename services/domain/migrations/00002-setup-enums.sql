-- Enums
-- depends: 00001-init

CREATE DOMAIN questkeeper.game_system AS smallint
  CHECK (VALUE IN (0,1,2,3));

CREATE DOMAIN questkeeper.seat AS smallint
  CHECK (VALUE IN (0,1));

CREATE DOMAIN questkeeper.session_status AS smallint
  CHECK (VALUE IN (0,1,2,3,4));

CREATE DOMAIN questkeeper.app_role AS smallint
  CHECK (VALUE IN (0,1,2));
