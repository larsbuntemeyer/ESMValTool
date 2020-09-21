"""Script to download HadCRUT4 from its webpage."""
import logging
import os

from esmvaltool.cmorizers.data.downloaders.wget import WGetDownloader

logger = logging.getLogger(__name__)


def download_dataset(config, dataset, _, __, overwrite):
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
    downloader = WGetDownloader(
        config=config,
        dataset=dataset,
        overwrite=overwrite,
    )
    downloader.tier = 2
    os.makedirs(downloader.local_folder, exist_ok=True)
    downloader.download_file(
        "https://crudata.uea.ac.uk/cru/data/temperature/"
        "HadCRUT.4.6.0.0.median.nc",
        wget_options=[]

    )
    downloader.download_file(
        "https://crudata.uea.ac.uk/cru/data/temperature/absolute.nc",
        wget_options=[]

    )