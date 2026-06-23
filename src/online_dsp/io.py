import matplotlib.pyplot as plt
import numpy as np


def audio_in(len_samples, channels):
    """マイク入力のシミュレーション（元のones(len,ch)に準拠）"""
    return np.ones((len_samples, channels))


def audio_out(sig):
    """スピーカー出力のシミュレーション（元のplotとdrawnowに準拠）"""
    plt.clf()
    plt.plot(sig)
    plt.pause(0.01)
