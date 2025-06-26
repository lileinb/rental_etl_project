# 东南亚房产租赁数据清洗与建模系统 -- 主要是关于马来西亚吉隆坡市场的房租分析和调研

## 项目简介
本项目旨在构建一个自动化 ETL 数据清洗流程，处理东南亚（如马来西亚）租房平台数据，构建结构化存储并支持可视化展示。

## 技术栈
- Python + Pandas
- MySQL
- Git + GitLab/GitHub
- Airflow
- Streamlit（可视化模块）

##  项目结构
```bash
rental_etl_project/
├── data/               # 原始与清洗后的数据
├── scripts/            # 清洗与加载脚本
├── sql/                # 建表 SQL
├── airflow_dags/       # DAG 脚本（后期）
├── streamlit_app/      # 展示前端（后期）
├── docs/               # 架构图、总结、复盘文档
├── README.md
├── requirements.txt


# june 24 2025
- 今天主要完成的任务是房价和房屋数目的直方图和曲线可视化，争对房价字段的数据清理筛除极端值，同时熟练掌握git，和使用github进行部署