from typing import List
from src.utils.common import get_signal_data
import pandas as pd

def get_smoothed_signal(planet_id: str,
                   instrument_idx: int,
                   mode="train"):
    """シグナル画像データを平均してスムージング下配列を返す

    Args:
        planet_id (str): planet_idを指定
        instrument_idx (int): 0: AIRS-CH0, 1: FGS1
        mode (str, optional): train, testでデータを指定. Defaults to "train".

    Returns:
        np.ndarray: スムージング後の配列
    """
    df_signal = get_signal_data(planet_id, instrument_idx, mode=mode)
    signal = df_signal.values.mean(axis=1)
    net_signal = signal[1::2] - signal[0::2]
    return net_signal

def get_smoothed_signals_df(planet_ids: List[str],
                       instrument_idx: int,
                       mode="train"):
    """シグナル画像データを平均してスムージングしたDFを返す

    Args:
        planet_id (str): planet_idを指定
        instrument_idx (int): 0: AIRS-CH0, 1: FGS1
        mode (str, optional): train, testでデータを指定. Defaults to "train".
    Returns:
        pd.DataFrame: スムージング後のデータを持つDF
    """
    data = {}
    for planet_id in planet_ids:
        data[planet_id] = get_smoothed_signal(planet_id,
                                instrument_idx=instrument_idx,
                                mode=mode)
    df = pd.DataFrame(data).T
    df.index.name = "planet_id"
    return df