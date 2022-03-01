from pathlib import Path

import pandas as pd

base_path = Path("jvs_ver1/")
subdir_name = "wav24kHz16bit"

all_transcripts = []
for transcript in base_path.glob("**/transcripts_utf8.txt"):
    with open(transcript) as f:
        for line in f:
            file_id, sentence = line.strip().split(":")
            path = (transcript.parent / subdir_name / (file_id + ".wav")).absolute()
            all_transcripts.append((file_id, sentence, str(path)))

df = pd.DataFrame(all_transcripts, columns=["file_id", "sentence", "path"])
df.to_csv(str(base_path / "all_transcripts.txt"), sep="\t", header=None, index=None)
