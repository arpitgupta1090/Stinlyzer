from fastapi import APIRouter
from starlette.responses import StreamingResponse
import plots
from crud import plot
import enums

router = APIRouter(
    tags=["Plots"],
    prefix="/plot"
)


@router.get('/pie/{flag}/{data}')
def sector_segment_wise_count_amount(flag: enums.Flag, data: enums.Data):
    labels, data = plot.sector_segment_wise_data(flag, data)
    img = plots.build_pie(data, labels)
    return StreamingResponse(img, media_type="image/png")


@router.get('/sector_segment/{flag}')
def sector_and_segment(flag: enums.Flag):
    labels, data = plot.sector_and_segment_wise_data(flag)
    img = plots.build_multi_bar(data=data, labels=labels, xlabel="Sectors", ylabel=flag.value)
    return StreamingResponse(img, media_type="image/png")


@router.get('/stacked/{flag}')
def sector_and_segment_stacked_amount(flag: enums.Flag):
    labels, legends, data = plot.sector_and_segment_wise_stacked_data(flag)
    img = plots.build_stacked_plot(data=data, labels=labels, legends=legends, xlabel="Sectors", ylabel=flag.value)
    return StreamingResponse(img, media_type="image/png")


