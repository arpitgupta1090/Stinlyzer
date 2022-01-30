from fastapi import APIRouter
from starlette.responses import StreamingResponse
import plots
from crud import plot

router = APIRouter(
    tags=["Plots"],
    prefix="/plot"
)


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


@router.get('/sector_segment_amount')
def sector_and_segment_amount():
    labels, data = plot.sector_and_segment_wise_data('amount')
    img = plots.build_multi_bar(data=data, labels=labels, xlabel="Sectors", ylabel="Amount")
    return StreamingResponse(img, media_type="image/png")


@router.get('/sector_segment_count')
def sector_and_segment_count():
    labels, data = plot.sector_and_segment_wise_data('count')
    img = plots.build_multi_bar(data=data, labels=labels, xlabel="Sectors", ylabel="Count")
    return StreamingResponse(img, media_type="image/png")


@router.get('/amount_stacked')
def sector_and_segment_stacked_amount():
    labels, legends, data = plot.sector_and_segment_wise_stacked_data('amount')
    img = plots.build_stacked_plot(data=data, labels=labels, legends=legends, xlabel="Sectors", ylabel="Amount")
    return StreamingResponse(img, media_type="image/png")


@router.get('/count_stacked')
def sector_and_segment_stacked_count():
    labels, legends, data = plot.sector_and_segment_wise_stacked_data('count')
    img = plots.build_stacked_plot(data=data, labels=labels, legends=legends, xlabel="Sectors", ylabel="Count")
    return StreamingResponse(img, media_type="image/png")
