import junit_xml_output, os, argparse, re
from pathlib import Path, PosixPath

def getPathArg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target_dir",
        type=lambda p: Path(p).absolute(),
        default=Path(__file__).absolute().parent / "target",
        help="Path to the target directory"
    )
    parser.add_argument(
        "--file_pattern",
        type=str,
        default="*.xml",
        help="file pattern"
    )
    p = parser.parse_args()
    return p


if __name__ == "__main__":
    params = getPathArg()    
    for entry in params.target_dir.glob(params.file_pattern):
        test_cases = []
        fileName = entry.name
        with entry.open() as f:
            for line in f:                
                header = ""
                try:
                    regResult = re.search("(\([A-Z]+[0-9]+\))", line)
                    header = regResult.group(1)
                except:
                    header = line                    
                test_cases.append(junit_xml_output.TestCase(
                    header, line, "failure"))
        junit_xml = junit_xml_output.JunitXml(fileName, test_cases)  # suite
        output = params.target_dir / fileName
        with open(str(output) + ".xml", "w") as f:
            f.write(junit_xml.dump())
