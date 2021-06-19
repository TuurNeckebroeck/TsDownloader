import argparse
import logging
import requests
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TsDownloader:
    @staticmethod
    def download(url, id_string="$", output_file="out.msb"):
        def download_ts(url, tmp_filename):
            logging.info("Start downloading")
            i = 1
            while True:
                param_url = url.replace(id_string, str(i))
                resp = requests.get(param_url)
                logger.debug(f"ts id {i}, HTTP response {resp.status_code}")
                if resp.status_code != 200:
                    break
                logger.debug(f"Downloading ts file {i}")
                with open(tmp_filename.format(str(i)), "wb") as f:
                    f.write(resp.content)
                    f.close()
                i += 1
            return i - 1

        def stitch(max_idx, tmp_filename):
            logging.info("Start stitching")
            with open(output_file, "wb") as f:
                for i in range(1, max_idx + 1):
                    ts_filename = tmp_filename.format(str(i))
                    with open(ts_filename, "rb") as f_ts:
                        f.write(f_ts.read())
                    logger.debug(f"Removing ts file {i}")
                    os.remove(ts_filename)

        if not id_string in url:
            raise Exception(f"No id string '{id_string}' in url {url}")
        
        tmp_file = "out-{}.ts"
        max_idx = download_ts(url, tmp_filename=tmp_file)
        if max_idx == 0:
            raise Exception("No ts files were downloaded")
        stitch(max_idx, tmp_filename=tmp_file)
        logging.info("Finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", required=True, help="url")
    parser.add_argument("-s", default="{}", help="string for id of ts part")
    parser.add_argument("-o", default="out.mp4", help="output file name")
    args = parser.parse_args()

    TsDownloader.download(args.u, id_string=args.s, output_file=args.o)
