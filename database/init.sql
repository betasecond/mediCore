CREATE DATABASE IF NOT EXISTS medical_data;


CREATE USER IF NOT EXISTS 'mediCore'@'%' IDENTIFIED BY 'bWVkaUNvcmU=';
GRANT ALL PRIVILEGES ON medical_data.* TO 'mediCore'@'%';
FLUSH PRIVILEGES;

USE medical_data;
--  DDL

CREATE TABLE `analysis_sheet`  (
  `id` int NOT NULL,
  `analysis_table_id` int NOT NULL COMMENT '分析表引用外键',
  `sheet_code` varchar(255) NOT NULL COMMENT '随机生成',
  `sheet_name` varchar(255) NOT NULL,
  `remark` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `analysis_sheet_detail`  (
  `id` int NOT NULL,
  `analysis_sheet_id` int NOT NULL,
  `case_id` int NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `item_value` varchar(255) NOT NULL,
  `item_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `analysis_table`  (
  `id` int NOT NULL,
  `table_name` varchar(255) NOT NULL,
  `extract_cases` varchar(255) NOT NULL,
  `since_start` date NOT NULL,
  `since_end` date NOT NULL,
  `data_template_id` int NOT NULL,
  `constraint` varchar(255) NULL COMMENT '约束条件',
  `load_times` datetime NULL COMMENT '数据加载次数',
  `last_load_date` datetime NULL COMMENT '最后加载时间',
  PRIMARY KEY (`id`)
);

CREATE TABLE `archive`  (
  `id` int NOT NULL,
  `arcive_id` varchar(255) NOT NULL,
  `archive_name` varchar(255) NOT NULL COMMENT '专病档案名称',
  `description` text NULL COMMENT '专病档案说明',
  PRIMARY KEY (`id`, `arcive_id`)
);

CREATE TABLE `archive_case_relative`  (
  `id` int NOT NULL,
  `archive_id` varchar(255) NOT NULL,
  `case_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `base_info`  (
  `id` int NOT NULL,
  `case_id` varchar(255) NOT NULL COMMENT '病历外键引用',
  `name` varchar(255) NOT NULL,
  `name_code` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `category_code` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `type_code` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL COMMENT '值',
  PRIMARY KEY (`id`)
);

CREATE TABLE `cases`  (
  `id` int NOT NULL,
  `case_id` varchar(255) NOT NULL,
  `identity_id` varchar(255) NOT NULL,
  `inhospital_id` varchar(255) NULL COMMENT '住院号',
  PRIMARY KEY (`id`, `case_id`)
);

CREATE TABLE `charts`  (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `analysis_sheet_id` int NOT NULL COMMENT '数据源',
  `selected_cases` varchar(255) NOT NULL,
  `selected_attrs` varchar(255) NOT NULL,
  `mapping` varchar(255) NOT NULL COMMENT '数据映射，存JSON',
  `axis` varchar(255) NOT NULL COMMENT '坐标轴，存JSON',
  `options` varchar(255) NOT NULL COMMENT '常规配置，存JSON',
  PRIMARY KEY (`id`)
);

CREATE TABLE `clinical_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `name_code` varchar(255) NOT NULL,
  `case_id` varchar(255) NOT NULL COMMENT '病历号外键',
  PRIMARY KEY (`id`)
);

CREATE TABLE `data_table`  (
  `id` int NOT NULL,
  `case_id` int NOT NULL COMMENT '病历外键引用',
  `table_name` varchar(255) NOT NULL,
  `data_template_id` int NOT NULL COMMENT '引用数据模板外键',
  PRIMARY KEY (`id`)
);

CREATE TABLE `data_template`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NULL,
  `category_id` int NOT NULL COMMENT '类型外键引用',
  `used_n` int NOT NULL COMMENT '被使用次数',
  PRIMARY KEY (`id`)
);

CREATE TABLE `data_template_category`  (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `data_template_details`  (
  `id` int NOT NULL,
  `data_template_id` int NOT NULL COMMENT '模板外键',
  `item_name` varchar(255) NOT NULL,
  `item_name_code` varchar(255) NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `category_name_code` varchar(255) NOT NULL,
  `type_name` varchar(255) NOT NULL,
  `type_name_code` varchar(255) NOT NULL,
  `order_index` int NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `data_template_tags`  (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `data_template_tags_relative`  (
  `id` int NOT NULL,
  `template_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `dictionary`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `word_code` varchar(255) NOT NULL COMMENT '词条编号',
  `word_name` varchar(255) NOT NULL COMMENT '中文名称',
  `word_eng` varchar(255) NULL COMMENT '英文名称',
  `word_short` varchar(255) NULL COMMENT '英文缩写',
  `word_class` varchar(255) NOT NULL COMMENT '词条类型',
  `word_apply` varchar(255) NOT NULL COMMENT '词条应用',
  `word_belong` varchar(255) NULL COMMENT '从属别名',
  PRIMARY KEY (`id`, `word_code`),
  INDEX `name_index`(`word_name`)
 );

CREATE TABLE `document_chart`  (
  `id` int NOT NULL,
  `document_id` int NOT NULL,
  `chart_id` int NOT NULL,
  `x` float NOT NULL,
  `y` float NOT NULL,
  `height` double NOT NULL,
  `width` double NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `documents`  (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NULL,
  `description` varchar(255) NULL,
  `properties` varchar(255) NOT NULL COMMENT '属性，存JSON',
  PRIMARY KEY (`id`)
);

CREATE TABLE `examination_images`  (
  `id` int NOT NULL,
  `examination_sheet_id` int NOT NULL COMMENT '检查表外键引用',
  `url` varchar(255) NOT NULL,
  `remark` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `examination_sheet`  (
  `id` int NOT NULL,
  `data_table_id` int NOT NULL COMMENT '数据表外键引用',
  `case_id` int NULL COMMENT '病历冗余存储',
  `name` varchar(255) NOT NULL,
  `name_code` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `category_code` varchar(255) NOT NULL,
  `diagnosis` varchar(255) NOT NULL COMMENT '诊断',
  `description` varchar(255) NULL COMMENT '检查描述',
  `exam_date` datetime NOT NULL,
  `inspector` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `identity`  (
  `id` int NOT NULL,
  `identity_id` varchar(255) NOT NULL COMMENT '身份证号',
  `true_name` varchar(255) NOT NULL COMMENT '真实姓名',
  `gender` int NOT NULL COMMENT '性别',
  `birth_date` datetime NOT NULL COMMENT '出生年月日',
  PRIMARY KEY (`id`, `identity_id`),
  UNIQUE INDEX `identity_index`(`identity_id`)
);

CREATE TABLE `image`  (
  `id` int NOT NULL,
  `document_id` int NOT NULL COMMENT '文档引用',
  `url` varchar(255) NOT NULL,
  `remark` varchar(255) NULL,
  `x` float NOT NULL,
  `y` float NOT NULL,
  `height` double NOT NULL,
  `width` double NOT NULL,
  `is_stroke` int NOT NULL,
  `stroke_weight` double NOT NULL COMMENT '描边粗细',
  `stroke_color` varchar(255) NOT NULL COMMENT '描边颜色',
  PRIMARY KEY (`id`)
);

CREATE TABLE `shape`  (
  `id` int NOT NULL,
  `document_id` int NOT NULL COMMENT '文档引用',
  `x` float NOT NULL,
  `y` float NOT NULL,
  `height` double NOT NULL,
  `width` double NOT NULL,
  `is_fill` int NOT NULL,
  `fill_color` varchar(255) NOT NULL COMMENT '填充颜色',
  `is_stroke` int NOT NULL,
  `stroke_color` varchar(255) NOT NULL COMMENT '描边颜色',
  `path` varchar(255) NOT NULL COMMENT '点集，存JSON',
  PRIMARY KEY (`id`)
);

CREATE TABLE `testing_sheet`  (
  `id` int NOT NULL,
  `data_table_id` int NOT NULL COMMENT '数据表外键引用',
  `case_id` int NULL COMMENT '病历冗余存储',
  `name` varchar(255) NOT NULL,
  `name_code` varchar(255) NOT NULL,
  `name_eng` varchar(255) NOT NULL,
  `name_short` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `category_code` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `type_code` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `test_date` datetime NOT NULL,
  `inspector` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `text`  (
  `id` int NOT NULL,
  `document_id` int NOT NULL COMMENT '文档引用',
  `x` float NOT NULL,
  `y` float NOT NULL,
  `height` double NOT NULL,
  `width` double NOT NULL,
  `family` varchar(255) NOT NULL,
  `size` int NOT NULL,
  `color` varchar(255) NOT NULL,
  `weight` int NOT NULL,
  `underline` int NOT NULL,
  `slope` int NOT NULL,
  PRIMARY KEY (`id`)
);

-- sd

-- 日志记录
CREATE TABLE IF NOT EXISTS `initialization_log` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `event` VARCHAR(255) NOT NULL,
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO `initialization_log` (`event`) VALUES ('Database initialized successfully.');