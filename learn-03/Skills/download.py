"""Download the pinned lesson Skill files without installing or running them."""

from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen
from zipfile import ZipFile
import argparse
import shutil
import stat


ROOT = Path(__file__).resolve().parent
OPEN_ARTIFACT_URL = (
    "https://github.com/JimLiu/open-artifact/releases/download/"
    "v0.14.3/open-artifact-plugins.zip"
)
OPEN_ARTIFACT_SHA256 = "601a2bbd7b1e419476172a98c839ac7bca843f9070591c5747a6057a1b58df06"
DESIGN = Path("PPT美化/design-style-skill")
DESIGN_SOURCE = Path("完整制作/MiniMax-pptx-plugin/skills/design-style-skill")

# Repository, commit, and (upstream folder, local folder, lesson entry points).
PACKAGES = (
    ("mattpocock/skills", "abeeaf95660ba9e8b7c753eb38f441ca707a8823", (
        ("skills/productivity/grilling", "资料调研/grilling", ("SKILL.md",)),
        ("skills/engineering/research", "资料调研/research", ("SKILL.md",)),
    )),
    ("anthropics/knowledge-work-plugins", "2baf6d1eded3cd7aeff0b5c5918601a5799189b4", (
        ("product-management/skills/synthesize-research", "资料调研/synthesize-research", ("SKILL.md",)),
        ("marketing/skills/brand-review", "PPT话术/brand-review", ("SKILL.md",)),
    )),
    ("zarazhangrui/frontend-slides", "9906a34d640d2111f724544cbc50f7f130569ae1", (
        ("plugins/frontend-slides", "完整制作/frontend-slides", ("skills/frontend-slides/SKILL.md",)),
    )),
    ("MiniMax-AI/skills", "02853d885acb1abc157477ce00c4d98a8ed14a71", (
        ("plugins/pptx-plugin", "完整制作/MiniMax-pptx-plugin", (
            "README.md",
            "skills/ppt-orchestra-skill/SKILL.md",
            "skills/slide-making-skill/SKILL.md",
            "skills/ppt-editing-skill/SKILL.md",
            "skills/color-font-skill/SKILL.md",
            "skills/design-style-skill/SKILL.md",
        )),
    )),
    ("GordenSun/GordenSuperPPTSkills", "8c05583dab8334182b71738e8dfbbec5c56a1951", (
        ("", "完整制作/Gorden-Super-PPT", (
            "GordenSuperPPTSkill/SKILL.md",
            "GordenImagePPTGen/SKILL.md",
            "GordenImage2PPTX/SKILL.md",
        )),
    )),
    ("anthropics/skills", "e4bb5d960d87126ff3b3a8af1a104b7db67560ba", (
        ("skills/pptx", "完整制作/anthropic-pptx", ("SKILL.md",)),
        ("skills/theme-factory", "PPT美化/theme-factory", ("SKILL.md",)),
    )),
    ("Phantomlau3674/steven-superppt-skill", "0cafca577cf943349c82afaf47ee55cfaf978f65", (
        ("steven-superppt-skill", "完整制作/steven-superppt-skill", ("SKILL.md",)),
    )),
    ("JimLiu/baoyu-skills", "bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c", (
        ("skills/baoyu-slide-deck", "完整制作/baoyu-slide-deck", ("SKILL.md",)),
    )),
    ("zhaohui-yang/official-document-drafting", "6b4166a50b96733684b36da6336ea85a847cf3be", (
        ("", "PPT话术/official-document-drafting", (
            "SKILL.md",
            "prompts/doc-types/presentation-汇报材料/spec.md",
        )),
    )),
    ("github/awesome-copilot", "f10fdb8b2660ce85c98f220b2f1ca24653768a5c", (
        ("skills/gtm-board-and-investor-communication", "PPT话术/gtm-board-and-investor-communication", ("SKILL.md",)),
    )),
    ("coleam00/excalidraw-diagram-skill", "8646fcc9f74f38539c6cdb4c969723336a96ddcd", (
        ("", "看板绘制/excalidraw-diagram-skill", ("SKILL.md", "references/render_excalidraw.py")),
    )),
    ("JimLiu/open-artifact", "v0.14.3", (
        ("codex", "完整制作/Open-Artifact", (
            "skills/open-artifact/SKILL.md",
            "skills/open-artifact/vendor/artifact-types/slides/SKILL.md",
        )),
    )),
)


def missing_files(folder, entries):
    return [str(folder / entry) for entry in entries if not (folder / entry).is_file()]


def download_zip(repo, revision, target):
    release = repo == "JimLiu/open-artifact"
    url = OPEN_ARTIFACT_URL if release else f"https://codeload.github.com/{repo}/zip/{revision}"
    request = Request(url, headers={"User-Agent": "night-learn-03-skills"})
    with urlopen(request, timeout=60) as response, target.open("wb") as output:
        shutil.copyfileobj(response, output)
    if release:
        with target.open("rb") as data:
            digest = sha256()
            for block in iter(lambda: data.read(1024 * 1024), b""):
                digest.update(block)
        if digest.hexdigest() != OPEN_ARTIFACT_SHA256:
            raise ValueError("Open Artifact 下载包的 SHA-256 与发布记录不符。")


def extract_skill(package, upstream, target):
    root = PurePosixPath(package.infolist()[0].filename).parts[0]
    source = PurePosixPath(root) / upstream
    root_notices = {"LICENSE", "LICENSE.txt", "LICENSE.md", "NOTICE", "NOTICE.md"}
    for item in package.infolist():
        path = PurePosixPath(item.filename)
        if item.is_dir():
            continue
        if path.is_relative_to(source):
            relative = path.relative_to(source)
        elif path.parent == PurePosixPath(root) and path.name in root_notices:
            relative = PurePosixPath(f"UPSTREAM-{path.name}")
        else:
            continue
        if ".." in relative.parts or "\\" in str(relative):
            raise ValueError(f"无效的压缩包路径 {item.filename}")
        mode = item.external_attr >> 16
        if stat.S_ISLNK(mode):
            raise ValueError(f"压缩包中的链接需单独处理 {item.filename}")
        output = target.joinpath(*relative.parts)
        output.parent.mkdir(parents=True, exist_ok=True)
        with package.open(item) as source_file, output.open("wb") as target_file:
            shutil.copyfileobj(source_file, target_file)
        if mode & stat.S_IXUSR:
            output.chmod(0o755)


def install_group(package):
    repo, revision, folders = package
    pending = []
    for upstream, local, entries in folders:
        destination = ROOT / local
        if not destination.exists() and not destination.is_symlink():
            pending.append((upstream, destination, entries))
        elif missing_files(destination, entries):
            raise ValueError(f"目录已存在但缺少文件，请移开后重试：{destination}")
    if not pending:
        return

    with TemporaryDirectory(prefix=".download-", dir=ROOT) as scratch:
        work = Path(scratch)
        archive = work / "source.zip"
        download_zip(repo, revision, archive)
        with ZipFile(archive) as zipped:
            for index, (upstream, destination, entries) in enumerate(pending):
                staging = work / str(index)
                extract_skill(zipped, upstream, staging)
                if missing_files(staging, entries):
                    raise ValueError(f"{repo} 的归档缺少入口：{destination.name}")
                destination.parent.mkdir(parents=True, exist_ok=True)
                staging.rename(destination)
                print(f"已下载 {destination.relative_to(ROOT)}", flush=True)


def check_library():
    missing = [
        path
        for _, _, folders in PACKAGES
        for _, local, entries in folders
        for path in missing_files(ROOT / local, entries)
    ]
    missing.extend(missing_files(ROOT / DESIGN, ("SKILL.md",)))
    if missing:
        raise SystemExit("缺少文件：\n" + "\n".join(missing))
    count = sum(len(folders) for _, _, folders in PACKAGES)
    print(f"已核对 {count} 个上游包或 Skill 目录，以及 PPT 美化里的 MiniMax 入口。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="只检查本地入口，不联网")
    args = parser.parse_args()
    if not args.check:
        with ThreadPoolExecutor(max_workers=4) as executor:
            list(executor.map(install_group, PACKAGES))
        shortcut = ROOT / DESIGN
        shortcut.parent.mkdir(parents=True, exist_ok=True)
        if not shortcut.exists() and not shortcut.is_symlink():
            shortcut.symlink_to(Path("..") / DESIGN_SOURCE, target_is_directory=True)
    check_library()


if __name__ == "__main__":
    main()
