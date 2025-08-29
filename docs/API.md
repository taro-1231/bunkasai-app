APIルート

成功コードの原則：GET=200, POST=201(+Location), PATCH=200, DELETE=204
デフォルトエラー（全エンドポイントに適用）
401 Unauthorized / 403 Forbidden / 404 Not Found / 422 ValidationError


/api/v1/public
GET /booths?q=&category=&page=&limit=
200 → Page（items=BoothListItem）
GET /booths/{slug}
200 → BoothDetail
GET /events?from=&to=&location=&page=&limit=
200 → Page（items=EventItem）
GET /announcements?include_pinned=true&page=&limit=
200 → { "pinned":[AnnouncementItem], "items":[AnnouncementItem], "page":1, "limit":20, "total":57 }

/api/v1/owner
  POST   /users                         {username,password,role:"staff"|"vendor"}
  201 → UserItem,409 → username_conflict
  PATCH  /users/{id}/role               （owner⇔不可、staff/vendor間のみ）
  200 → UserItem
  DELETE /users/{id}
  204（本文なし）
  POST   /booths/{booth_id}/members     {user_id}  ← vendor割当
  201 → { "booth_id":"...", "user_id":"..." }
  DELETE /booths/{booth_id}/members/{user_id}
  204

/api/v1/staff
POST /api/v1/staff/booths … 201+Location → BoothDetail,409 → slug_conflict
POST /events … 201 → EventItem
PATCH /events/{id} … 200 → EventItem
DELETE /events/{id} … 204
POST /announcements … 201 → AnnouncementItem
PATCH /announcements/{id} … 200 → AnnouncementItem
DELETE /announcements/{id} … 204

/api/v1/vendor
GET /booths … 200 → Page（items=BoothDetail でも可）
PATCH /booths/{id} … 200 → BoothDetail

/api/v1/auth
POST /login {username,password} … 200 → { "user": UserItem }（＋セッションクッキー）
POST /logout … 204


Page
{
  "items": [ /* 要素の配列（後述の各Item） */ ],
  "page": 1,
  "limit": 20,
  "total": 57
}

BoothListItem
{
  "id": "uuid",
  "slug": "takoyaki-3a",
  "name": "たこ焼き 3A",
  "summary": "外カリ中トロ",
  "category": "food",
  "image_url": null,
  "open_from": "2025-10-12T09:00:00Z",
  "open_to": "2025-10-12T16:00:00Z"
}

BoothDetail
{
  "id": "uuid",
  "slug": "takoyaki-3a",
  "name": "たこ焼き 3A",
  "summary": "外カリ中トロ",
  "description_md": "### こだわり…",
  "location": "3年A組",
  "category": "food",
  "image_url": null,
  "open_from": "2025-10-12T09:00:00Z",
  "open_to": "2025-10-12T16:00:00Z"
}

EventItem
{
  "id":"uuid",
  "title":"吹奏楽ステージ",
  "start_at":"2025-10-12T11:00:00Z",
  "end_at":"2025-10-12T11:30:00Z",
  "location":"中庭",
  "description":""
}

AnnouncementItem
{
  "id":"uuid",
  "title":"開場時間変更",
  "body":"**10:30** 開場に変更します。",
  "pinned": true,
  "published_at":"2025-10-11T12:00:00Z"
}

UserItem
{ "id":"uuid", "username":"s12345", "role":"vendor", "created_at":"..." }
