import os
import click
import requests
import mimetypes
from PIL import Image
from StringIO import StringIO
from time import sleep


def check_output_path_exists(ctx, param, value):
    if not os.path.isdir(value):
        raise click.BadParameter(
            'Output path needs to exist and be a directory')

    return value


@click.command()
@click.option('--url',    required=True,    help='URL to download')
@click.option('--count',  default=50,       help='Number of times to repeat the download (default: 50).')
@click.option('--pause',  default=2,        help='Number of seconds to pause between downloads (default: 2).')
@click.option('--param',  default='count',  help='Query param to append to url on each retry (default: count).')
@click.option('--output', default='images', help='Where to output the resulting files (default: ./images).', callback=check_output_path_exists)
def repeatedly_download(url, count, pause, param, output):
    """Simple program to repeatedly download a file while appending a unique query string"""
    original_filename = os.path.basename(url)
    res = requests.get(url)
    img = Image.open(StringIO(res.content))
    img.save(os.path.join(output, original_filename))
    ext = mimetypes.guess_extension(res.headers['content-type'])

    click.echo("Downloaded file: %s" % os.path.join(output, original_filename))
    click.echo("Will now retry download %s times, every %s second(s)" %
               (count, pause))

    for i in range(1, count+1):
        sleep(pause)
        click.echo(
            "Retrying download with ?%s=%i appended to the url" % (param, i))
        res = requests.get(url, params=dict([(param, i)]))
        img = Image.open(StringIO(res.content))
        img.save(os.path.join(output, str(i) + ext))


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    repeatedly_download()
