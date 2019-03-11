SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
FROM information_schema.tables
WHERE table_schema = 'heroku_e0771598287fecc';


-- SET FOREIGN_KEY_CHECKS = 0;
-- DROP TABLE IF EXISTS `auth_group_permissions`;
-- DROP TABLE IF EXISTS `auth_permission`;
-- DROP TABLE IF EXISTS `auth_group`;
-- DROP TABLE IF EXISTS `django_admin_log`;
-- DROP TABLE IF EXISTS `django_content_type`;
-- DROP TABLE IF EXISTS `django_migrations`;
-- DROP TABLE IF EXISTS `django_session`;
-- DROP TABLE IF EXISTS `doctors_doctorlogin`;
-- DROP TABLE IF EXISTS `doctors_doctors`;
-- DROP TABLE IF EXISTS `doctors_logincredentials`;
-- DROP TABLE IF EXISTS `patients_emergencycontacts`;
-- DROP TABLE IF EXISTS `patients_healthstats`;
-- DROP TABLE IF EXISTS `patients_patientlogin`;
-- DROP TABLE IF EXISTS `patients_patientrecord`;
-- DROP TABLE IF EXISTS `patients_patients`;
-- DROP TABLE IF EXISTS `users_customuser`;
-- DROP TABLE IF EXISTS `users_customuser_groups`;
-- DROP TABLE IF EXISTS `users_customuser_user_permissions`;

-- SET FOREIGN_KEY_CHECKS = 1;
