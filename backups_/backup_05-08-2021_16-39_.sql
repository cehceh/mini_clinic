BEGIN TRANSACTION;
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO "auth_permission" VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES(5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES(6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES(8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES(9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES(10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES(11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES(12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES(13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES(14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES(15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES(16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES(21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES(22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES(23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES(24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES(25,7,'add_pasthistory','Can add past history');
INSERT INTO "auth_permission" VALUES(26,7,'change_pasthistory','Can change past history');
INSERT INTO "auth_permission" VALUES(27,7,'delete_pasthistory','Can delete past history');
INSERT INTO "auth_permission" VALUES(28,7,'view_pasthistory','Can view past history');
INSERT INTO "auth_permission" VALUES(29,8,'add_patients','Can add patients');
INSERT INTO "auth_permission" VALUES(30,8,'change_patients','Can change patients');
INSERT INTO "auth_permission" VALUES(31,8,'delete_patients','Can delete patients');
INSERT INTO "auth_permission" VALUES(32,8,'view_patients','Can view patients');
INSERT INTO "auth_permission" VALUES(33,9,'add_presenthistory','Can add present history');
INSERT INTO "auth_permission" VALUES(34,9,'change_presenthistory','Can change present history');
INSERT INTO "auth_permission" VALUES(35,9,'delete_presenthistory','Can delete present history');
INSERT INTO "auth_permission" VALUES(36,9,'view_presenthistory','Can view present history');
INSERT INTO "auth_permission" VALUES(37,10,'add_medicine','Can add medicine');
INSERT INTO "auth_permission" VALUES(38,10,'change_medicine','Can change medicine');
INSERT INTO "auth_permission" VALUES(39,10,'delete_medicine','Can delete medicine');
INSERT INTO "auth_permission" VALUES(40,10,'view_medicine','Can view medicine');
INSERT INTO "auth_permission" VALUES(41,11,'add_visits','Can add visits');
INSERT INTO "auth_permission" VALUES(42,11,'change_visits','Can change visits');
INSERT INTO "auth_permission" VALUES(43,11,'delete_visits','Can delete visits');
INSERT INTO "auth_permission" VALUES(44,11,'view_visits','Can view visits');
INSERT INTO "auth_permission" VALUES(45,12,'add_labvisit','Can add lab visit');
INSERT INTO "auth_permission" VALUES(46,12,'change_labvisit','Can change lab visit');
INSERT INTO "auth_permission" VALUES(47,12,'delete_labvisit','Can delete lab visit');
INSERT INTO "auth_permission" VALUES(48,12,'view_labvisit','Can view lab visit');
INSERT INTO "auth_permission" VALUES(49,13,'add_labfollowup','Can add lab followup');
INSERT INTO "auth_permission" VALUES(50,13,'change_labfollowup','Can change lab followup');
INSERT INTO "auth_permission" VALUES(51,13,'delete_labfollowup','Can delete lab followup');
INSERT INTO "auth_permission" VALUES(52,13,'view_labfollowup','Can view lab followup');
INSERT INTO "auth_permission" VALUES(53,14,'add_remedicine','Can add remedicine');
INSERT INTO "auth_permission" VALUES(54,14,'change_remedicine','Can change remedicine');
INSERT INTO "auth_permission" VALUES(55,14,'delete_remedicine','Can delete remedicine');
INSERT INTO "auth_permission" VALUES(56,14,'view_remedicine','Can view remedicine');
INSERT INTO "auth_permission" VALUES(57,15,'add_revisits','Can add revisits');
INSERT INTO "auth_permission" VALUES(58,15,'change_revisits','Can change revisits');
INSERT INTO "auth_permission" VALUES(59,15,'delete_revisits','Can delete revisits');
INSERT INTO "auth_permission" VALUES(60,15,'view_revisits','Can view revisits');
INSERT INTO "auth_permission" VALUES(61,16,'add_operations','Can add operations');
INSERT INTO "auth_permission" VALUES(62,16,'change_operations','Can change operations');
INSERT INTO "auth_permission" VALUES(63,16,'delete_operations','Can delete operations');
INSERT INTO "auth_permission" VALUES(64,16,'view_operations','Can view operations');
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0));
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO "django_content_type" VALUES(1,'admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'auth','permission');
INSERT INTO "django_content_type" VALUES(3,'auth','group');
INSERT INTO "django_content_type" VALUES(4,'auth','user');
INSERT INTO "django_content_type" VALUES(5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'sessions','session');
INSERT INTO "django_content_type" VALUES(7,'pasthistory','pasthistory');
INSERT INTO "django_content_type" VALUES(8,'patientdata','patients');
INSERT INTO "django_content_type" VALUES(9,'presenthistory','presenthistory');
INSERT INTO "django_content_type" VALUES(10,'visitdrug','medicine');
INSERT INTO "django_content_type" VALUES(11,'visits','visits');
INSERT INTO "django_content_type" VALUES(12,'labs','labvisit');
INSERT INTO "django_content_type" VALUES(13,'labs','labfollowup');
INSERT INTO "django_content_type" VALUES(14,'revisitdrug','remedicine');
INSERT INTO "django_content_type" VALUES(15,'revisits','revisits');
INSERT INTO "django_content_type" VALUES(16,'patientdata','operations');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2021-07-27 20:09:58.726780');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2021-07-27 20:09:59.024004');
INSERT INTO "django_migrations" VALUES(3,'admin','0001_initial','2021-07-27 20:09:59.335028');
INSERT INTO "django_migrations" VALUES(4,'admin','0002_logentry_remove_auto_add','2021-07-27 20:09:59.512029');
INSERT INTO "django_migrations" VALUES(5,'admin','0003_logentry_add_action_flag_choices','2021-07-27 20:09:59.674042');
INSERT INTO "django_migrations" VALUES(6,'contenttypes','0002_remove_content_type_name','2021-07-27 20:09:59.879050');
INSERT INTO "django_migrations" VALUES(7,'auth','0002_alter_permission_name_max_length','2021-07-27 20:10:00.058748');
INSERT INTO "django_migrations" VALUES(8,'auth','0003_alter_user_email_max_length','2021-07-27 20:10:00.220745');
INSERT INTO "django_migrations" VALUES(9,'auth','0004_alter_user_username_opts','2021-07-27 20:10:00.358772');
INSERT INTO "django_migrations" VALUES(10,'auth','0005_alter_user_last_login_null','2021-07-27 20:10:00.501703');
INSERT INTO "django_migrations" VALUES(11,'auth','0006_require_contenttypes_0002','2021-07-27 20:10:00.615188');
INSERT INTO "django_migrations" VALUES(12,'auth','0007_alter_validators_add_error_messages','2021-07-27 20:10:00.737184');
INSERT INTO "django_migrations" VALUES(13,'auth','0008_alter_user_username_max_length','2021-07-27 20:10:00.892195');
INSERT INTO "django_migrations" VALUES(14,'auth','0009_alter_user_last_name_max_length','2021-07-27 20:10:01.048208');
INSERT INTO "django_migrations" VALUES(15,'auth','0010_alter_group_name_max_length','2021-07-27 20:10:01.215213');
INSERT INTO "django_migrations" VALUES(16,'auth','0011_update_proxy_permissions','2021-07-27 20:10:01.398817');
INSERT INTO "django_migrations" VALUES(17,'auth','0012_alter_user_first_name_max_length','2021-07-27 20:10:01.569824');
INSERT INTO "django_migrations" VALUES(18,'sessions','0001_initial','2021-07-27 20:10:01.834192');
INSERT INTO "django_migrations" VALUES(19,'patientdata','0001_initial','2021-07-27 20:10:36.699789');
INSERT INTO "django_migrations" VALUES(20,'visits','0001_initial','2021-07-27 20:11:06.530931');
INSERT INTO "django_migrations" VALUES(21,'visitdrug','0001_initial','2021-07-27 20:11:46.562476');
INSERT INTO "django_migrations" VALUES(22,'presenthistory','0001_initial','2021-07-27 21:08:45.035329');
INSERT INTO "django_migrations" VALUES(23,'pasthistory','0001_initial','2021-07-27 21:09:40.670547');
INSERT INTO "django_migrations" VALUES(24,'labs','0001_initial','2021-07-28 04:14:37.944157');
INSERT INTO "django_migrations" VALUES(25,'labs','0002_alter_labvisit_image','2021-07-28 04:45:05.046223');
INSERT INTO "django_migrations" VALUES(26,'labs','0003_auto_20210728_0644','2021-07-28 04:45:05.217893');
INSERT INTO "django_migrations" VALUES(27,'patientdata','0002_operations','2021-07-29 08:22:23.330712');
INSERT INTO "django_migrations" VALUES(28,'patientdata','0003_auto_20210729_1347','2021-07-29 11:47:22.566884');
INSERT INTO "django_migrations" VALUES(29,'revisits','0001_initial','2021-07-30 09:47:12.556473');
INSERT INTO "django_migrations" VALUES(30,'revisitdrug','0001_initial','2021-07-30 09:47:37.012134');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE TABLE "labs_labfollowup" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "result" varchar(150) NULL, "resdate" date NOT NULL, "image" varchar(100) NULL, "updated" datetime NOT NULL, "followup_id" bigint NOT NULL REFERENCES "visits_visits" ("id") DEFERRABLE INITIALLY DEFERRED, "patient_id" bigint NOT NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "labs_labvisit" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "result" varchar(150) NULL, "resdate" date NOT NULL, "updated" datetime NOT NULL, "patient_id" bigint NOT NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED, "visit_id" bigint NOT NULL REFERENCES "visits_visits" ("id") DEFERRABLE INITIALLY DEFERRED, "file" varchar(100) NULL, "image" varchar(100) NULL);
INSERT INTO "labs_labvisit" VALUES(3,'HB','','2021-07-28','2021-07-28 20:07:26.434748',1,1,'','patient_1_y-a-h-i-a- -s-a-y-e-d/WhatsApp_Image_2021-07-13_at_5.12.32_PM.jpeg');
INSERT INTO "labs_labvisit" VALUES(4,'PSA','','2021-07-28','2021-07-28 11:00:27.676241',1,1,'','patient_1_[''y-a-h-i-a'']/Unregistered.png');
INSERT INTO "labs_labvisit" VALUES(5,'CBC','','2021-07-28','2021-07-28 20:07:41.316850',1,1,'','patient_1_yahia-sayed/214943467_349684603192785_745352544058005412_n.jpg');
INSERT INTO "labs_labvisit" VALUES(6,'Urine Analysis','','2021-07-28','2021-07-28 10:56:00.133436',1,1,'','patient_1_yahia/Desert.jpg');
INSERT INTO "labs_labvisit" VALUES(7,'Urine Analysis','','2021-07-28','2021-07-29 11:23:19.521413',2,2,'patient_2_Manal-mongy-ahmed/Dear_doctor_agKzOJT.pdf','patient_2_Manal-mongy-ahmed/199722177_170501375044402_7313632204099769954_n.jpg');
INSERT INTO "labs_labvisit" VALUES(8,'CBC','','2021-07-28','2021-07-28 20:10:09.745720',2,2,'','patient_2_Manal-mongy-ahmed/WhatsApp_Image_2021-07-13_at_5.12.32_PM.jpeg');
INSERT INTO "labs_labvisit" VALUES(9,'Any Analysis','','2021-07-29','2021-07-29 11:12:12.836107',2,2,'patient_2_Manal-mongy-ahmed/laundry1.png','patient_2_Manal-mongy-ahmed/laundry2.png');
INSERT INTO "labs_labvisit" VALUES(10,'Stool','','2021-07-29','2021-07-29 11:31:37.981479',2,2,'patient_2_Manal-mongy-ahmed/python-3.6.5.exe','patient_2_Manal-mongy-ahmed/sales6.jpg');
INSERT INTO "labs_labvisit" VALUES(11,'CBC','','2021-07-31','2021-07-31 16:03:41.449490',4,4,'','patient_4_����-����/199722177_170501375044402_7313632204099769954_n.jpg');
INSERT INTO "labs_labvisit" VALUES(12,'Urine Analysis','','2021-08-01','2021-08-01 10:34:45.308960',5,5,'','');
INSERT INTO "labs_labvisit" VALUES(13,'CBC','','2021-08-01','2021-08-01 10:36:26.186214',5,5,'','');
INSERT INTO "labs_labvisit" VALUES(14,'Stone Analysis','','2021-08-01','2021-08-01 10:38:27.163471',5,5,'','');
INSERT INTO "labs_labvisit" VALUES(15,'PCR','','2021-08-02','2021-08-02 12:34:40.665980',6,6,'','');
INSERT INTO "labs_labvisit" VALUES(16,'any','','2021-08-03','2021-08-03 21:49:12.404861',3,3,'','');
CREATE TABLE "pasthistory_pasthistory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "pasthist" varchar(150) NULL, "histdate" date NULL, "remarknote" varchar(1000) NULL, "patient_id" bigint NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "pasthistory_pasthistory" VALUES(1,'Hernia','2001-07-27','',1);
INSERT INTO "pasthistory_pasthistory" VALUES(2,'Appendectomy','2006-03-27','',1);
INSERT INTO "pasthistory_pasthistory" VALUES(3,'Abccess','2021-07-27','',1);
INSERT INTO "pasthistory_pasthistory" VALUES(4,'any history','2021-07-31','',4);
INSERT INTO "pasthistory_pasthistory" VALUES(5,'any operation','2021-08-04','',3);
INSERT INTO "pasthistory_pasthistory" VALUES(6,'any history','2021-08-04','',3);
CREATE TABLE "patientdata_operations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NULL, "opdate" date NULL, "amount" decimal NOT NULL, "followup" varchar(150) NULL, "improve" varchar(150) NULL, "heal" bool NOT NULL, "remark" varchar(300) NULL, "patient_id" bigint NOT NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "patientdata_operations" VALUES(1,'Kidney','2021-07-31',2500,'','',0,'',1);
INSERT INTO "patientdata_operations" VALUES(2,'Appendectomy','2021-07-29',0,'','',1,'',1);
INSERT INTO "patientdata_operations" VALUES(3,'Any op','2021-07-29',0,'','',0,'',1);
INSERT INTO "patientdata_operations" VALUES(4,'Appendectomy','2021-07-29',0,'','',0,'',2);
INSERT INTO "patientdata_operations" VALUES(5,'Appendectomy','2021-07-29',0,'','',0,'',2);
INSERT INTO "patientdata_operations" VALUES(6,'Appendectomy','2021-07-29',0,'','',1,'',2);
INSERT INTO "patientdata_operations" VALUES(7,'Any','2021-08-02',3000,'any','any',1,'any',2);
INSERT INTO "patientdata_operations" VALUES(8,'Any','2021-07-29',0,'','',0,'',1);
INSERT INTO "patientdata_operations" VALUES(9,'Any Operation','2021-08-11',0,'','',0,'',1);
INSERT INTO "patientdata_operations" VALUES(10,'Any Operation','2021-08-10',4500,'any','improved',1,'any descreiption',5);
CREATE TABLE "patientdata_patients" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL, "address" varchar(100) NULL, "birth_date" date NULL, "phone" varchar(150) NULL, "mobile" varchar(150) NULL, "cardid" varchar(20) NULL, "barcode" varchar(100) NULL UNIQUE, "barurl" varchar(200) NULL, "barimg" varchar(100) NULL, "job" varchar(80) NULL, "age" varchar(80) NULL);
INSERT INTO "patientdata_patients" VALUES(1,'yahia sayed','Alexandria','1994-05-11','032989823','0125656565876','1',NULL,NULL,'',NULL,'27 years, 2 months, and 17 days old.');
INSERT INTO "patientdata_patients" VALUES(2,'Manal mongy ahmed','','1997-12-28','','','2',NULL,NULL,'','','23 years, 7 months, and 1 day old.');
INSERT INTO "patientdata_patients" VALUES(3,'Ahmed','�������','1992-05-24','02','015','3',NULL,NULL,'','','29 years, 2 months, and 5 days old.');
INSERT INTO "patientdata_patients" VALUES(4,'���� ����','��������','1969-12-31','0365665','01117676323','',NULL,NULL,'','���� ���������','51 years, 6 months, and 29 days old.');
INSERT INTO "patientdata_patients" VALUES(5,'wafaa Abdo','behira','1961-04-09','0455225252','015','',NULL,NULL,'','��� ����','60 years, 3 months, and 23 days old.');
INSERT INTO "patientdata_patients" VALUES(6,'samira magdy Ahmed','','2021-08-01','','','',NULL,NULL,'','','Oops! Could not calculate age!');
CREATE TABLE "presenthistory_presenthistory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "visitdate" date NULL, "temprature" decimal NOT NULL, "weight" decimal NOT NULL, "height" decimal NOT NULL, "cholestrol" varchar(150) NULL, "pulse" varchar(150) NULL, "bloodpr" varchar(150) NULL, "bsl" varchar(150) NULL, "hb" varchar(150) NULL, "patient_id" bigint NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED, "visit_id" bigint NULL REFERENCES "visits_visits" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "presenthistory_presenthistory" VALUES(1,'2021-07-29',0,0,0,'','6=80','','','',4,4);
INSERT INTO "presenthistory_presenthistory" VALUES(4,'2021-07-31',0,0,0,'','','','','',5,5);
INSERT INTO "presenthistory_presenthistory" VALUES(5,'2021-07-27',0,0,0,'','','','','',1,1);
INSERT INTO "presenthistory_presenthistory" VALUES(8,'2021-08-01',0,0,0,'','','','','',6,6);
CREATE TABLE "revisitdrug_remedicine" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NULL, "plan" varchar(150) NULL, "patient_id" bigint NOT NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED, "revisit_id" bigint NULL REFERENCES "revisits_revisits" ("id") DEFERRABLE INITIALLY DEFERRED, "visit_id" bigint NULL REFERENCES "visits_visits" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "revisits_revisits" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "visitdate" date NULL, "complain" text NULL, "sign" text NULL, "diagnosis" varchar(150) NULL, "intervention" varchar(150) NULL, "amount" integer NOT NULL, "patient_id" bigint NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED, "visit_id" bigint NULL REFERENCES "visits_visits" ("id") DEFERRABLE INITIALLY DEFERRED);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('django_migrations',30);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',0);
INSERT INTO "sqlite_sequence" VALUES('django_content_type',16);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',64);
INSERT INTO "sqlite_sequence" VALUES('auth_group',0);
INSERT INTO "sqlite_sequence" VALUES('auth_user',0);
INSERT INTO "sqlite_sequence" VALUES('visits_visits',6);
INSERT INTO "sqlite_sequence" VALUES('pasthistory_pasthistory',6);
INSERT INTO "sqlite_sequence" VALUES('labs_labvisit',16);
INSERT INTO "sqlite_sequence" VALUES('patientdata_operations',10);
INSERT INTO "sqlite_sequence" VALUES('patientdata_patients',6);
INSERT INTO "sqlite_sequence" VALUES('visitdrug_medicine',13);
INSERT INTO "sqlite_sequence" VALUES('presenthistory_presenthistory',8);
CREATE TABLE "visitdrug_medicine" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NULL, "plan" varchar(150) NULL, "patient_id" bigint NOT NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED, "visit_id" bigint NULL REFERENCES "visits_visits" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "visitdrug_medicine" VALUES(1,'Alfa Kemo Tripsen','����� ��� ������',3,3);
INSERT INTO "visitdrug_medicine" VALUES(2,'Alfa Kemo Tripsen','����� ��� ������',2,2);
INSERT INTO "visitdrug_medicine" VALUES(3,'Cataflam','��� ��� ������',2,2);
INSERT INTO "visitdrug_medicine" VALUES(4,'Scaro Creem','���� ����� � ����',2,2);
INSERT INTO "visitdrug_medicine" VALUES(5,'Urosolvine','���� 3 ����',2,2);
INSERT INTO "visitdrug_medicine" VALUES(6,'Scaro Creem','���� ��� ����� �����',5,5);
INSERT INTO "visitdrug_medicine" VALUES(7,'Urosolvine','���� �����',5,5);
INSERT INTO "visitdrug_medicine" VALUES(8,'Cataflam tab','��� ��� ������',5,5);
INSERT INTO "visitdrug_medicine" VALUES(9,'Remactazide Tab','��� ��� ��� ���',5,5);
INSERT INTO "visitdrug_medicine" VALUES(10,'Asprine tab','��� ��� �����',5,5);
INSERT INTO "visitdrug_medicine" VALUES(11,'Dosin','��� ��� ����',5,5);
INSERT INTO "visitdrug_medicine" VALUES(12,'alfa kimotripsen Amp','������ ��� � ���',5,5);
INSERT INTO "visitdrug_medicine" VALUES(13,'Fusi Cream','���� ��� ����� �����',5,5);
CREATE TABLE "visits_visits" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "visitdate" date NULL, "complain" text NULL, "sign" text NULL, "diagnosis" varchar(150) NULL, "intervention" varchar(150) NULL, "amount" integer NOT NULL, "patient_id" bigint NULL REFERENCES "patientdata_patients" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "visits_visits" VALUES(1,'2021-07-27','any comp','any sign','any diagnosis','any intervention',150,1);
INSERT INTO "visits_visits" VALUES(2,'2021-07-28','any comp','any sign','','any intervention',200,2);
INSERT INTO "visits_visits" VALUES(3,'2021-07-29','any comp','any sign','any diagnosis','any intervention',150,3);
INSERT INTO "visits_visits" VALUES(4,'2021-07-29','any comp','any sign',NULL,'any intervention',0,4);
INSERT INTO "visits_visits" VALUES(5,'2021-07-31','any comp','any sign',NULL,'any intervention',0,5);
INSERT INTO "visits_visits" VALUES(6,'2021-08-01','any comp','any sign',NULL,'any intervention',0,6);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "visits_visits_patient_id_4d8ec1b0" ON "visits_visits" ("patient_id");
CREATE INDEX "visitdrug_medicine_patient_id_b777d6a8" ON "visitdrug_medicine" ("patient_id");
CREATE INDEX "visitdrug_medicine_visit_id_74b006f5" ON "visitdrug_medicine" ("visit_id");
CREATE INDEX "presenthistory_presenthistory_patient_id_18a6586f" ON "presenthistory_presenthistory" ("patient_id");
CREATE INDEX "presenthistory_presenthistory_visit_id_cf288778" ON "presenthistory_presenthistory" ("visit_id");
CREATE INDEX "pasthistory_pasthistory_patient_id_a4eadbe8" ON "pasthistory_pasthistory" ("patient_id");
CREATE INDEX "labs_labfollowup_followup_id_99b0a8d1" ON "labs_labfollowup" ("followup_id");
CREATE INDEX "labs_labfollowup_patient_id_c666ed70" ON "labs_labfollowup" ("patient_id");
CREATE INDEX "labs_labvisit_patient_id_55bd14fa" ON "labs_labvisit" ("patient_id");
CREATE INDEX "labs_labvisit_visit_id_5b969b27" ON "labs_labvisit" ("visit_id");
CREATE INDEX "patientdata_operations_patient_id_2a37f9dd" ON "patientdata_operations" ("patient_id");
CREATE INDEX "revisits_revisits_patient_id_6fd5f137" ON "revisits_revisits" ("patient_id");
CREATE INDEX "revisits_revisits_visit_id_8102a628" ON "revisits_revisits" ("visit_id");
CREATE INDEX "revisitdrug_remedicine_patient_id_bf797334" ON "revisitdrug_remedicine" ("patient_id");
CREATE INDEX "revisitdrug_remedicine_revisit_id_eb26873d" ON "revisitdrug_remedicine" ("revisit_id");
CREATE INDEX "revisitdrug_remedicine_visit_id_052b0028" ON "revisitdrug_remedicine" ("visit_id");
COMMIT;
