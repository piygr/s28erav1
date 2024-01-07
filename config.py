from pathlib import Path


def get_config():
    return dict(
        micro_batch_size=4,
        batch_size=8,   #should be multiple of micro_batch
        epoch_steps=10,
        seq_len=512,
        preload=False,
        feed_url='https://696a-35-203-132-31.ngrok-free.app/generate'
    )