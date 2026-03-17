import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

from opc_client import read_values

st.title("Automated Tank Monitoring System")

data = []

placeholder = st.empty()

while True:

    tank_level, valve_state, alarm_state = read_values()

    data.append(tank_level)

    df = pd.DataFrame(data, columns=["tank_level"])

    with placeholder.container():

        col1, col2, col3 = st.columns(3)

        col1.metric("Tank Level", round(tank_level,2))
        col2.metric("Valve State", valve_state)
        col3.metric("Alarm", alarm_state)

        WINDOW = 50
        df_window = df.tail(WINDOW)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=df_window["tank_level"],
                mode="lines",
                name="Tank Level"
            )
        )

        fig.update_layout(
            title="Tank Level Trend",
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        mean = df["tank_level"].mean()
        std = df["tank_level"].std()

        ucl = mean + 3 * std
        lcl = mean - 3 * std

        fig2 = go.Figure()

        fig2.add_trace(go.Scatter(
            y=df_window["tank_level"],
            mode="lines",
            name="Tank Level"
        ))

        fig2.add_trace(go.Scatter(
            y=[mean]*len(df_window),
            mode="lines",
            name="Mean"
        ))

        fig2.add_trace(go.Scatter(
            y=[ucl]*len(df_window),
            mode="lines",
            name="UCL"
        ))

        fig2.add_trace(go.Scatter(
            y=[lcl]*len(df_window),
            mode="lines",
            name="LCL"
        ))

        fig2.update_layout(
            title="SPC Control Chart",
            height=400
        )

        st.plotly_chart(fig2, use_container_width=True)

    time.sleep(1)