# NVKB — NGINX Vulnerability Knowledge Base

NVKB là thư viện tri thức tiếng Việt về NGINX và các lỗ hổng liên quan, chạy trên máy cá nhân. Sản phẩm gồm CLI Python để thu thập, kiểm tra, tra cứu dữ liệu và vault Markdown để đọc bằng Obsidian. Mỗi nhận định có thể truy về bằng chứng, vị trí trích dẫn, bản chụp nguồn và lịch sử thay đổi.

Bản sản phẩm này dùng phiên bản **1.3.0**, kèm dữ liệu hiện có và snapshot nguồn để kiểm tra offline. Phạm vi mặc định trong `config/scope.yaml` là NGINX OSS, năm công bố 2024–2026, mốc dữ liệu **2026-11-25**. Năm trong mã CVE không đồng nghĩa với năm công bố. Các sản phẩm như NGINX Plus, NGINX Ingress Controller và module bên thứ ba được phân biệt với NGINX OSS.

## Kiến trúc

```text
Tài liệu NGINX / CVE / nguồn bản phân phối / nguồn tham khảo
                              |
                   collectors + HTTP cache
                              |
                data/raw: snapshot + content hash
                              |
                 normalization + evidence
                              |
       data/canonical: thực thể, claim, evidence, relationship
                 |                          |
        data/history, conflicts      ontology/nvkb.yaml
                 |                          |
                 +------ validation --------+
                              |
                  +-----------+-----------+
                  |                       |
          SQLite + FTS5             Jinja2 + Markdown
          database/nvkb.sqlite     vault/ → Obsidian
                  |                       |
                  +------ CLI / export ---+
```

**Canonical JSON là dữ liệu gốc của ứng dụng.** SQLite và các note được sinh trong vault là mô hình phục vụ đọc, có thể tái dựng. LinkML trong `ontology/nvkb.yaml` là schema được biên soạn; JSON Schema được sinh từ schema đó.

| Thành phần | Trách nhiệm |
| --- | --- |
| `src/nvkb/cli.py`, `config.py` | Lệnh người dùng, chọn workspace và nạp cấu hình YAML. |
| `collectors/` | Đọc nguồn công khai, giới hạn tần suất, retry, cache HTTP và giữ snapshot. |
| `normalization/` | Chuẩn hóa CVE, sản phẩm, module và nội dung tri thức tiếng Việt. |
| `evidence/` | Liên kết bằng chứng, kiểm tra quan hệ, trạng thái và vòng đời của nhận định. |
| `storage/` | Lưu JSON theo ID ổn định, ghi atomic, theo dõi lịch sử và xung đột. |
| `validation/` | Kiểm tra schema, tham chiếu, hash snapshot, ngày, phiên bản và ràng buộc ngữ nghĩa. |
| `versioning/` | So sánh phiên bản upstream, gói Debian/Ubuntu và RPM theo từng hệ sinh thái. |
| `database/` | Dựng SQLite, khóa ngoại, các view và chỉ mục tìm kiếm FTS5. |
| `rendering/`, `templates/` | Sinh vault Obsidian, liên kết note và bảo vệ note đã sửa tay. |
| `reporting/` | Xuất CSV/JSONL và sinh báo cáo cục bộ khi người dùng yêu cầu. |

Ứng dụng không cần máy chủ, graph database hoặc dịch vụ AI để đọc và tái dựng dữ liệu đã có. Chế độ cập nhật nguồn cần Internet. Trạng thái đạt schema hoặc nhãn ingestion `VERIFIED` không tự chứng minh mọi nhận định đúng; cần đọc trạng thái review, source support và bằng chứng đi kèm.

## Cấu trúc bản sản phẩm

```text
NVKB/
├── src/nvkb/                 Mã nguồn thư viện và CLI
├── config/                   Thiết lập, phạm vi và nguồn thu thập
├── ontology/
│   ├── nvkb.yaml             Schema LinkML
│   └── generated/            JSON Schema
├── data/
│   ├── canonical/            Dữ liệu tri thức chuẩn hóa
│   ├── raw/                  Snapshot nguồn và cache phục vụ offline
│   ├── history/              Lịch sử thay đổi dữ liệu
│   ├── conflicts/            Xung đột dữ liệu cần đối chiếu
│   ├── curation/             Dữ liệu biên soạn tri thức
│   └── review_tasks/         Trạng thái công việc rà soát tri thức
├── templates/                Template Markdown
├── vault/                    Vault Obsidian đã sinh
├── examples/
│   └── inventory.example.json
├── pyproject.toml
├── uv.lock                   Khóa phiên bản dependency
└── README.md
```

Repo chỉ chứa bản sản phẩm. Lab, báo cáo bàn giao, kế hoạch, script phát triển, tài liệu phát triển, môi trường Python, log và cấu hình Obsidian cá nhân không được đưa vào Git. `database/`, `logs/`, `reports/` và dữ liệu export có thể được tạo cục bộ khi chạy; `.gitignore` giữ chúng ngoài repo. Lịch sử trong `data/history/` là lịch sử dữ liệu của sản phẩm, tách biệt với lịch sử commit phát triển.

## Cài đặt

Yêu cầu: Git, Python **3.11–3.14**, SQLite có FTS5 và `uv` có trong `PATH`. Python 3.13 phù hợp với môi trường đã dùng của dự án. Sao chép URL clone của repo private từ GitHub; tài khoản dùng để clone phải có quyền truy cập.

```bash
git clone https://github.com/quanghoang205/NVKB.git NVKB
cd NVKB
uv sync --frozen --no-dev
uv run --frozen --no-dev nvkb doctor
uv run --frozen --no-dev nvkb init
```

`uv sync` cần Internet ở lần đầu nếu chưa có dependency trong cache. `--no-dev` chỉ cài dependency chạy sản phẩm. Các nguồn công khai mặc định không cần API key. Không cần copy `.env.example` để chạy: CLI tự tìm workspace từ thư mục hiện tại; file `.env` không được tự động nạp.

Nếu gọi từ nơi khác, chọn workspace rõ ràng:

```bash
/path/to/NVKB/.venv/bin/nvkb --root /path/to/NVKB doctor
# Hoặc: export NVKB_ROOT=/path/to/NVKB
```

## Khởi chạy và đọc bằng Obsidian

Kiểm tra dữ liệu kèm theo rồi dựng SQLite và vault hoàn toàn từ dữ liệu cục bộ:

```bash
uv run --frozen --no-dev nvkb validate
uv run --frozen --no-dev nvkb build
```

Kết quả `build` bao gồm kiểm tra wiki-link của vault. Trong Obsidian, chọn **Open folder as vault** và mở thư mục `vault/`. Bắt đầu từ `vault/00-Home/NVKB-Home.md`; các mục CVE, module, giao thức, điểm yếu, cách giảm thiểu và bằng chứng được liên kết qua wiki-link. Obsidian được cài riêng, không đi kèm repo.

Ghi chú tự viết đặt trong `vault/13-Research/` hoặc `vault/15-Lectures/`; mẫu có trong `vault/99-Templates/`. Không sửa note generated nếu muốn tiếp tục tự động tái dựng. Builder so sánh với `vault/.nvkb-generated.json` và từ chối ghi đè note generated đã bị sửa tay hoặc tệp xung đột không thuộc builder. Khi gặp trường hợp đó, sao lưu nội dung tự viết sang hai thư mục authored trước khi xử lý xung đột.

## Tra cứu và xuất dữ liệu

```bash
# Cú pháp toàn bộ CLI
uv run --frozen --no-dev nvkb --help

# Tìm trên SQLite đã build
uv run --frozen --no-dev nvkb search 'HTTP/2'
uv run --frozen --no-dev nvkb show CVE-2024-24989
uv run --frozen --no-dev nvkb stats

# Xuất danh mục CVE ra data/exports/
uv run --frozen --no-dev nvkb export --format csv
uv run --frozen --no-dev nvkb export --format jsonl

# Đối chiếu inventory được cung cấp, không quét máy chủ
uv run --frozen --no-dev nvkb assess-inventory examples/inventory.example.json
```

Chỉnh inventory mẫu theo tài sản thực tế. Mỗi phần tử cần `asset_id` duy nhất; các trường `product`, `installed_version`, `distribution`, `release`, `package_name` và `package_version` được dùng để đối chiếu phiên bản/gói. Có thể bổ sung `runtime_evidence`, `inventory_provenance`, `package_origin` và `custom_build` để ghi nhận nguồn dữ liệu và tình trạng kiểm chứng. Thiếu bằng chứng hoặc ngữ cảnh có thể dẫn đến kết quả chưa xác định; không diễn giải thiếu thông tin thành đã an toàn.

## Cập nhật nguồn và cấu hình

| Tệp | Nội dung |
| --- | --- |
| `config/scope.yaml` | Năm công bố, mốc dữ liệu, sản phẩm chính và phạm vi lịch sử. |
| `config/sources.yaml` | Nguồn NGINX, CVE, Vulnerability-Lookup và bản phân phối. |
| `config/settings.yaml` | Timeout, retry, khoảng nghỉ HTTP, đường dẫn vault/SQLite và chính sách provenance. |
| `config/logging.yaml` | Định dạng và mức log. |

Các lệnh sau thay đổi dữ liệu cục bộ; nên commit hoặc sao lưu phần biên soạn trước khi cập nhật:

```bash
# Xem thay đổi dự kiến từ nguồn công khai
uv run --frozen --no-dev nvkb update --dry-run

# Cập nhật dữ liệu và tái dựng read models
uv run --frozen --no-dev nvkb update

# Thu thập theo năm công bố hoặc một CVE
uv run --frozen --no-dev nvkb sync --year 2025
uv run --frozen --no-dev nvkb sync --cve CVE-2024-24989

# Chạy với cache hiện có; báo lỗi nếu thiếu snapshot cần thiết
uv run --frozen --no-dev nvkb update --offline
```

`sync` chỉ thu thập và ghi dữ liệu; chạy `nvkb build` sau đó để cập nhật SQLite/vault. `update` thực hiện cả hai bước. `nvkb enrich` nạp thêm nội dung tri thức biên soạn và provenance; dùng `--offline` khi chỉ muốn đọc cache. `nvkb schema` sinh lại JSON Schema và tài liệu ontology cục bộ. `nvkb conflicts` xem xung đột và `nvkb report` sinh báo cáo chất lượng cục bộ trong thư mục đã được Git bỏ qua.

## Xử lý lỗi thường gặp

- **Không tìm thấy workspace:** chạy trong thư mục repo hoặc truyền `nvkb --root /path/to/NVKB ...`.
- **Chưa có database:** chạy `nvkb build` trước `nvkb search`.
- **Snapshot/hash hoặc tham chiếu không hợp lệ:** đọc lỗi từ `nvkb validate`, khôi phục tệp dữ liệu tương ứng; đừng xóa `data/raw/` vì bằng chứng đang tham chiếu tới snapshot.
- **Offline thiếu cache:** chạy thu thập online cho nguồn còn thiếu, sau đó kiểm tra lại dữ liệu.
- **Vault có note bị sửa tay:** sao lưu nội dung và giải quyết xung đột manifest trước khi build lại.
- **Nguồn công khai đổi cấu trúc hoặc tạm lỗi:** xem `logs/nvkb.log`, cấu hình nguồn và đầu ra CLI; lần cập nhật có lỗi không bảo đảm dữ liệu đã đầy đủ.

## Nguồn và quyền sử dụng

Snapshot, bản ghi CVE và tài liệu tham khảo giữ nguồn/bản quyền riêng của bên cung cấp; không được tái cấp license theo mã NVKB. Dependency được quản lý qua `pyproject.toml` và `uv.lock`; không đóng gói binary hoặc thư viện bên thứ ba vào repo. Bản này dành cho repo private và chưa khai báo giấy phép phát hành mã nguồn công khai.
