"""Logging module to track all runs and output"""
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("This is warning")
logging.error("This is error")
logging.info("Program end")
