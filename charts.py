from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import requests


from data import tab1_data, tab2_data, tab3_data, tab4_data
from color import segment_colors_dct

############################################## tab 1 ##############################################

vc_country = pd.Series(tab1_data)

geojson_url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
geojson = requests.get(geojson_url).json()

tab1_geo_fig = px.choropleth_mapbox(
  vc_country,
  geojson = geojson,
  featureidkey="properties.ISO_A2",
  locations=vc_country.index,
  color=vc_country.values,
  color_continuous_scale="Mint",
  mapbox_style="carto-positron",
  zoom=4,
  center={"lat":0, "lon": 35},
  opacity=0.5,
  range_color=[0, vc_country.values.max()]
).update_layout({
  "title": {"text": "Geographic region", "x": 0.5}
})

############################################## tab 2 ##############################################

def tab2_hist_fig(country_code, segmentation_name):

  df = tab2_data[segmentation_name]

  fig = px.bar(
    df[df["question_user_country_code"]==country_code], 
    x=segmentation_name, 
    y="n",
    color=segmentation_name,
    color_discrete_map=segment_colors_dct
  )

  return fig.update_layout({
    "title": {"text": f"{country_code}, {segmentation_name}", "x": 0.5},
    "xaxis": {"title": "segments"},
  })


def tab2_pie_fig(country_code, segmentation_name):

  df = tab2_data[segmentation_name]

  fig = px.pie(
    df[df["question_user_country_code"]==country_code], 
    names=segmentation_name, 
    values="n",
    color=segmentation_name,
    color_discrete_map=segment_colors_dct
  )
  fig.update_traces(
    hovertemplate="segment %{label}"
  )

  return fig.update_layout({
    "title": {"text": f"{country_code}, {segmentation_name}", "x": 0.5},
    "showlegend": False,
  })

############################################## tab 3 ##############################################

def tab3_bar_bigfig(country_codes, segmentation_name, individual_segment_lst, broad_category_lst):
  df_b = tab3_data["broad"][segmentation_name]
  df_n = tab3_data["niche"][segmentation_name]

  bigfig = make_subplots(
    2, len(country_codes),
    subplot_titles=[
      f"{country} {topic}" for topic in ["broad topics", "niche topics"] 
      for country in country_codes
    ],
    vertical_spacing=0.2
  )

  for idx, country in enumerate(country_codes):
    df_sub_broad = df_b[df_b["question_user_country_code"]==country]

    niche_mk = (df_n["question_user_country_code"]==country)
    if broad_category_lst:
      niche_mk &= (df_n["broad_type"].isin(broad_category_lst))
    df_sub_niche = df_n[niche_mk]

    segment_order_lst = ["1", "2", "3", "4", "5"]
    segment_final_lst = [j for j in segment_order_lst if j in individual_segment_lst]
    for segment in segment_final_lst:
      df_trace_broad = df_sub_broad[df_sub_broad[segmentation_name]==segment]
      df_trace_niche = df_sub_niche[df_sub_niche[segmentation_name]==segment]
      bigfig.add_trace(
        go.Bar(
          x=df_trace_broad["category"],
          y=df_trace_broad["pct"],
          showlegend=(idx==0),
          marker={
            "color": df_trace_broad["segment_color"],
          },
          name=segment
        ),
        row=1, col=idx+1
      ).add_trace(
        go.Bar(
          x=df_trace_niche["category"],
          y=df_trace_niche["pct"],
          showlegend=False,
          marker={
            "color": df_trace_niche["segment_color"],
          },
          name=segment
        ),
        row=2, col=idx+1
      )

  return bigfig

############################################## tab 4 ##############################################

def tab4_broad_bigfig(country_codes, segmentation_name, individual_segment_lst, broad_category_lst, time_slice):

    df = tab4_data["broad"][segmentation_name][time_slice]

    bigfig = make_subplots(
      len(broad_category_lst), len(country_codes),
      subplot_titles=[
        f"{cat}: {country}"
        for cat in broad_category_lst
        for country in country_codes
      ],
      vertical_spacing=0.1,
      row_heights=[300] * len(broad_category_lst)
    )

    for idx_col, country in enumerate(country_codes):
      df_country = df[df["question_user_country_code"]==country]
      for idx_row, cat in enumerate(broad_category_lst):
        df_cat = df_country[df_country["category"]==cat]

        segment_order_lst = ["1", "2", "3", "4", "5"]
        segment_final_lst = [j for j in segment_order_lst if j in individual_segment_lst]
        for segment in segment_final_lst:
          df_segment = df_cat[df_cat[segmentation_name]==segment]

          bigfig.add_trace(
            go.Scatter(
              x=df_segment[time_slice],
              y=df_segment["pct"],
              mode="lines+markers",
              marker={"color": df_segment["segment_color"].values},
              line={"color": df_segment["segment_color"].iloc[0]},
              showlegend=(idx_row==0 and idx_col==0),
              name=segment
            ),
            row=idx_row+1, col=idx_col+1
          )

    return bigfig.update_layout({
      "height": 300 * len(broad_category_lst)
    })


def tab4_niche_bigfig(country_codes, segmentation_name, individual_segment_lst, broad_category_lst, niche_category_lst, time_slice):

    df = tab4_data["niche"][segmentation_name][time_slice]

    if not niche_category_lst:
      niche_category_lst=["maize"]

    niche_mk = pd.Series(True, index=df.index)
    if niche_category_lst:
      niche_mk &= (df["niche"].isin(niche_category_lst))
    df_sub_niche = df[niche_mk]


    bigfig = make_subplots(
      len(niche_category_lst), len(country_codes),
      subplot_titles=[
        f"{cat}: {country}"
        for cat in niche_category_lst
        for country in country_codes
      ],
      vertical_spacing=0.1,
      row_heights=[300] * len(niche_category_lst)
    )

    for idx_col, country in enumerate(country_codes):
      df_country = df_sub_niche[df_sub_niche["question_user_country_code"]==country]
      for idx_row, cat in enumerate(niche_category_lst):
        df_cat = df_country[df_country["niche"]==cat]

        segment_order_lst = ["1", "2", "3", "4", "5"]
        segment_final_lst = [j for j in segment_order_lst if j in individual_segment_lst]
        for segment in segment_final_lst:
          df_segment = df_cat[df_cat[segmentation_name]==segment]

          bigfig.add_trace(
            go.Scatter(
              x=df_segment[time_slice],
              y=df_segment["pct"],
              mode="lines+markers",
              marker={"color": df_segment["segment_color"].values},
              line={"color": df_segment["segment_color"].iloc[0]},
              showlegend=(idx_row==0),
              name=segment
            ),
            row=idx_row+1, col=idx_col+1
          )

    return bigfig.update_layout({
      "height": 300 * len(niche_category_lst)
    })