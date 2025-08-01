import logging

def setup_logger():
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    return logging.getLogger("MarksheetLogger")