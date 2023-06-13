import json
import streamlit as st
from pathlib import Path

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo
from utils import *

# 页面参数设置
st.set_page_config(
    layout="wide",
    page_title='Metric Visual V1',
    page_icon='🔗'
)

# 页面标题
st.title('Metric Visualization V1')
st.markdown('***Constructed in June 11, 2023, this web is used to visualize the metric and the result of the model training.***')
st.markdown('***Version 1.0, Updated in June 12, 2023, MPX***')
st.divider()

# 侧边栏
with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")



# 参数监控台
metric_container = st.container()
metric_container.subheader('Params')

metric_name = 'Accuracy'
loss_name = 'CrossEntropy'
model_name = 'ResNet'
epoch = 55
all_epoch = 100
metric_num = 90
loss_num = 0.55863
params = {
    'lr': 0.05,
    'decay': 0.001,
    'momentum': '0.95',
    'augmentation': 'True'
}
progress_text = "Operation in progress. Please wait."

metric_block, tqdm_block = metric_container.columns(2)

vis_bar = tqdm_block.progress(0, text=progress_text)
vis_info = tqdm_block.info('##### ***The model is still training***')
bar_visual(epoch, vis_bar, progress_text)
metric_visual(metric_block, model_name, epoch, all_epoch, metric_name, metric_num, loss_name, loss_num, params)
# metric_container.divider()


# 可拖动图表监控台
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

layout = [
    dashboard.Item("editor", 0, 0, 6, 3),
    dashboard.Item("chart", 6, 0, 6, 3),
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        # 参数框
        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Result Viewer", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )
            with mui.CardActions:
                mui.Button("Apply changes", onClick=sync())
        # 图表
        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Chart", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Line(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )