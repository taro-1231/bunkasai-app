Base URL: https://{subdomain}.yourfest.app/api/v1
Tenant: サブドメインで解決（tenant_id はリクエストに含めない）

共通ポリシー

成功コード原則：GET=200, POST=201(+Location), PATCH=200, DELETE=204

デフォルトエラー（全エンドポイントに適用）：401/403/404/422

日時：ISO 8601（UTC）例 2025-10-12T09:00:00Z

ページング：{ items: T[], page: number, limit: number, total: number }

409（重複時）：username_conflict / slug_conflict を各POSTに明記

/api/v1/public

GET /booths?q=&category=&page=&limit= → Page〈BoothListItem〉

GET /booths/{slug} → BoothDetail

GET /events?from=&to=&location=&page=&limit= → Page〈EventItem〉

GET /announcements?include_pinned=&page=&limit= → { pinned: AnnouncementItem[], items: AnnouncementItem[], page, limit, total }

/api/v1/owner

POST /users（{username,password,role}）→ 201 + Location / UserItem（409: username_conflict）

PATCH /users/{id}/role → UserItem

DELETE /users/{id} → 204

POST /booths/{booth_id}/members（{user_id}）→ 201 / { booth_id, user_id }

DELETE /booths/{booth_id}/members/{user_id} → 204

/api/v1/staff

POST /events → 201 / EventItem

PATCH /events/{id} → EventItem

DELETE /events/{id} → 204

POST /announcements → 201 / AnnouncementItem

PATCH /announcements/{id} → AnnouncementItem

DELETE /announcements/{id} → 204

（※ ブース作成を運営側で行う場合は）POST /booths → 201 + Location / BoothDetail（409: slug_conflict）

/api/v1/vendor

GET /booths → Page〈BoothDetail〉（または BoothListItem）

PATCH /booths/{id} → BoothDetail

（※ ベンダーが下書き作成する場合は）POST /booths → 201 + Location / BoothDetail

/api/v1/auth

POST /login（{username,password}）→ 200 / { user: UserItem }（セッションクッキー）

POST /logout → 204

互換性ポリシー

追加はOK、削除/改名はNG（破壊的変更は /api/v2 で）