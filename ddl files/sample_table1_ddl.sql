CREATE TABLE SAMPLE_TABLE
( 
   id                     bigint not null encode raw,
   user_type              varchar(32) encode text255,
   metric_type            varchar(32) encode text255,
   month                  smallint encode raw,
   year                   integer encode bytedict,
   location_country_name  varchar(32) encode text255,
   client                 varchar(32) encode text255,
   no_of_users            bigint encode bytedict,
   total_users            bigint encode bytedict,
   dataset_timestamp      timestamp not null encode delta32k,
   dataset_date           date not null encode delta32k
) 
diststyle all
sortkey (user_type);
