import os
import pandas as pd
from typing import Dict

BASE_PATH = "/kaggle/input/ariel-data-challenge-2024"

def get_label_data() -> pd.DataFrame:
    """学習用ラベルを取得
    Returns:
        pd.DataFrame: 学習用ラベルDF
    """
    return pd.read_csv(os.path.join(BASE_PATH, "train_labels.csv"))

def get_meta_data() -> Dict[str, pd.DataFrame]:
    """メタデータを取得
    Returns:
        Dict[str, pd.DataFrame]: キーをstrとして機器に依存するパラメータ等を保持しているデータフレームを返す
    """
    return {
        "train_ads_info": pd.read_csv(os.path.join(BASE_PATH, "train_adc_info.csv")),
        "test_ads_info": pd.read_csv(os.path.join(BASE_PATH, "test_adc_info.csv")),
        "axis_info": pd.read_parquet(os.path.join(BASE_PATH, "axis_info.parquet")),
        "wavelengths": pd.read_csv(os.path.join(BASE_PATH, "wavelengths.csv")),
    }

def get_signal_data(planet_id: str,
                    instrument_id: int,
                    mode: str ="train"
    ) -> Dict[str, pd.DataFrame]:
    """planet_idに紐づくデータを返す．具体的にはシグナルデータとキャリブレーションデータ
    Args:
        planet_id (str): planet_idを指定
        instrument_idx (int): 0: AIRS-CH0, 1: FGS1
        mode (str, optional): train, testでデータを指定. Defaults to "train".
    Returns:
        Dict[str, pd.DataFrame]: 各種データを保持したDFをバリューとする辞書
    """
    if instrument_id == 0:
        return pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/AIRS-CH0_signal.parquet")),
    else:
        return pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/FGS1_signal.parquet")),

def get_calibration_data(planet_id: str,
                         mode: str ="train"
    ) -> Dict[str, pd.DataFrame]:
    """キャリブレーションデータの取得
    Returns:
        Dict[str, pd.DataFrame]: 各種データを保持したDFをバリューとする辞書
    """
    return {
        "AIRS-CH0_calibration_dark": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/AIRS-CH0_calibration/dark.parquet")),
        "AIRS-CH0_calibration_dark": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/FGS1_calibration/dark.parquet")),
        "AIRS-CH0_calibration_dead": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/AIRS-CH0_calibration/dead.parquet")),
        "AIRS-CH0_calibration_dead": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/FGS1_calibration/dead.parquet")),
        "AIRS-CH0_calibration_flat": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/AIRS-CH0_calibration/flat.parquet")),
        "AIRS-CH0_calibration_flat": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/FGS1_calibration/flat.parquet")),
        "AIRS-CH0_calibration_linear_corr": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/AIRS-CH0_calibration/linear_corr.parquet")),
        "AIRS-CH0_calibration_linear_corr": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/FGS1_calibration/linear_corr.parquet")),
        "AIRS-CH0_calibration_read": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/AIRS-CH0_calibration/read.parquet")),
        "AIRS-CH0_calibration_read": pd.read_parquet(os.path.join(BASE_PATH, f"{mode}/{planet_id}/FGS1_calibration/read.parquet")),
    }