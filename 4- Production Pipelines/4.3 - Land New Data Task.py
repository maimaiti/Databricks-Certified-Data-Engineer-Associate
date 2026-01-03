# Databricks notebook source
# MAGIC %run ../Includes/Copy-Datasets

# COMMAND ----------

load_new_json_data()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from json.`/Volumes/dev/default/bookstore/books-cdc/02.json`
