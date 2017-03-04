CREATE MULTISET TABLE drivers ,FALLBACK ,
     NO BEFORE JOURNAL,
     NO AFTER JOURNAL,
     CHECKSUM = DEFAULT,
     DEFAULT MERGEBLOCKRATIO
     (
      first_name VARCHAR (30),
      last_name VARCHAR (30),
      address VARCHAR (50),
      city VARCHAR (30),
      county VARCHAR (30),
      state VARCHAR (2),
      zip int,
      phone VARCHAR (12),
      email VARCHAR (50),
      driver_license VARCHAR (10),
      driving_behavior VARCHAR (20)
     )
PRIMARY INDEX ( zip )
UNIQUE INDEX (driver_license);

CREATE MULTISET TABLE image_results ,FALLBACK ,
     NO BEFORE JOURNAL,
     NO AFTER JOURNAL,
     CHECKSUM = DEFAULT,
     DEFAULT MERGEBLOCKRATIO
     (
      driver_license VARCHAR (10),
      image_results JSON(10000) CHARACTER SET LATIN COMPRESS USING TD_SYSFNLIB.JSON_COMPRESS DECOMPRESS USING TD_SYSFNLIB.JSON_DECOMPRESS,
      date_taken TIMESTAMP(6) default current_timestamp(6)
     )
PRIMARY INDEX ( date_taken );
