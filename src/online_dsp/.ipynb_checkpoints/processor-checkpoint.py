import numpy as np


def frame_processing(frm_sig0, param):
    """フレーム毎の信号処理（元のframe_processing.mのループ構造を再現）"""
    len_val, ch_val = frm_sig0.shape

    # 複素数データ用のハコ（周波数スペクトル）と、実数データ用のハコを準備
    frm_spc = np.zeros((len_val, ch_val), dtype=np.complex128)
    frm_sig1 = np.zeros((len_val, ch_val))

    # 各チャンネルごとにFFT
    for h in range(ch_val):
        frm_spc[:, h] = np.fft.fft(frm_sig0[:, h], len_val)

    # ----------------------------------------------------
    # ※ 将来オンラインAuxIVAの数式（VやWの更新）をここに実装していく
    # ----------------------------------------------------

    # 各チャンネルごとにiFFT
    for h in range(ch_val):
        frm_sig1[:, h] = np.fft.ifft(frm_spc[:, h], len_val).real

    return frm_sig1, param
