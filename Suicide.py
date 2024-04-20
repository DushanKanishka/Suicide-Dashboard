import dash
import pandas as pd
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objects as go
from datetime import datetime
import base64
# Load the dataset
df = pd.read_csv('Suicide data.csv')
#filtered_df = df[(df['year'] >= 2000) & (df['year'] <= 2015)]

# Initialize the Dash app
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css', 'custom.css']
app = dash.Dash(title="Suicide Rates App",external_stylesheets=external_stylesheets, suppress_callback_exceptions=True, prevent_initial_callbacks='initial_duplicate')
server = app.server
app.title = "Suicide Rates"

# Define the layout components
title = html.Div(
    children=[
        html.H1(
            "𝙎𝙐𝙄𝘾𝙄𝘿𝙀 𝙍𝘼𝙏𝙀𝙎 𝘼𝙉𝘼𝙇𝙔𝙎𝙄𝙎",
            style={'font-size': '30px', 'text-align': 'center', 'font-weight': 'bold', 'color': '#FDFEFE',
                   'backgroundColor': '#273746', 'margin': '1px', 'padding': '2px'}
        )
    ]
)

footer = html.Div(
    children=[
        html.Div(
            [
                html.P('CREATED BY:', style={'font-size': '10px', 'text-align': 'center', 'font-weight': 'bold',
                                              'color': 'black', 'margin-bottom': '3px', 'margin-top': '3px'}),
                html.P('Dushan:COHANDDS-018', style={'font-size': '9px', 'text-align': 'center',
                                                      'font-weight': 'bold', 'color': 'black', 'margin-bottom': '3px', 'margin-top': '3px'}),
                html.P('Akash:COHANDDS-011', style={'font-size': '9px', 'text-align': 'center',
                                                      'font-weight': 'bold', 'color': 'black', 'margin-bottom': '3px', 'margin-top': '0px'}),
            ],
            style={'background-color': '#EAECEE', 'padding': '5px', 'border-radius': '5px', 'margin-bottom': '0px',
                   'position': 'fixed', 'bottom': '0', 'right': '0', 'width': '10%', 'height': '60px',
                   'display': 'flex', 'flex-direction': 'column', 'justify-content': 'flex-start', 'align-items': 'center'}
        )
    ]
)


# Define the app layout
app.layout = html.Div([
    title,
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                id = 'tab-1',
                label='𝘐𝘯𝘵𝘳𝘰𝘥𝘶𝘤𝘵𝘪𝘰𝘯',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style={'font-size': '20px','backgroundColor': '#D6DBDF', 'color': 'black'}
            ),
            dcc.Tab(
                id = 'tab-2',
                label='𝘓𝘪𝘯𝘦 𝘊𝘩𝘢𝘳𝘵',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style={'font-size': '20px','backgroundColor': '#D6DBDF', 'color': 'black'}
            ),
            dcc.Tab(
                id = 'tab-3',
                label='𝘚𝘤𝘢𝘵𝘵𝘦𝘳 𝘗𝘭𝘰𝘵',
                value='tab-3',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style={'font-size': '20px','backgroundColor': '#D6DBDF', 'color': 'black'}
            ),
            dcc.Tab(
                id = 'tab-4',
                label='𝘐𝘯𝘵𝘦𝘳𝘢𝘤𝘵𝘪𝘷𝘦 𝘊𝘩𝘢𝘳𝘵',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style={'font-size': '20px','backgroundColor': '#D6DBDF', 'color': 'black'}
            ),
            dcc.Tab(
                id = 'tab-5',
                label='𝘈𝘯𝘢𝘭𝘺𝘴𝘪𝘴 𝘰𝘧 𝘴𝘶𝘪𝘤𝘪𝘥𝘦',
                value='tab-5',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style={'font-size': '20px','backgroundColor': '#D6DBDF', 'color': 'black'}
            ),
        ]
    ),
    html.Div(id='tabs-content-classes',),
    footer
],style={'backgroundColor': '#121212', 'color': '#ffffff'})


with open("image.jpg", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()
# Tab-1 Layout
@app.callback(Output('tab-1', 'children'),
              Input('tabs-with-classes', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        introduction = """
# *Introduction*

## This dashboard analyzes suicide rates by country using data from a specified period.
_____________________   
### Data Overview:
**Data Source:** [Suicide Rates Overview 1985 to 2016](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016)  
**Time Period:** [1985 to 2016] 

### Variables:
#### &bull; `country`: The name of the country where the data is recorded.  
#### &bull; `year`: The year in which the data is recorded.  
#### &bull; `sex`: The gender (male or female) for which the data is reported.  
#### &bull; `age`: The age group to which the data corresponds.  
#### &bull; `suicides_no`: The number of suicides reported for a specific group.  
#### &bull; `population`: The population count for a specific group.  
#### &bull; `suicides/100k_pop`: The number of suicides per 100,000 population.  
#### &bull; `gdp_per_capita`: The GDP per capita, representing the economic output per person.  
#### &bull; `gdp_for_year`: The gross domestic product (GDP) for a specific year.
    
        """

        return html.Div(
            children=[
                dcc.Markdown(introduction),
                html.Div(
                    style={  # Set margin and padding to zero
                        'position': 'absolute',
                        'top': '0',
                        'left': '0',
                        'width': '100%',
                        'height': '100%',
                        'margin': '0',
                        'padding': '0',
                        'z-index': '-1'
                    },
                        children=[
                            html.Img(
                                src=f"data:image/jpeg;base64,{encoded_image}",
                                style={'width': '100%', 'height': '100%', 'object-fit': 'cover',}
                            )
                        ]
                )
            ],
            style={'text-align': 'center', 'height': 'calc(108vh - 180px)', 'position': 'relative', 'z-index': '0'}
        )
    else:
        return []

# Tab-2 Layout
@app.callback(
    Output('tab-2', 'children'),
    Input('tabs-with-classes', 'value')
)
def render_content(tab):
    if tab == 'tab-2':
        return html.Div([
            dcc.Dropdown(
                id='y-axis-dropdown',
                options=[
                    {'label': 'Total Suicides', 'value': 'Total_suicides'},
                    {'label': 'Suicides per 100k', 'value': 'suicides_per_100k'},
                    {'label': 'GDP per Capita', 'value': 'gdp_per_capita'}
                ],
                value='Total_suicides',
                clearable=False, 
                style={'margin-bottom': '20px', 'backgroundColor': '#EBF5FB', 'color': '#273746'},
                className='dropdown-options'  
            ),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['country'].unique()],
                clearable=False, 
                style={'margin-bottom': '20px', 'backgroundColor': '#EBF5FB', 'color': '#273746'}
            ),
            html.Div(
                dcc.RangeSlider(
                    id='year-range-slider',
                    min=df['year'].min(),
                    max=df['year'].max(),
                    step=1,
                    value=[df['year'].min(), df['year'].max()],
                    marks={str(year): {'label': str(year), 'style': {'color': '#273746'}} for year in df['year'].unique()},
                    allowCross=False
                ),
                style={'backgroundColor': '#EBF5FB', 'margin-bottom': '20px'}
            ),
            dcc.Graph(id='line-chart')
        ],
        style={'backgroundColor': '#566573', 'color': '#000000'})  # Light background and black text
    else:
        return []




# TAb-2 Functions
@app.callback(
    Output('line-chart', 'figure'),
    [Input('y-axis-dropdown', 'value'),
     Input('country-dropdown', 'value'),
     Input('year-range-slider', 'value')]
)
def update_line_chart(y_axis, selected_country, selected_year_range):
    df2 = df[(df['country'] == selected_country) &
             (df['year'].between(selected_year_range[0], selected_year_range[1]))]
    grouped_data = df2.groupby('year').agg(
        Total_suicides=pd.NamedAgg('suicides_no', lambda x: round(x.sum())),
        suicides_per_100k=pd.NamedAgg('suicides/100k_pop', 'mean'),
        gdp_per_capita=pd.NamedAgg('gdp_for_capita_$', 'mean')).reset_index()
    
    fig = px.line(grouped_data, x='year', y=y_axis, title=f'{y_axis} for {selected_country}')
    
    # Set background color and font color
    fig.update_layout(
        plot_bgcolor='#EBEDEF',  # Background color
        font=dict(color='#000000')  # Font color
    )
    
    return fig


# Tab-3 Layout
@app.callback(
    Output('tab-3', 'children'),
    Input('tabs-with-classes', 'value'),
)
def render_content(tab):
    if tab == 'tab-3':
        return html.Div(
            [
                dcc.RadioItems(
                    id='y-axis-radio',
                    options=[
                        {'label': 'Population', 'value': 'population'},
                        {'label': 'Suicides/100k_pop', 'value': 'suicides/100k_pop'},
                        {'label': 'GDP for Year', 'value': '_gdp_for_year__$_'},
                        {'label': 'GDP for Capita', 'value': 'gdp_for_capita_$'}
                    ],
                    value='population',
                    labelStyle={'display': 'inline-block', 'margin-right': '20px'},
                    style={'margin-bottom': '20px', 'backgroundColor': '#EBF5FB', 'color': '#273746'}
                ),

                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': country, 'value': country} for country in df['country'].unique()],
                    multi=True,
                    value=[],  
                    style={'margin-bottom': '20px', 'backgroundColor': '#EBF5FB', 'color': '#273746'}
                ),

                html.Div(
                    dcc.RangeSlider(
                        id='year-range-slider',
                        min=df['year'].min(),
                        max=df['year'].max(),
                        step=1,
                        value=[df['year'].min(), df['year'].max()],
                        marks={str(year): {'label': str(year), 'style': {'color': '#273746'}} for year in df['year'].unique()},
                        allowCross=False
                    ),
                    style={'backgroundColor': '#EBF5FB', 'margin-bottom': '20px'}
                ),

                html.Div([
                    dcc.Graph(id='scatter-plot-container', style={'width': '80%', 'height': '80vh'}),  
                    dcc.Graph(id='right-side-chart', style={'width': '40%', 'height': '80vh'})  
                ], style={'display': 'flex', 'flex-direction': 'row'})  
            ],
            style={'backgroundColor': '#566573', 'color': '#000000'}  
        )
    else:
        return []


# Tab-3 Function-1
@app.callback(
    Output('scatter-plot-container', 'figure'),  # Change 'children' to 'figure'
    [Input('y-axis-radio', 'value'),
     Input('year-range-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_scatter_plot(y_axis, selected_year_range, selected_countries):

    df_new = df.groupby(['country', 'year']).agg(
        suicides_no=pd.NamedAgg('suicides_no', 'sum'),
        Population=pd.NamedAgg('population', 'sum'),
        Suicides_100k_pop=pd.NamedAgg('suicides/100k_pop', 'sum'),
        GDP_for_Year=pd.NamedAgg('_gdp_for_year__$_', 'mean'),
        GDP_for_capita=pd.NamedAgg('gdp_for_capita_$', 'mean'),
    ).reset_index()

    df_filtered = df_new[df_new['year'].between(selected_year_range[0], selected_year_range[1])]

    if selected_countries:
        df_filtered = df_filtered[df_filtered['country'].isin(selected_countries)]

    if y_axis == 'population':
        y_axis = 'Population'
    elif y_axis == 'suicides/100k_pop':
        y_axis = 'Suicides_100k_pop'
    elif y_axis == '_gdp_for_year__$_':
        y_axis = 'GDP_for_Year'
    elif y_axis == 'gdp_for_capita_$':
        y_axis = 'GDP_for_capita'

    fig = px.scatter(df_filtered, x=y_axis, y='suicides_no', color='country',
                     title=f'Scatter Plot: suicides_no vs {y_axis}', trendline="ols", custom_data=['country'])

    correlation = df_filtered[['suicides_no', y_axis]].corr().iloc[0, 1]
    fig.update_layout(title=f'Scatter Plot: suicides_no vs {y_axis} (Correlation: {correlation:.2f})')
    fig.update_layout(xaxis_title=y_axis)
    return fig

# Tab-3 Function-2
@app.callback(
    Output('right-side-chart', 'figure'),
    [Input('scatter-plot-container', 'clickData'),
     Input('y-axis-radio', 'value')]
)
def update_right_side_chart(clickData, y_axis):
    print(clickData)
    if clickData:
        try:
            country = clickData['points'][0]['customdata'][0]
            if country is None or country not in df['country'].unique():
                return {}  # Return empty figure if the selected country is not found
        except KeyError:
            return {}  # Return empty figure if custom data is not available

        df_country = df[df['country'] == country]

        y_column_name = y_axis

        # Aggregate data based on the selected y-axis
        if 'population' in y_axis or 'suicides/100k_pop' in y_axis:
            agg_func = 'sum'
        else:
            agg_func = 'mean'

        df_country2 = df_country.groupby('year').agg({y_column_name: agg_func}).reset_index()

        fig = px.line(df_country2, x='year', y=y_column_name, title=f'{country} - {y_axis}', color_discrete_sequence=['red'])
        
        fig.update_traces(mode='lines+markers')
        
        return fig
    else:
        return {}


# Tab 4 Layout
@app.callback(
    Output('tab-4', 'children'),
    [Input('tabs-with-classes', 'value')]
)
def render_content(tab):
    if tab == 'tab-4':
        return html.Div([
            dcc.Dropdown(
                id='sex-dropdown',
                options=[{'label': sex, 'value': sex} for sex in df['sex'].unique()],
                value=df['sex'].unique()[0],  # Set default value to the first sex option
                style={'margin-bottom': '20px','backgroundColor': '#EBF5FB', 'color': '#273746'}
            ),
            dcc.Dropdown(
                id='age-dropdown',
                options=[{'label': age, 'value': age} for age in df['age'].unique()],
                value=df['age'].unique()[0],  # Set default value to the first age option
                style={'margin-bottom': '20px','backgroundColor': '#EBF5FB', 'color': '#273746'}
            ),
            dcc.Graph(id='bar-chart'),
            dcc.Graph(id='line-chart2'),
        ],
        style={'backgroundColor': '#566573', 'color': '#000000'}
        )
    else:
        return []


# Tab-4 Function 1
@app.callback(
        Output('bar-chart', 'figure'),
        [Input('sex-dropdown', 'value'),
        Input('age-dropdown', 'value')]
    )
def update_bar_chart(selected_sex, selected_age):
        filtered_df2 = df[(df['sex'] == selected_sex) & (df['age'] == selected_age)]
        grouped_data = filtered_df2.groupby('country')['suicides_no'].sum().reset_index()
        return px.bar(grouped_data, x='country', y='suicides_no', title=f'Suicides by Country for {selected_sex}, {selected_age}')

#Tab-4 Funtion 2
@app.callback(
    Output('line-chart2', 'figure'),
    [Input('bar-chart', 'clickData')]
)
def update_line_chart(clickData):
    if clickData:
        selected_country = clickData['points'][0]['x']
        filtered_df = df[df['country'] == selected_country]
        suicide_age_data = filtered_df.groupby(['age', 'year']).agg({
            'suicides/100k_pop': 'mean'
        }).reset_index()

        fig = px.line(suicide_age_data, x='year', y='suicides/100k_pop', color='age',
                      title=f'Suicide Rates by Age Category in {selected_country}')

        fig.update_xaxes(title_text='Year', showgrid=True, gridcolor='lightgray', zeroline=False)
        fig.update_yaxes(title_text='Suicide Rate per 100k Population', showgrid=True, gridcolor='lightgray')
        fig.update_layout(title_font=dict(size=24), title_x=0.5, title_y=0.95)
        fig.update_layout(plot_bgcolor='white', paper_bgcolor='white')
        fig.update_layout(legend_title_text='Age Category')
        fig.update_layout(template="plotly")

        return fig

    else:
        return {}


# Tab-5 Layout
@app.callback(
    Output('tab-5', 'children'),
    [Input('tabs-with-classes', 'value')]
)
def render_content(tab):
    if tab == 'tab-5':
        return html.Div([
            dcc.Graph(id='world-map', config={'scrollZoom': False})
        ])
    else:
        return []


# Tab-5 Function
@app.callback(
        Output('world-map', 'figure'),
        Input('tabs-with-classes', 'value')
    )
def update_world_map(tab):
        if tab == 'tab-5':
            df_new = df.groupby('country').agg({'suicides/100k_pop':'mean'}).reset_index()
            fig = px.choropleth(df_new,
                    locations='country',
                    locationmode='country names',
                    color='suicides/100k_pop',
                    hover_name='country',
                    hover_data={'country': False, 'suicides/100k_pop': True},
                    color_continuous_scale='Sunset',
                    range_color=(df_new['suicides/100k_pop'].min(), df_new['suicides/100k_pop'].max()),  # Set the range of colors based on the data
                    title='Suicide Rates by Country',
                    labels={'suicides/100k_pop': 'Suicides per 100k Population'}
                    )

            fig.update_geos(
                projection_type='natural earth',
                showcoastlines=True,
                coastlinecolor="Gray",
                showland=True,
                landcolor="white",
                showocean=True,
                oceancolor="#0077BE",
                showlakes=True,
                lakecolor="LightBlue"
            )
            fig.update_layout(geo=dict(
                showframe=False,
                showcountries=True,
                countrycolor="Gray"
            ))
            return fig
        else:
            return {}



    
if __name__ == '__main__':
    app.run_server(debug=True)
