/* (Beta) Export of data model vehicle_types of the subject dataModel.GBFS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE vehicle_types_type AS ENUM ('vehicle_types');CREATE TYPE version_type AS ENUM ('2.1-RC','2.1','2.2','3.0-RC','3.0');
CREATE TABLE vehicle_types (data JSON, id TEXT PRIMARY KEY, last_updated INTEGER, ttl INTEGER, type vehicle_types_type, version version_type);