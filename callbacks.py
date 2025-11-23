from dash import Input, Output, State, exceptions
import plotly.graph_objects as go
import json

from charts import tab2_hist_fig, tab2_pie_fig, tab3_bar_bigfig, tab4_broad_bigfig, tab4_niche_bigfig, tab5_funnel_fig
from data import tab2_data, tab3_data, intersections
from color import basic_layout

def none_to_list(lst):
    return ["1", "2", "3", "4", "5"] if lst=="None" else [lst]

def none_to_string(input):
    return "None"


def callbacks_master(app):
############################################## tab 2 ##############################################

    @app.callback(
        Output("comp5_hist_fig_tab2_OUT", "figure"),
        Output("comp6_pie_fig_tab2_OUT", "figure"),
        Input("comp4_dropdown_country_tab2_IN", "value"),
        Input("comp4_dropdown_segmentation_tab2_IN", "value")
    )
    def callback_tab2_out(country, segmentation):
        return basic_layout(
            tab2_hist_fig(
                country, 
                segmentation
            )
        ), basic_layout(
            tab2_pie_fig(
                country, 
                segmentation
            )
        )

############################################## tab 5 (2.5, between 2 and 3) ##############################################

    @app.callback(
        Output("comp20_funnel_fig_tab5_OUT", "figure"),
        Output("comp19_cs_text_tab5_OUT", "children"),
        Input("comp19_dropdown_ua_cs_tab5_IN", "value"),
        Input("comp19_dropdown_spr_cs_tab5_IN", "value"),
        Input("comp19_dropdown_cs_cs_tab5_IN", "value"),
        Input("comp19_dropdown_ten_cs_tab5_IN", "value")
        )
    def callback_tab5_out(ua_cs, spr_cs, cs_cs, ten_cs):
        if not ua_cs:
            ua_cs = none_to_string(ua_cs)
        if not spr_cs:
            spr_cs = none_to_string(spr_cs)
        if not cs_cs:
            cs_cs = none_to_string(cs_cs)
        if not ten_cs:
            ten_cs = none_to_string(ten_cs)

        cs_combo_dct = {
            "unique_askers": none_to_list(cs_cs),
            "speed_post_response": none_to_list(spr_cs),
            "tenure": none_to_list(ten_cs),
            "user_activity_post_count": none_to_list(ua_cs)
        }

        cs_key_json = json.dumps(cs_combo_dct, sort_keys=True)
        cs_count = intersections["counts"][cs_key_json]["total"]

        segment_values_dct = {
            "user_activity_post_count": ua_cs,
            "speed_post_response": spr_cs,
            "unique_askers": cs_cs,
            "tenure": ten_cs
        }

        return (
            basic_layout(
                tab5_funnel_fig(
                    segment_values_dct
                )
            ),
            cs_count
        )


############################################## tab 3 ##############################################

    @app.callback(
        Output("comp8_bigfig_tab3_OUT", "figure"),
        Output("comp12_cs1_text_tab3_OUT", "children"),
        Output("comp17_cs2_text_tab3_OUT", "children"),
        Input("comp7_dropdown_country_tab3_IN", "value"),
        Input("comp7_dropdown_segmentation_tab3_IN", "value"),
        Input("comp7_dropdown_individual_segment_tab3_IN", "value"),
        Input("comp7_dropdown_b_topic_tab3_IN", "value"),
        Input("comp12_dropdown_ua_cs1_tab3_IN", "value"),
        Input("comp12_dropdown_spr_cs1_tab3_IN", "value"),
        Input("comp12_dropdown_cs_cs1_tab3_IN", "value"),
        Input("comp12_dropdown_ten_cs1_tab3_IN", "value"),
        Input("comp17_dropdown_ua_cs2_tab3_IN", "value"),
        Input("comp17_dropdown_spr_cs2_tab3_IN", "value"),
        Input("comp17_dropdown_cs_cs2_tab3_IN", "value"),
        Input("comp17_dropdown_ten_cs2_tab3_IN", "value")

    )
    def callback_tab3_out(
        country, 
        segmentation, 
        individual_segment_lst, 
        broad_topic_lst,
        ua_cs1,
        spr_cs1,
        cs_cs1,
        ten_cs1,
        ua_cs2,
        spr_cs2,
        cs_cs2,
        ten_cs2

    ):

        if not individual_segment_lst:
            individual_segment_lst = ["1", "2", "3", "4", "5"]
        if not country:
            country = tab2_data["user_activity_post_count"]["question_user_country_code"].unique()
        if not ua_cs1:
            ua_cs1 = none_to_string(ua_cs1)
        if not spr_cs1:
            spr_cs1 = none_to_string(spr_cs1)
        if not cs_cs1:
            cs_cs1 = none_to_string(cs_cs1)
        if not ten_cs1:
            ten_cs1 = none_to_string(ten_cs1)
        if not ua_cs2:
            ua_cs2 = none_to_string(ua_cs2)
        if not spr_cs2:
            spr_cs2 = none_to_string(spr_cs2)
        if not cs_cs2:
            cs_cs2 = none_to_string(cs_cs2)
        if not ten_cs2:
            ten_cs2 = none_to_string(ten_cs2)

        cs1_combo_dct = {
            "unique_askers": none_to_list(cs_cs1),
            "speed_post_response": none_to_list(spr_cs1),
            "tenure": none_to_list(ten_cs1),
            "user_activity_post_count": none_to_list(ua_cs1)
        }

        cs1_key_json = json.dumps(cs1_combo_dct, sort_keys=True)
        cs1_count = intersections["counts"][cs1_key_json]["total"]

        cs2_combo_dct = {
            "unique_askers": none_to_list(cs_cs2),
            "speed_post_response": none_to_list(spr_cs2),
            "tenure": none_to_list(ten_cs2),
            "user_activity_post_count": none_to_list(ua_cs2)
        }

        cs2_key_json = json.dumps(cs2_combo_dct, sort_keys=True)
        cs2_count = intersections["counts"][cs2_key_json]["total"]


        return (
            basic_layout(
                tab3_bar_bigfig(
                    country, 
                    segmentation, 
                    individual_segment_lst, 
                    broad_topic_lst,
                    cs1_key_json,
                    cs2_key_json
                )
            ).update_layout({
                "margin": {"t": 25}
            }),
            cs1_count,
            cs2_count
        )

    @app.callback(
        Output('comp12_dropdown_ua_cs1_tab3_IN', 'value'),
        Input('comp7_dropdown_segmentation_tab3_IN', 'value'),
        State('comp12_dropdown_ua_cs1_tab3_IN', 'value'),
        prevent_initial_call=True
    )
    def preserve_custom_segment(segmentation, current_value):
        # Don't change the value, just return what it already was
        return current_value if current_value else 'None'


############################################## tab 4 ##############################################

    @app.callback(
        Output("comp9_dropdown_n_topic_tab4_IN", "data"),
        Output("comp9_dropdown_n_topic_tab4_IN", "value"),
        Input("comp9_dropdown_b_topic_tab4_IN", "value"),
        State("comp9_dropdown_segmentation_tab4_IN", "value"),
        State("comp9_dropdown_n_topic_tab4_IN", "value")
    )
    def filter_niche_by_broad(broad_topics, segmentation, current_niches):
        df = tab3_data["niche"][segmentation]
        
        if not broad_topics:
            niche_options = df["niche"].unique().tolist()
        else:
            niche_mk = df["broad_type"].isin(broad_topics)
            niche_options = df[niche_mk]["niche"].unique().tolist()
        
        if current_niches:
            new_value = [n for n in current_niches if n in niche_options]
        else:
            new_value = []
        
        if not new_value and niche_options:
            new_value = [niche_options[0]]

        return niche_options, new_value

    @app.callback(
        Output("comp10_bigfig_tab4_OUT", "figure"),
        Output("comp13_cs1_text_tab4_OUT", "children"),
        Output("comp18_cs2_text_tab4_OUT", "children"),  
        Input("comp9_dropdown_sc_tab4_IN", "value"),
        Input("comp9_dropdown_country_tab4_IN", "value"),
        Input("comp9_dropdown_segmentation_tab4_IN", "value"),
        Input("comp9_dropdown_individual_segments_tab4_IN", "value"),
        Input("comp9_dropdown_b_topic_tab4_IN", "value"),
        Input("comp9_dropdown_n_topic_tab4_IN", "value"),
        Input("comp9_dropdown_time_tab4_IN", "value"),
        Input("comp13_dropdown_ua_cs1_tab4_IN", "value"),
        Input("comp13_dropdown_spr_cs1_tab4_IN", "value"),
        Input("comp13_dropdown_cs_cs1_tab4_IN", "value"),
        Input("comp13_dropdown_ten_cs1_tab4_IN", "value"),
        Input("comp18_dropdown_ua_cs2_tab4_IN", "value"),
        Input("comp18_dropdown_spr_cs2_tab4_IN", "value"),
        Input("comp18_dropdown_cs_cs2_tab4_IN", "value"),
        Input("comp18_dropdown_ten_cs2_tab4_IN", "value")        

    )
    def callback_tab4_out(
        specificity,
        country, 
        segmentation, 
        individual_segment_lst, 
        broad_topic_lst,
        niche_topic_lst,
        time_slice,
        ua_cs1,
        spr_cs1,
        cs_cs1,
        ten_cs1,
        ua_cs2,
        spr_cs2,
        cs_cs2,
        ten_cs2
    ):
        if not broad_topic_lst:
            broad_topic_lst = ["crop"]
        if not broad_topic_lst:
            broad_topic_lst = ["maize"]
        if not individual_segment_lst:
            individual_segment_lst = ["1", "2", "3", "4", "5"]
        if not country:
            country = tab2_data["user_activity_post_count"]["question_user_country_code"].unique()
        if not ua_cs1:
            ua_cs1 = none_to_string(ua_cs1)
        if not spr_cs1:
            spr_cs1 = none_to_string(spr_cs1)
        if not cs_cs1:
            cs_cs1 = none_to_string(cs_cs1)
        if not ten_cs1:
            ten_cs1 = none_to_string(ten_cs1)
        if not ua_cs2:
            ua_cs2 = none_to_string(ua_cs2)
        if not spr_cs2:
            spr_cs2 = none_to_string(spr_cs2)
        if not cs_cs2:
            cs_cs2 = none_to_string(cs_cs2)
        if not ten_cs2:
            ten_cs2 = none_to_string(ten_cs2)

        cs1_combo_dct = {
            "unique_askers": none_to_list(cs_cs1),
            "speed_post_response": none_to_list(spr_cs1),
            "tenure": none_to_list(ten_cs1),
            "user_activity_post_count": none_to_list(ua_cs1)
        }

        cs1_key_json = json.dumps(cs1_combo_dct, sort_keys=True)
        cs1_count = intersections["counts"][cs1_key_json]["total"]


        cs2_combo_dct = {
            "unique_askers": none_to_list(cs_cs2),
            "speed_post_response": none_to_list(spr_cs2),
            "tenure": none_to_list(ten_cs2),
            "user_activity_post_count": none_to_list(ua_cs2)
        }

        cs2_key_json = json.dumps(cs2_combo_dct, sort_keys=True)
        cs2_count = intersections["counts"][cs2_key_json]["total"]


        if specificity=="Broad":
            return (
                basic_layout(
                    tab4_broad_bigfig(
                        country, 
                        segmentation, 
                        individual_segment_lst, 
                        broad_topic_lst,
                        time_slice,
                        cs1_key_json,
                        cs2_key_json
                    )
                ).update_layout({
                    "margin": {"t": 25}
                }),
                cs1_count,
                cs2_count
            )
        else:
            return (
                basic_layout(
                    tab4_niche_bigfig(
                        country, 
                        segmentation, 
                        individual_segment_lst, 
                        broad_topic_lst,
                        niche_topic_lst,
                        time_slice,
                        cs1_key_json,
                        cs2_key_json
                    )
                ).update_layout({
                    "margin": {"t": 25}
                }),
                cs1_count,
                cs2_count
            )