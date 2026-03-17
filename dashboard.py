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
        if valve_state:
            col2.success("Valve OPEN")
        else:
            col2.warning("Valve CLOSED")
        if alarm_state:
            col3.error("ALARM ACTIVE")
        else:
            col3.success("System Normal")

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=tank_level,
            title={'text': "Tank Level (%)"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "blue"},
                'steps': [
                    {'range': [0,30], 'color': "lightgray"},
                    {'range': [30,80], 'color': "lightgreen"},
                    {'range': [80,100], 'color': "orange"}
                ]
            }
        ))

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

    #with placeholder.container():
        
        # st.plotly_chart(gauge, use_container_width=True)
        st.plotly_chart(gauge, use_container_width=True, key=f"gauge_{len(data)}")
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

    time.sleep(1)