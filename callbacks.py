from dash import Input, Output, State, exceptions

from charts import tab2_hist_fig, tab2_pie_fig, tab3_bar_bigfig, tab4_broad_bigfig, tab4_niche_bigfig
from color import basic_layout
from data import tab2_data, tab3_data

def callbacks_master(app):
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
    
    @app.callback(
        Output("comp8_bigfig_tab3_OUT", "figure"),
        Input("comp7_dropdown_country_tab3_IN", "value"),
        Input("comp7_dropdown_segmentation_tab3_IN", "value"),
        Input("comp7_dropdown_individual_segment_tab3_IN", "value"),
        Input("comp7_dropdown_b_topic_tab3_IN", "value")
    )
    def callback_tab3_out(
        country, 
        segmentation, 
        individual_segment_lst, 
        broad_topic_lst
    ):
        if not individual_segment_lst:
            individual_segment_lst = ["1", "2", "3", "4", "5"]
        if not country:
            country = tab2_data["user_activity_post_count"]["question_user_country_code"].unique()
        return basic_layout(
            tab3_bar_bigfig(
                country, 
                segmentation, 
                individual_segment_lst, 
                broad_topic_lst
            )
        ).update_layout({
            "margin": {"t": 25}
        })

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
        Input("comp9_dropdown_sc_tab4_IN", "value"),
        Input("comp9_dropdown_country_tab4_IN", "value"),
        Input("comp9_dropdown_segmentation_tab4_IN", "value"),
        Input("comp9_dropdown_individual_segments_tab4_IN", "value"),
        Input("comp9_dropdown_b_topic_tab4_IN", "value"),
        Input("comp9_dropdown_n_topic_tab4_IN", "value"),
        Input("comp9_dropdown_time_tab4_IN", "value")
    )
    def callback_tab4_out(
        specificity,
        country, 
        segmentation, 
        individual_segment_lst, 
        broad_topic_lst,
        niche_topic_lst,
        time_slice
    ):
        if not broad_topic_lst:
            broad_topic_lst = ["crop"]
        if not broad_topic_lst:
            broad_topic_lst = ["maize"]
        if not individual_segment_lst:
            individual_segment_lst = ["1", "2", "3", "4", "5"]
        if not country:
            country = tab2_data["user_activity_post_count"]["question_user_country_code"].unique()

        if specificity=="Broad":
            return basic_layout(
                tab4_broad_bigfig(
                    country, 
                    segmentation, 
                    individual_segment_lst, 
                    broad_topic_lst,
                    time_slice
                )
            ).update_layout({
                "margin": {"t": 25}
            })
        else:
            return basic_layout(
                tab4_niche_bigfig(
                    country, 
                    segmentation, 
                    individual_segment_lst, 
                    broad_topic_lst,
                    niche_topic_lst,
                    time_slice
                )
            ).update_layout({
                "margin": {"t": 25}
            })