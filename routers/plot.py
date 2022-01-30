from fastapi import APIRouter
from starlette.responses import StreamingResponse
import numpy as np
import plots
from crud import plot

router = APIRouter(
    tags=["Plots"],
    prefix="/plot"
)


@router.get('/sin/{freq}')
def graph_sine(freq: int):
    plot.sector_wise()
    x_values = np.arange(-5, 5, 0.01)
    y_values = np.sin(x_values*freq)
    img = plots.build_graph(x_values, y_values)
    return StreamingResponse(img, media_type="image/png")


@router.get('/pie')
def graph_pie_chart():
    labels = ['C', 'C++', 'Java', 'Python', 'PHP']
    data = [23,17,35,29,12]
    img = plots.build_pie(data, labels)
    return StreamingResponse(img, media_type="image/png")


@router.get('/sector_count')
def sector_wise_count():
    labels, data = plot.sector_segment_wise_data('count', 'sector')
    img = plots.build_pie(data, labels)
    return StreamingResponse(img, media_type="image/png")


@router.get('/sector_amount')
def sector_wise_amount():
    labels, data = plot.sector_segment_wise_data('sum', 'sector')
    img = plots.build_pie(data, labels)
    return StreamingResponse(img, media_type="image/png")


@router.get('/segment_count')
def segment_wise_count():
    labels, data = plot.sector_segment_wise_data('count', 'segment')
    img = plots.build_pie(data, labels)
    return StreamingResponse(img, media_type="image/png")


@router.get('/segment_amount')
def segment_wise_amount():
    labels, data = plot.sector_segment_wise_data('sum', 'segment')
    img = plots.build_pie(data, labels)
    return StreamingResponse(img, media_type="image/png")


@router.get('/bar')
def graph_bar():
    labels = ['C', 'C++', 'Java', 'Python', 'PHP']
    data = [23,17,35,29,12]
    img = plots.build_bar(labels, data)
    return StreamingResponse(img, media_type="image/png")


@router.get('/multibar')
def graph_multi_bar():
    labels = ['TECH', 'IT', 'FINANCE', 'TELECOM', 'CRYPTO']

    data = {'LARGE': [12, 30, 1, 8, 22],
            'MID': [28, 6, 16, 5, 10],
            'SMALL': [29, 3, 24, 25, 17],
            "MICRO": [8, 13, 4, 95, 170]}

    img = plots.build_multi_bar(data=data, labels=labels, xlabel="Sectors", ylabel="Stocks")
    return StreamingResponse(img, media_type="image/png")


@router.get('/stacked')
def graph_stacked_bar():
    labels = ['TECH', 'IT', 'FINANCE', 'TELECOM', 'CRYPTO']
    legends = ['LARGE', 'MID', 'SMALL', 'MICRO']
    data = [
        [12, 30, 18, 8, 22],
        [28, 60, 16, 5, 10],
        [29, 13, 24, 25, 17],
        [8, 13, 4, 26, 43]
            ]

    img = plots.build_stacked_plot(data=data, labels=labels, legends=legends, xlabel="Stocks", ylabel="Sectors")
    return StreamingResponse(img, media_type="image/png")

