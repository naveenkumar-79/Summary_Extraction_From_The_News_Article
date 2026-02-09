import logging
def setup_logging(script_name):
    logger=logging.getLogger(script_name)
    logger.setLevel(logging.DEBUG)

    handler=logging.FileHandler(f'D:\\NLP_projects\\summary_extraction\\log_files\\{script_name}.log','w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger