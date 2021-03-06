import time
from pathlib import Path
from typing import Union

import cv2
import numpy as np


class File_Manager:
    """
    The file manager...
    - Generates a unique, time-stamped folder
    which extractors may access via file_manager.new_folderpath.
    - Reads image sequences for offline analysis.
    - Saves images from camera streams.
    """

    def __init__(self, output_root: Union[Path, str]) -> None:
        self.output_root = output_root
        self.input_folderpath = ""

        self.output_root.mkdir(exist_ok=True, parents=True)

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.new_folderpath = self.output_root / f"trial_{timestamp}"
        self.new_folderpath.mkdir(exist_ok=True)
        print(f"Outputting data to {self.new_folderpath}")  # TODO convert to logging call

    def save_image(self, image: np.ndarray, frame: int) -> None:
        """
        Saves video sequence to new folderpath.
        """
        img_pth = Path(self.new_folderpath, f"frame_{frame}.jpg")
        cv2.imwrite(str(img_pth), image)

    def read_image(self, frame: int) -> np.ndarray:
        """
        Reads video sequence from the input folderpath.
        Command-line argument -v [dir] sets this vid_path.
        """
        img_pth = Path(self.input_folderpath, f"pic{frame}.jpg")
        return np.array(cv2.imread(str(img_pth)))
