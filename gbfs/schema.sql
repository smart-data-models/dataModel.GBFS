/* (Beta) Export of data model gbfs of the subject dataModel.GBFS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE gbfs_type AS ENUM ('gbfs');CREATE TYPE version_type AS ENUM ('2.1-RC','2.1-RC2','2.1','2.2','3.0-RC','3.0');
CREATE TABLE gbfs (data JSON, last_updated INTEGER, ttl INTEGER, type gbfs_type, version version_type);