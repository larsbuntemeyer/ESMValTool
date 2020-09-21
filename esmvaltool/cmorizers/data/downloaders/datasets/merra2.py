"""Script to download MERRA2."""

from dateutil import relativedelta

from esmvaltool.cmorizers.data.downloaders.wget import NASADownloader


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
    loop_date = start_date

    downloader = NASADownloader(
        config=config,
        dataset=dataset,
        overwrite=overwrite,
    )

    while loop_date <= end_date:
        year = loop_date.year
        downloader.download_folder(
            "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/"
            f"M2TMNXLND.5.12.4/{year}/"
        )
        loop_date += relativedelta.relativedelta(years=1)