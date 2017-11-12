drop table if exists `spasociety_store`.`user`;
CREATE TABLE `spasociety_store`.`user` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(47) NOT NULL,
  `lastname` VARCHAR(47) NOT NULL,
  `username` VARCHAR(47) NOT NULL,
  `email` TEXT NOT NULL,
  `password` VARCHAR(47) NOT NULL,
  PRIMARY KEY (`userid`)
);
