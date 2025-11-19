import pandas as pd
import numpy as np

from dash import html, dcc, _dash_renderer
from dash_iconify import DashIconify
import dash_mantine_components as dmc
_dash_renderer._set_react_version('18.2.0')

from data import tab1_data, tab2_data, tab3_data, tab4_data
from charts import tab1_geo_fig
from color import basic_layout

# # # # # # # # # # # # # # basic layout # # # # # # # # # # # # # # 

############################################## tab 1 ##############################################

comp1_geo_fig_tab1 = dmc.Card(
    [
        dcc.Graph(
            figure=basic_layout(tab1_geo_fig), 
            id="comp1_geo_fig_tab1", 
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp1_geo_card"
)

comp3_text = dmc.Card(
    [
        dmc.Text(
            [
                "DataKind DataKit: Smallholder Farmers"
            ],
            fw=500,
            size="l",
            className="text_header"
        ),
        dmc.Text(
            "Smallholder farmers are individuals or families who manage relatively small plots of land, often relying on family labor and traditional farming methods. Despite their small scale, they play a central role in global food systems, producing up to one-third of the world’s food supply and forming the backbone of rural economies across Africa, Asia, and Latin America. Their livelihoods are closely tied to the land and weather, making them both essential contributors to food security, and highly vulnerable to environmental and market changes.",
            c="gray",
            size="xs",
            className="text_standard_intro"
        ),
        dmc.Text(
            "Understanding smallholder farmers and the challenges they face is key for building resilient agricultural systems and sustainable rural development. By studying their behaviors and needs organizations can design better tools, information services, and policies that directly improve productivity, income, and climate resilience. Data-driven insights into their practices not only empower farmers themselves, but also strengthen local economies and contribute to broader goals such as poverty reduction and food sustainability.",
            c="gray",
            size="xs",
            className="text_standard_intro text_nomargin"
        ),

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp3_text_card"
)

inline_comp_3_0 = html.Div(
    [
        comp3_text,
    ],
    className="in inline_comp_3_0"
)

tab1 = html.Div(
    [
        inline_comp_3_0,
        comp1_geo_fig_tab1
    ],
    className="d d1"
)


############################################## tab 2 ##############################################
comp4_dropdown_tab2 = dmc.Card(
    [
        dmc.Select(
                label="Country",
                placeholder="select...",
                value=tab2_data["user_activity_post_count"]["question_user_country_code"].unique()[0],
                data=tab2_data["user_activity_post_count"]["question_user_country_code"].unique(),
                clearable=False,
                id="comp4_dropdown_country_tab2_IN"
            ),
        dmc.Select(
                label="Segmentation",
                placeholder="select...",
                value="user_activity_post_count",
                data=["user_activity_post_count", "speed_post_response", "conversation_starters", "tenure"],
                clearable=False,
                id="comp4_dropdown_segmentation_tab2_IN"
            )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t f-child comp3_dropdown_tab2_card"
)


comp4_center_filter_tab2 = html.Div(
    [
        comp4_dropdown_tab2
    ],
    className="f f-parent"
)


comp5_hist_fig_tab2 = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp5_hist_fig_tab2_OUT",
            # style={"height": "100%", "width": "100%"}
            )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp5_hist_fig_tab2_card"   
)

comp6_pie_fig_tab2 = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp6_pie_fig_tab2_OUT", 
            # style={"height": "100%", "width": "100%"}
            )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp6_pie_fig_tab2_card"   
)

grid_tab2 = html.Div(
    [
        comp5_hist_fig_tab2,
        comp6_pie_fig_tab2
    ],
    className="d d2"

)

tab2 = html.Div(
    [
        comp4_center_filter_tab2,
        grid_tab2
    ],
    className="a tab2_all"
)

############################################## tab 3 ##############################################
comp7_dropdown_tab3 = dmc.Card(
    [
        dmc.MultiSelect(
            label="Country",
            placeholder="select...",
            value=tab2_data["user_activity_post_count"]["question_user_country_code"].unique(),
            data=tab2_data["user_activity_post_count"]["question_user_country_code"].unique(),
            maxValues=2,
            clearable=False,
            id="comp7_dropdown_country_tab3_IN"
        ),
        dmc.Select(
                label="Segmentation",
                placeholder="...",
                value="user_activity_post_count",
                data=["user_activity_post_count", "speed_post_response", "conversation_starters", "tenure"],
                clearable=False,
                id="comp7_dropdown_segmentation_tab3_IN"
            ),
        dmc.MultiSelect(
            label="Individual segments",
            placeholder="select multiple...",
            value=["1", "5"],
            data=["1", "2", "3", "4", "5"],
            clearable=False,
            id="comp7_dropdown_individual_segment_tab3_IN"
        ),
        dmc.MultiSelect(
            label="Broad topic",
            placeholder="select multiple...",
            value=["livestock"],
            data=tab3_data["niche"]["user_activity_post_count"]["broad_type"].unique(),
            clearable=True,
            id="comp7_dropdown_b_topic_tab3_IN"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t f-child comp7_dropdown_tab3_card"
)

comp7_center_filter_tab3 = html.Div(
    [
        comp7_dropdown_tab3
    ],
    className="f f-parent"
)

comp8_bigfig_tab3 = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp8_bigfig_tab3_OUT", style={"height": "100%"})
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp8_bigfig_tab3_card",
    style={"height": "100%"}

)

tab3 = html.Div(
    [
        comp7_center_filter_tab3,
        comp8_bigfig_tab3
    ],
    className="a tab3_all"
)

############################################## tab 4 ##############################################
comp9_dropdown_tab4 = dmc.Card(
       [
        dmc.SegmentedControl(
            orientation="horizontal",
            id="comp9_dropdown_sc_tab4_IN",
            value="Broad",
            style={"width": "100%"},
            data=[
                {"value": "Broad", "label": "Broad"},
                {"value": "Niche", "label": "Niche"},
            ],
        ),
        dmc.MultiSelect(
            label="Country",
            placeholder="select multiple...",
            value=tab2_data["user_activity_post_count"]["question_user_country_code"].unique(),
            data=tab2_data["user_activity_post_count"]["question_user_country_code"].unique(),
            maxValues=2,
            clearable=False,
            id="comp9_dropdown_country_tab4_IN"
        ),
        dmc.Select(
                label="Segmentation",
                placeholder="select...",
                value="user_activity_post_count",
                data=["user_activity_post_count", "speed_post_response", "conversation_starters", "tenure"],
                clearable=False,
                id="comp9_dropdown_segmentation_tab4_IN"
            ),
        dmc.MultiSelect(
            label="Individual segments",
            placeholder="select multiple...",
            value=["1","5"],
            data=["1", "2", "3", "4", "5"],
            clearable=False,
            id="comp9_dropdown_individual_segments_tab4_IN"
        ),
        dmc.MultiSelect(
            label="Broad topic",
            placeholder="select multiple...",
            value=["livestock"],
            data=tab3_data["niche"]["user_activity_post_count"]["broad_type"].unique(),
            maxValues=4,
            clearable=True,
            id="comp9_dropdown_b_topic_tab4_IN"
        ),
        dmc.MultiSelect(
            label="Niche topic",
            placeholder="select multiple...",
            value=["animals"],
            data=tab3_data["niche"]["user_activity_post_count"]["niche"].unique(),
            maxValues=4,
            clearable=True,
            id="comp9_dropdown_n_topic_tab4_IN"
        ),
        dmc.Select(
            label="Time slice",
            placeholder="select...",
            value=list(tab4_data["broad"]["user_activity_post_count"].keys())[0],
            data=list(tab4_data["broad"]["user_activity_post_count"].keys()),
            clearable=True,
            id="comp9_dropdown_time_tab4_IN"
        ) 
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t f-child comp7_dropdown_tab3_card"
)

comp9_center_filter_tab4 = html.Div(
    [
        comp9_dropdown_tab4
    ],
    className="f f-parent"
)

comp10_bigfig_tab4 = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp10_bigfig_tab4_OUT")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp10_bigfig_tab4_card"
)

tab4 = html.Div(
    [
        comp9_center_filter_tab4,
        comp10_bigfig_tab4,
    ],
    className="a tab4_all"
)


# # # # # # # # # # # # # # tabs # # # # # # # # # # # # # # 

Tabs = html.Div(
    [
        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.TabsTab(
                            "Geography",
                            leftSection=DashIconify(icon="material-symbols:travel-explore-rounded", width=20, color="black", className="icons-2"),
                            value="Geography"
                        ),
                        dmc.TabsTab(
                            "Segments",
                            leftSection=DashIconify(icon="material-symbols:modeling-outline-rounded", width=20, color="black", className="icons-2"),
                            value="Segments"),
                        dmc.TabsTab(
                            "Topics",
                            leftSection=DashIconify(icon="material-symbols:explore-outline-rounded", width=20, color="black", className="icons-2"),
                            value="Topics"
                        ),
                        dmc.TabsTab(
                            "Time",
                            leftSection=DashIconify(icon="fluent:arrow-sort-up-lines-24-regular", width=20, color="black", className="icons-2"),
                            value="Time"
                        )
                    ]
                ),
                dmc.TabsPanel(
                    tab1,
                    value="Geography"
                ),
                dmc.TabsPanel(
                    tab2,
                    value="Segments"
                ),
                dmc.TabsPanel(
                    tab3,
                    value="Topics"
                ),        
                dmc.TabsPanel(
                    tab4,
                    value="Time"
                ),
            ],
            color="blue",
            value="Geography",
            variant="outline"
        )
    ],
    className="tabs_main nm"
)


# # # # # # # # # # # # # # title # # # # # # # # # # # # # #


title = dmc.Card(
    [
        dmc.Text(
            "Smallholder Farmers in East Africa",
            size="xl",
            fw=600
            )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t tit nm",
)

# # # # # # # # # # # # # # footer # # # # # # # # # # # # # #

color = "white"

icon_datakind = html.Img(src="/assets/DK_LOGO_R_ORG-2.png", style={"width": "100px"})
link_datakind = "https://www.datakind.org/"

icon_producers_direct = html.Img(src="/assets/Producers-Direct_Logo_500x500.png", style={"width": "100px"})
link_producers_direct = "https://producersdirect.org/"


comp32_datakind = dmc.Anchor(
    icon_datakind, href=link_datakind, target="_blank",
    size="xl",
    className="footnt-child"
)

comp33_producers_direct = dmc.Anchor(
    icon_producers_direct, href=link_producers_direct, target="_blank",
    size="xl",
    className="footnt-child"
)

comp25_copyrightfooter = html.P(
    "© Benjamin Noyes 2025 all rights reserved",
    className="footertinytext"
)

comp34_datakind_parent = html.Div(
    [
        comp32_datakind
    ],
    className="footnt-parent"
)

comp35_datakind_parent = html.Div(
    [
        comp33_producers_direct
    ],
    className="footnt-parent"
)


comp26_icons = html.Div(
    [
        comp34_datakind_parent,
        comp35_datakind_parent
    ],
    className="footie-middle"
)


footer = dmc.Card(
    [
        comp26_icons,
        comp25_copyrightfooter
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t footie-all nm",
)

# # # # # # # # # # # # # # mobile # # # # # # # # # # # # # #

mobile_error = html.Div(
    [
        dmc.Card(
            [
                dmc.Text(
                    "This dashboard is not optimized for mobile. Please access from a desktop.",
                    size="xs",
                )
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            className="mn-1"
        )
    ],
    className="mn-2"
)
############################### composition ##################################

lyt = dmc.MantineProvider(
    [
        title,
        Tabs,
        footer,
        mobile_error
    ]
)