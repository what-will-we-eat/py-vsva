#!/usr/bin/env python3
"""
This module uses a config file. Here are functions related to that.
"""
import json
import os



class Config:
    """
    A class object for config options. Currently contains paths to riksdagen corpora.
    """
    def __init__(self,
                 metadata_path=None,
                 records_path=None,
                 motions_path=None,
                 interpellations_path=None,
                 common_path_prefix=None):
        print("init")
        self.metadata_path = metadata_path
        self.records_path = records_path
        self.motions_path = motions_path
        self.interpellations_path = interpellations_path
        self.common_path_prefix = "./"

    def write(self,  path_ = f"{os.path.dirname(__file__)}/_cfg.json"):
        """
        Write config object to json.

        Args:
            path_ (str): where to write the config.
        """
        with open(path_, "w+") as outf:
            json.dump(dict(self.__dict__), outf, indent=2, ensure_ascii=False)

    def set_key(self, k, v):
        """
        Change a class instance attrib value
        """
        setattr(self, k, v)


def load_config(path_ = f"{os.path.dirname(__file__)}/_cfg.json"):
    """
    load a config object to json. If no valid json is found, a config object with default values is initiated.

    Args:
        path_ (str): where to write the config.
    """
    c = Config()
    try:
        assert os.path.exists(path_)
        with open(path_, 'r') as inf:
            J = json.load(inf)
            for k, v in J.items():
                setattr(c, k, v)
    except:
        setattr(c, "metadata_path", "riksdagen-persons/data")
        setattr(c, "records_path", "riksdagen-records/data")
        setattr(c, "motions_path", "riksdagen-motions/data")
        setattr(c, "interpellations_path", "riksdagen-interpellations/data")
        setattr(c, "common_path_prefix", "./")
    return c








