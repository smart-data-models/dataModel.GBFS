/* (Beta) Export of data model system_regions of the subject dataModel.GBFS for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE system_regions_type AS ENUM ('system_regions');CREATE TYPE version_type AS ENUM ('1.1-RC', 1.1, '2.0-RC', 2.0, '2.1-RC', '2.1-RC2', 2.1, 2.2, '3.0-RC', 3.0);
CREATE TABLE system_regions (data json, id text, last_updated integer, ttl integer, type system_regions_type, version version_type);