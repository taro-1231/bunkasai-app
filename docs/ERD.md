ユースケース

学校オーナーはテナントを登録（作成）できる。
スタッフは店を登録、編集できる
来場者は模擬店一覧と開催スケジュールを閲覧できる
来場者は人気投票を1人1票で行える
運営はお知らせ、イベントを投稿、編集できる


エンティティ

Tenant（学校）
User（オーナー、スタッフ、出店者など）
Booth（模擬店）
Event（スケジュール枠）
Announcement（お知らせ）


ER図
erDiagram
    TENANTS ||--o{ USERS : "1対多"
    TENANTS ||--o{ BOOTHS : "1対多"
    TENANTS ||--o{ EVENTS : "1対多"
    TENANTS ||--o{ ANNOUNCEMENTS : "1対多"
    TENANTS ||--o{ BOOTH_MEMBERS : "1対多"
    USERS   ||--o{ BOOTH_MEMBERS : "1対多"
    BOOTHS  ||--o{ BOOTH_MEMBERS : "1対多"

    TENANTS {
      UUID id PK
      TEXT name
      CITEXT subdomain "URL用キー（英数字） UNIQUE NOT NULL"
      TEXT plan        "free/standard/pro"
      TIMESTAMPTZ created_at "DEFAULT now()"
    }

    USERS {
      UUID id PK
      UUID tenant_id FK
      CITEXT username  "学校内で一意 NOT NULL"
      TEXT password_hash
      TEXT role        "owner/staff/vendor/viewer"
      TIMESTAMPTZ created_at "DEFAULT now()"
      UNIQUE (tenant_id, username)
    }

    BOOTHS {
      UUID id PK
      UUID tenant_id FK
      TEXT name
      TEXT group_name
      CITEXT slug      "URL用識別子 NOT NULL"
      TEXT category
      TEXT summary     "短い説明（一覧カード）"
      TEXT description_md "詳細（Markdown）"
      TEXT image_url
      TEXT location
      TIMESTAMPTZ open_from
      TIMESTAMPTZ open_to
      TIMESTAMPTZ created_at "DEFAULT now()"
      UNIQUE (tenant_id, slug)
    }

    EVENTS {
      UUID id PK
      UUID tenant_id FK
      TEXT title
      TEXT group_name
      TIMESTAMPTZ start_at
      TIMESTAMPTZ end_at
      TEXT location
      TEXT description
      TIMESTAMPTZ created_at "DEFAULT now()"
    }

    ANNOUNCEMENTS {
      UUID id PK
      UUID tenant_id FK
      TEXT title
      TEXT body         "本文（Markdown）"
      BOOLEAN pinned    "DEFAULT false"
      TIMESTAMPTZ published_at "DEFAULT now()"
    }
    BOOTH_MEMBERS {
      UUID id PK
      UUID tenant_id FK
      UUID booth_id  FK
      UUID user_id   FK
      TEXT role      "vendor 固定"
      TIMESTAMPTZ created_at "DEFAULT now()"
      UNIQUE (tenant_id, booth_id, user_id)
    }



追加機能
イベントのアラーム
投票
