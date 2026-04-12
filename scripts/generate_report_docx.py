from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
import sys
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "docs" / "Parul_University_Internship_Report.md"
DEFAULT_OUTPUT_PATH = ROOT / "docs" / "Parul_University_Internship_Report.docx"


@dataclass
class TableBlock:
    rows: list[list[str]]


@dataclass
class ParagraphBlock:
    text: str
    style: str = "Normal"
    page_break_before: bool = False


@dataclass
class CodeBlock:
    lines: list[str]


def strip_md(text: str) -> str:
    text = text.replace("\\", "")
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.replace("`", "")
    return text.strip()


def needs_page_break(line: str) -> bool:
    targets = {
        "# CERTIFICATE",
        "# INTERNSHIP CERTIFICATE",
        "# ACKNOWLEDGEMENT",
        "# ABSTRACT",
        "# TABLE OF CONTENTS",
        "# LIST OF ABBREVIATIONS",
        "# LIST OF FIGURES",
        "# CHAPTER 1: INTRODUCTION",
        "# CHAPTER 2: AIM AND OBJECTIVES",
        "# CHAPTER 3: LITERATURE REVIEW",
        "# CHAPTER 4: METHODOLOGY",
        "# CHAPTER 5: RESULTS AND DISCUSSION",
        "# CHAPTER 6: CONCLUSION",
        "# REFERENCES",
        "# ANNEXURES",
    }
    return line.strip() in targets


def parse_markdown(text: str) -> list[object]:
    lines = text.splitlines()
    blocks: list[object] = []
    i = 0
    first_heading = True

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i].rstrip("\n"))
                i += 1
            blocks.append(CodeBlock(code_lines))
            i += 1
            continue

        if stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            rows = []
            for idx, table_line in enumerate(table_lines):
                parts = [strip_md(part.strip()) for part in table_line.strip("|").split("|")]
                if idx == 1 and all(set(part) <= {"-", ":"} for part in parts):
                    continue
                rows.append(parts)
            if rows:
                blocks.append(TableBlock(rows))
            continue

        if stripped == "---":
            i += 1
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            heading_text = strip_md(stripped[level:].strip())
            style = {1: "Heading1", 2: "Heading2", 3: "Heading3", 4: "Heading4"}.get(level, "Heading4")
            page_break_before = False
            raw_heading = stripped
            if needs_page_break(raw_heading) and not first_heading:
                page_break_before = True
            first_heading = False
            blocks.append(ParagraphBlock(heading_text, style=style, page_break_before=page_break_before))
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            blocks.append(ParagraphBlock(strip_md(stripped), style="ListBullet"))
            i += 1
            continue

        if re.match(r"^\d+\.\s+", stripped):
            blocks.append(ParagraphBlock(strip_md(stripped), style="ListNumber"))
            i += 1
            continue

        para_lines = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt:
                break
            if nxt.startswith(("#", "|", "```")) or nxt == "---":
                break
            if re.match(r"^[-*]\s+", nxt) or re.match(r"^\d+\.\s+", nxt):
                break
            para_lines.append(nxt)
            i += 1
        blocks.append(ParagraphBlock(strip_md(" ".join(para_lines))))

    return blocks


def inline_runs(text: str, default_style: str = "Normal") -> str:
    style_map = {
        "Normal": "",
        "Code": '<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="20"/></w:rPr>',
    }
    base = style_map.get(default_style, "")
    if not text:
        return f"<w:r>{base}<w:t xml:space=\"preserve\"></w:t></w:r>"
    return f"<w:r>{base}<w:t xml:space=\"preserve\">{escape(text)}</w:t></w:r>"


def paragraph_xml(block: ParagraphBlock) -> str:
    p_pr = [f"<w:pStyle w:val=\"{block.style}\"/>"]
    if block.style == "Normal":
        p_pr.append("<w:jc w:val=\"both\"/>")
    if block.style in {"ListBullet", "ListNumber"}:
        p_pr.append("<w:ind w:left=\"720\" w:hanging=\"360\"/>")
    p_pr_xml = "".join(p_pr)
    prefix = ""
    if block.page_break_before:
        prefix = "<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>"
    return f"{prefix}<w:p><w:pPr>{p_pr_xml}</w:pPr>{inline_runs(block.text)}</w:p>"


def code_block_xml(block: CodeBlock) -> str:
    parts = []
    for line in block.lines or [""]:
        parts.append(
            "<w:p><w:pPr><w:pStyle w:val=\"Code\"/></w:pPr>"
            f"{inline_runs(line, default_style='Code')}</w:p>"
        )
    return "".join(parts)


def table_xml(block: TableBlock) -> str:
    max_cols = max((len(row) for row in block.rows), default=1)
    page_width = 9360
    col_width = max(1200, page_width // max_cols)
    grid_cols = "".join(f"<w:gridCol w:w=\"{col_width}\"/>" for _ in range(max_cols))
    rows_xml = []
    for row_index, row in enumerate(block.rows):
        cell_xml = []
        padded_row = row + [""] * (max_cols - len(row))
        for cell in padded_row:
            p_style = "TableHeader" if row_index == 0 else "TableText"
            cell_xml.append(
                "<w:tc>"
                f"<w:tcPr><w:tcW w:w=\"{col_width}\" w:type=\"dxa\"/></w:tcPr>"
                f"<w:p><w:pPr><w:pStyle w:val=\"{p_style}\"/></w:pPr>{inline_runs(cell)}</w:p>"
                "</w:tc>"
            )
        rows_xml.append("<w:tr>" + "".join(cell_xml) + "</w:tr>")
    return (
        "<w:tbl>"
        "<w:tblPr>"
        "<w:tblStyle w:val=\"TableGrid\"/>"
        f"<w:tblW w:w=\"{page_width}\" w:type=\"dxa\"/>"
        "<w:tblLayout w:type=\"fixed\"/>"
        "<w:tblLook w:val=\"04A0\" w:firstRow=\"1\" w:lastRow=\"0\" w:firstColumn=\"1\" w:lastColumn=\"0\" w:noHBand=\"0\" w:noVBand=\"1\"/>"
        "<w:tblBorders>"
        "<w:top w:val=\"single\" w:sz=\"8\" w:space=\"0\" w:color=\"000000\"/>"
        "<w:left w:val=\"single\" w:sz=\"8\" w:space=\"0\" w:color=\"000000\"/>"
        "<w:bottom w:val=\"single\" w:sz=\"8\" w:space=\"0\" w:color=\"000000\"/>"
        "<w:right w:val=\"single\" w:sz=\"8\" w:space=\"0\" w:color=\"000000\"/>"
        "<w:insideH w:val=\"single\" w:sz=\"6\" w:space=\"0\" w:color=\"808080\"/>"
        "<w:insideV w:val=\"single\" w:sz=\"6\" w:space=\"0\" w:color=\"808080\"/>"
        "</w:tblBorders>"
        "</w:tblPr>"
        f"<w:tblGrid>{grid_cols}</w:tblGrid>"
        + "".join(rows_xml) +
        "</w:tbl>"
    )


def document_xml(blocks: list[object]) -> str:
    body_parts = []
    for block in blocks:
        if isinstance(block, ParagraphBlock):
            body_parts.append(paragraph_xml(block))
        elif isinstance(block, TableBlock):
            body_parts.append(table_xml(block))
        elif isinstance(block, CodeBlock):
            body_parts.append(code_block_xml(block))
    sect_pr = (
        "<w:sectPr>"
        "<w:pgSz w:w=\"12240\" w:h=\"15840\"/>"
        "<w:pgMar w:top=\"1440\" w:right=\"1080\" w:bottom=\"1440\" w:left=\"1440\" w:header=\"720\" w:footer=\"720\" w:gutter=\"0\"/>"
        "<w:cols w:space=\"720\"/>"
        "<w:docGrid w:linePitch=\"360\"/>"
        "</w:sectPr>"
    )
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:wpc=\"http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas\" "
        "xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" "
        "xmlns:o=\"urn:schemas-microsoft-com:office:office\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
        "xmlns:v=\"urn:schemas-microsoft-com:vml\" "
        "xmlns:wp14=\"http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing\" "
        "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "xmlns:w10=\"urn:schemas-microsoft-com:office:word\" "
        "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:w14=\"http://schemas.microsoft.com/office/word/2010/wordml\" "
        "xmlns:wpg=\"http://schemas.microsoft.com/office/word/2010/wordprocessingGroup\" "
        "xmlns:wpi=\"http://schemas.microsoft.com/office/word/2010/wordprocessingInk\" "
        "xmlns:wne=\"http://schemas.microsoft.com/office/2006/wordml\" "
        "xmlns:wps=\"http://schemas.microsoft.com/office/word/2010/wordprocessingShape\" "
        "mc:Ignorable=\"w14 wp14\">"
        "<w:body>"
        + "".join(body_parts)
        + sect_pr +
        "</w:body></w:document>"
    )


def styles_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="24"/>
        <w:szCs w:val="24"/>
        <w:lang w:val="en-US"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:line="360" w:lineRule="auto" w:after="120"/>
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
      <w:sz w:val="24"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="32"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="200" w:after="100"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="28"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="160" w:after="80"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="26"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading4">
    <w:name w:val="heading 4"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListBullet">
    <w:name w:val="List Bullet"/>
    <w:basedOn w:val="Normal"/>
    <w:rPr><w:sz w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListNumber">
    <w:name w:val="List Number"/>
    <w:basedOn w:val="Normal"/>
    <w:rPr><w:sz w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Code">
    <w:name w:val="Code"/>
    <w:basedOn w:val="Normal"/>
    <w:rPr>
      <w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>
      <w:sz w:val="20"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="TableHeader">
    <w:name w:val="Table Header"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="22"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="TableText">
    <w:name w:val="Table Text"/>
    <w:basedOn w:val="Normal"/>
    <w:rPr><w:sz w:val="22"/></w:rPr>
  </w:style>
</w:styles>
"""


def content_types_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


def package_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


def document_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""


def core_xml() -> str:
    created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Parul University Internship Report</dc:title>
  <dc:subject>HR Analytics Dashboard with Predictive Attrition Analysis</dc:subject>
  <dc:creator>OpenAI Codex</dc:creator>
  <cp:keywords>internship report, hr analytics, parul university, project report</cp:keywords>
  <dc:description>Detailed internship report prepared in Word format.</dc:description>
  <cp:lastModifiedBy>OpenAI Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{created}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{created}</dcterms:modified>
</cp:coreProperties>
"""


def app_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
  <DocSecurity>0</DocSecurity>
  <ScaleCrop>false</ScaleCrop>
  <HeadingPairs>
    <vt:vector size="2" baseType="variant">
      <vt:variant><vt:lpstr>Title</vt:lpstr></vt:variant>
      <vt:variant><vt:i4>1</vt:i4></vt:variant>
    </vt:vector>
  </HeadingPairs>
  <TitlesOfParts>
    <vt:vector size="1" baseType="lpstr">
      <vt:lpstr>Parul University Internship Report</vt:lpstr>
    </vt:vector>
  </TitlesOfParts>
  <Company>Parul University</Company>
  <LinksUpToDate>false</LinksUpToDate>
  <SharedDoc>false</SharedDoc>
  <HyperlinksChanged>false</HyperlinksChanged>
  <AppVersion>16.0000</AppVersion>
</Properties>
"""


def build_docx() -> None:
    markdown = SOURCE_PATH.read_text(encoding="utf-8")
    blocks = parse_markdown(markdown)
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types_xml())
        docx.writestr("_rels/.rels", package_rels_xml())
        docx.writestr("docProps/core.xml", core_xml())
        docx.writestr("docProps/app.xml", app_xml())
        docx.writestr("word/document.xml", document_xml(blocks))
        docx.writestr("word/styles.xml", styles_xml())
        docx.writestr("word/_rels/document.xml.rels", document_rels_xml())
    print(f"Generated {output_path}")


if __name__ == "__main__":
    build_docx()
