ALTER TABLE `analysis_sheet`
MODIFY `id` INT NOT NULL AUTO_INCREMENT;


# 修改数据模板相关主键为BIGINT
ALTER TABLE `data_template`
MODIFY COLUMN `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT;
-- 1. 修改 data_table 中的 data_template_id 字段
ALTER TABLE `data_table`
MODIFY COLUMN `data_template_id` BIGINT UNSIGNED NOT NULL COMMENT '引用数据模板外键';

-- 2. 修改 data_template_details 中的 data_template_id 字段
ALTER TABLE `data_template_details`
MODIFY COLUMN `data_template_id` BIGINT UNSIGNED NOT NULL COMMENT '模板外键';

-- 3. 修改 data_template_tags_relative 中的 template_id 字段
ALTER TABLE `data_template_tags_relative`
MODIFY COLUMN `template_id` BIGINT UNSIGNED NOT NULL;
