import streamlit as st
import pandas as pd

# 如果在jupyter出现这个问题，就注释掉这一句，用回原始版本
from streamlit_extras.metric_cards import style_metric_cards

# 参数监控台
def metric_visual(container, model_name, epoch: int, all_epoch: int, metric_name: str, metric_num: float, loss_name: str, loss_num: float, params: dict):
    intro, epoch_m, metric_m, loss_m = container.columns(4)


    intro.metric('Current Model', ''+model_name, '3.75%')
    epoch_m.metric('Epoch', str(epoch) + ' / ' + str(all_epoch), str(all_epoch-epoch) + ' epochs left')
    metric_m.metric(metric_name, str(metric_num) + ' %', '3.75%')
    loss_m.metric(loss_name, str(loss_num), '-0.7533')
    # 如果在jupyter出现这个问题，就注释掉这一句，用回原始版本
    style_metric_cards()

def bar_visual(epoch, bar, bar_text):
    bar.progress(epoch + 1, text=bar_text)
