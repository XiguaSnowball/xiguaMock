SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `mock_config`
-- ----------------------------
DROP TABLE IF EXISTS `mock_config`;
CREATE TABLE `mock_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `reqparams` varchar(500) DEFAULT NULL,
  `methods` varchar(50) DEFAULT NULL,
  `domain` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `resparams` varchar(500) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` int(1) DEFAULT NULL,
  `ischeck` int(1) DEFAULT NULL,
  `project_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mock_config
-- ----------------------------
INSERT INTO `mock_config` (`id`, `title`, `reqparams`, `methods`, `domain`, `description`, `resparams`, `update_time`, `status`, `ischeck`, `project_name`)
VALUES
	(512, '登录1', 'var1=1&var2=2&var3=3', 'GET', '/login/manageLogin2', '一个请求342343423423423423423', '{\"code\":0,\"msg\":\"成功\",\"data\":{\"count\":1,\"responseList\":[{\"id\":304,\"mryxId\":70889601,\"platform\":1,\"nickName\":\"候春磊\",\"mobile\":\"18310553894\",\"rankId\":2,\"rankName\":\"初级小B\",\"inviteUserId\":236,\"orderCount\":13,\"orderPrice\":24.91,\"commissionPrice\":262.12,\"relation\":null,\"memberCount\":2,\"labelNameStr\":\"非官方\",\"userStatus\":1,\"userStatusName\":\"已通过\",\"createTime\":\"2019-01-04 18:07:36\",\"createTimeStr\":\"2019-01-04 18:07:36\"}]}}', '2019-01-16 19:59:44', 0, 1, '登录');
INSERT INTO `mock_config` (`id`, `title`, `reqparams`, `methods`, `domain`, `description`, `resparams`, `update_time`, `status`, `ischeck`, `project_name`)
VALUES
	(392, '西瓜2', '{\n\"a\":1\n}', 'post', '/api/999', 'sdfsd', '{\n\"a\":1,\n\"b\":2\n}', '2019-01-16 17:15:43', 0, 1, 'eee');
