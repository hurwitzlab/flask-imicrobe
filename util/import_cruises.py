import argparse
import glob
import os.path
import sys

import pandas as pd

import app.models


def get_args():
    arg_parser = argparse.ArgumentParser()

    return arg_parser.parse_args()


def main():
    spreadsheet_file_list = []
    spreadsheet_file_list.extend(glob.glob('iplant/home/scope/data/caron/**/*.xls'))
    spreadsheet_file_list.extend(glob.glob('iplant/home/scope/data/caron/**/**/*.xls'))
    print('\n'.join(spreadsheet_file_list))

    for spreadsheet_fp in spreadsheet_file_list:
        basename, ext = os.path.splitext(os.path.split(spreadsheet_fp)[1])
        parse_function_name = 'parse_{}_{}'.format(basename, ext[1:])
        print(parse_function_name)
        parse_function = sys.modules[__name__].__dict__[parse_function_name]
        parse_function(spreadsheet_fp)


def parse_Caron_HL2A_18Sdiel_seq_attrib_v2_xls(spreadsheet_fp):
    """
    File Caron_HL2A_VertProf_seq_attrib_v2_xls has three sheets:
        'README'
        'core attributes + data'
        'additional attributes'

    Sheet 'README' has two separate blocks of data.

    :param spreadsheet_fp:
    :return:
    """
    readme_block_1_df = pd.read_excel(
        spreadsheet_fp,
        sheetname='README',
        index_col='Cast #',
        skip_footer=27,
        parse_cols=range(9, 22)
    )
    print('README block 1')
    print(readme_block_1_df)

    readme_block_2_df = pd.read_excel(
        spreadsheet_fp,
        sheetname='README',
        header=22,
        index_col='Cast #',
        skip_rows=range(23),
        skip_footer=5,
        parse_cols=range(9, 17)
    )
    print('README block 2')
    print(readme_block_2_df)

    readme_df = pd.merge(left=readme_block_1_df, left_index=True, right=readme_block_2_df, right_index=True)
    print('all README data')
    print(readme_df)

    core_attr_plus_data_df = pd.read_excel(
        spreadsheet_fp,
        sheetname='core attributes + data',
        skiprows=(0,2)
    )
    print('core attributes + data')
    print(core_attr_plus_data_df)



def parse_Caron_HL2A_VertProf_seq_attrib_v2_xls(spreadsheet_fp):
    pass


def parse_Caron_HL3_VertProf_seq_attrib_v2_xls(spreadsheet_fp):
    pass


def parse_Caron_HOTquarterly_18Sv4_seq_assoc_data_v2_xls(spreadsheet_fp):
    pass


def parse_Caron_HOT273_18Ssizefrac_seq_assoc_data_v2_xls(spreadsheet_fp):
    pass


if __name__ == '__main__':
    main()