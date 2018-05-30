import _plotly_utils.basevalidators


class IconsizeValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='iconsize',
        parent_name='layout.mapbox.layer.symbol',
        **kwargs
    ):
        super(IconsizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            **kwargs
        )