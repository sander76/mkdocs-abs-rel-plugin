import logging
import os
import re

from pathlib import Path

LOGGER = logging.getLogger(__name__)

md_link = re.compile(r"([\s(:]{1})(/[^\n\r)]*)")


def _check_link(link: str, source_file: Path, root_folder: Path):
    full_link_path = root_folder.joinpath(link[1:])
    link = os.path.relpath(full_link_path, source_file.parent)
    link = link.replace("\\", "/")

    return link


def _to_rel(source_file: Path, root_folder: Path):
    def re_write_link(matchobj):
        pre = matchobj.group(1)
        link = matchobj.group(2)

        link = _check_link(link, source_file, root_folder)

        return "{}{}".format(pre, link)

    return re_write_link


def _absolute_to_rel(content, source_file: Path, root_folder: Path):
    file_data = re.sub(md_link, _to_rel(source_file, root_folder), content)
    return file_data
