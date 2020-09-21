"""Script to download ESACCI-SOIL-MOISTURE."""
from dateutil import relativedelta
from datetime import datetime

from esmvaltool.cmorizers.data.downloaders.ftp import CCIDownloader


def download_dataset(config, dataset, start_date, end_date, overwrite):
    """
    Download dataset.

    Parameters
    ----------
    config : dict
        ESMValTool's user configuration
    dataset : str
        Name of the dataset
    start_date : datetime
        Start of the interval to download
    end_date : datetime
        End of the interval to download
    overwrite : bool
        Overwrite already downloaded files
    """
    if start_date is None:
        start_date = datetime(1979, 1, 1)
    if end_date is None:
        end_date = datetime(2016, 1, 1)

    loop_date = start_date

    downloader = CCIDownloader(
        config=config,
        dataset=dataset,
        overwrite=overwrite,
    )
    downloader.ftp_name = 'soil_moisture'
    downloader.connect()
    downloader.set_cwd('ancillary/v04.2/')
    downloader.download_folder('.')
    downloader.set_cwd('daily_files/COMBINED/v04.2/')
    while loop_date <= end_date:
        year = loop_date.year
        downloader.download_year(f'{year}')
        loop_date += relativedelta.relativedelta(years=1)