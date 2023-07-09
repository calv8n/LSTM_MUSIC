from transformers.models import transfo_xl
from transformers import TransfoXLConfig
from tensorflow.keras import activations
# from .vocab import MusicVocab

def default_config():
    config = TransfoXLConfig.copy()
    config['act'] = activations.gelu

    config['mem_len'] = 512
    config['d_model'] = 512
    config['d_inner'] = 2048
    config['n_layers'] = 16
    
    config['n_heads'] = 8
    config['d_head'] = 64

    return config

def music_config():
    config = default_config()
    config['encode_position'] = True
    return config

def musicm_config():
    config = music_config()
    config['d_model'] = 768
    config['d_inner'] = 3072
    config['n_heads'] = 12
    config['d_head'] = 64
    config['n_layers'] = 12
    return config
    
def multitask_config():
    config = default_config()
    config['bias'] = True
    config['enc_layers'] = 8
    config['dec_layers'] = 8
    del config['n_layers']
    return config

def multitaskm_config():
    config = musicm_config()
    config['bias'] = True
    config['enc_layers'] = 12
    config['dec_layers'] = 12
    del config['n_layers']
    return config
