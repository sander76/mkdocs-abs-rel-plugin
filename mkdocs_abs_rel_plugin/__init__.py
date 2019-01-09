import logging
import os
import re

from pathlib import Path

LOGGER = logging.getLogger(__name__)

# md_link = re.compile(r"([\s(:]{1})(/[^\n\r)]*)")
md_link = re.compile(r"(]\()(/[^\n\r)]*)(\))|(]:\s)(/[^\n\r)]*)")


def _check_link(link: str, source_file: Path, root_folder: Path):
    full_link_path = root_folder.joinpath(link[1:])
    link = os.path.relpath(full_link_path, source_file.parent)
    link = link.replace("\\", "/")

    return link


def _to_rel(source_file: Path, root_folder: Path):
    def re_write_link(matchobj):
        group1 = matchobj.group(1)  # front stuff
        group2 = matchobj.group(2)  # the actual link
        group3 = matchobj.group(3)  # closing tag

        if group1 and group2 and group3:

            link = _check_link(group2, source_file, root_folder)

            return "{}{}{}".format(group1, link, group3)

        group4 = matchobj.group(4)  # front stuff
        group5 = matchobj.group(5)  # the actual link
        if group4 and group5:
            link = _check_link(group5, source_file, root_folder)

            return "{}{}".format(group4, link)

    return re_write_link


def _absolute_to_rel(content, source_file: Path, root_folder: Path):
    file_data = re.sub(md_link, _to_rel(source_file, root_folder), content)
    return file_data
