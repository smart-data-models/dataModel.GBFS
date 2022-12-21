/* (Beta) Export of data model gbfs of the subject dataModel.GBFS for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE gbfs_type AS ENUM ('gbfs');CREATE TYPE version_type AS ENUM ('2.1-RC', '2.1-RC2', 2.1, 2.2, '3.0-RC', 3.0);
CREATE TABLE gbfs (data json, id text, last_updated integer, ttl integer, type gbfs_type, version version_type);