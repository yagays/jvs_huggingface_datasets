from datasets import load_dataset

jvs_datasets = load_dataset(
    "csv", data_files="jvs_ver1/all_transcripts.txt", delimiter="\t", column_names=["file_id", "sentence", "path"]
)["train"]
