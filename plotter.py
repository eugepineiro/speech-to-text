import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def boxplot_metric_by_model(df, metric, models, title):
    fig = go.Figure()

    for model in models:
        group = df.groupby('model').get_group(model)[metric]
        fig.add_trace(go.Box(y=group, name=model))

    fig.update_layout(
        title=f"{metric} by Model {title}",
        xaxis_title="Model",
        yaxis_title=f"{metric}",
        font={'size': 18}
    )

    fig.show()

def boxplot_metric_by_postprocessing(metric, df, df_post, model):
    fig = go.Figure()

    group_df = df.groupby('model').get_group(model)[metric]
    group_df_post = df_post.groupby('model').get_group(model)[metric]

    fig.add_trace(go.Box(y=group_df, name='False'))
    fig.add_trace(go.Box(y=group_df_post, name='True'))

    fig.update_layout(
        title=f"WER Postprocessing impact for {model}",
        xaxis_title="Postprocessing",
        yaxis_title=f"{metric}",
        font={'size': 18}
    )

    fig.show()

def scatterplot_metric_by_time(df, metric, model):

    fig = px.scatter(df, x='exec_time_minutes', y=metric, color="model",
                     hover_data=["audio_name","exec_time_minutes","audio_len_minutes", "model"])

    fig.update_traces(marker_size=10)

    fig.update_layout(
        title=f"{metric} by Execution time for model {model} (Agent channel)",
        xaxis_title="Execution time (minutes)",
        yaxis_title=f"{metric}",
        font={'size': 18}
    )
    fig.show()

def scatterplot_metric_by_var_by_model(df, metric, var):

    fig = px.scatter(df, x=var, y=metric,
                     color='model', hover_data=["audio_name","exec_time_minutes","audio_len_minutes"])
    """
     group = df.groupby('model').get_group(model)[metric]
    fig.add_trace(go.Scatter(x=metric, y='exec_time_minutes',
                             mode='lines+markers',
                             name='model')) """

    fig.update_layout(
        title=f"{metric} by {var}",
        xaxis_title=f"{var}",
        yaxis_title=f"{metric}",
        font={'size': 18}
    )
    fig.show()


if __name__ == "__main__":

    PLOT_WER = True
    PLOT_PT = True

    df = pd.read_csv('analytics/model_performance_5.csv', delimiter=",")
    df_post = pd.read_csv('analytics/model_performance_postprocessing_5.csv', delimiter=",")

    # --------------- WER ----------------- #
    if PLOT_WER == True:
        boxplot_metric_by_model(df, 'WER', models=['whisper_large_v2', 'whisper_large_v3'], title="(raw)")
        boxplot_metric_by_model(df_post, 'WER', models=['whisper_large_v2', 'whisper_large_v3'], title="(with postprocessing)")

        boxplot_metric_by_postprocessing('WER', df, df_post, 'whisper_large_v2')
        boxplot_metric_by_postprocessing('WER', df, df_post, 'whisper_large_v3')

    # --------------- PROCESS TIME ----------------- #
    if PLOT_PT == True:
        boxplot_metric_by_model(df, 'exec_time_minutes', models=['whisper_large_v2', 'whisper_large_v3'], title="")
        print(df)
        #scatterplot_metric_by_var_by_model(df, 'exec_time_minutes', 'audio_len_minutes')

        scatterplot_metric_by_time(df, 'audio_len_minutes', 'whisper_large_v3')

        #scatterplot_metric_by_time(df, 'WER', 'whisper_large_v3')


