import pandas as pd
import os

def combine_csvs(directories, output_file, keyword=''):
    """
    Combine multiple CSV files from multiple directories into a single CSV file,
    including only files that contain 'truth' in the filename.

    Parameters
    ----------
    directories : list of str
        The directories containing the CSV files to combine.
    output_file : str
        The path of the output CSV file.
    keyword : str
        Keyword that must be in filename

    Returns
    -------
    None
    """
    csv_files = []
    for directory in directories:
        # List all CSV files in each directory that include 'truth' in the filename
        files = [file for file in os.listdir(directory) if file.endswith('.csv') and keyword in file]
        csv_files.extend([os.path.join(directory, file) for file in files])

    # Read and concatenate all CSV files
    df_list = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.drop_duplicates(inplace=True)

    # Save the combined CSV
    combined_df.to_csv(output_file, index=False)
    print(f'saved {output_file} with {len(combined_df):,} rows')

directories = ['energy/',
               'location/',
               'angle/',
               'particle/',
            ]
tds = [d+'truth_logs' for d in directories]
rds = [d+'reco_logs' for d in directories]

combine_csvs(tds,'truth_interactions.csv',keyword='truth')
combine_csvs(rds,'reco_interactions.csv',keyword='reco')


