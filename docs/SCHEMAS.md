Schemas

Page<T>
| フィールド | 型      | 必須 | 説明    |
| ----- | ------ | -- | ----- |
| items | T\[]   | 必須 | 要素配列  |
| page  | number | 必須 | 1以上   |
| limit | number | 必須 | 1–100 |
| total | number | 必須 | 0以上   |

BoothListItem
| フィールド      | 型                 | 必須 | 説明/制約                      |
| ---------- | ----------------- | -- | -------------------------- |
| id         | uuid              | 必須 |                            |
| slug       | string            | 必須 | `^[a-z0-9]+(-[a-z0-9]+)*$` |
| name       | string            | 必須 | ≤80                        |
| summary    | string            | 任意 | ≤200                       |
| category   | string            | 任意 |                            |
| image\_url | string(url)       | 任意 |                            |
| open\_from | string(date-time) | 任意 |                            |
| open\_to   | string(date-time) | 任意 |                            |

BoothDetail（= BoothListItem + 追加）
| フィールド           | 型      | 必須 | 説明 |
| --------------- | ------ | -- | -- |
| description\_md | string | 任意 |    |
| location        | string | 任意 |    |

EventItem
| フィールド       | 型                 | 必須 |
| ----------- | ----------------- | -- |
| id          | uuid              | 必須 |
| title       | string            | 必須 |
| start\_at   | string(date-time) | 必須 |
| end\_at     | string(date-time) | 任意 |
| location    | string            | 任意 |
| description | string            | 任意 |

AnnouncementItem
| フィールド         | 型                 | 必須 |
| ------------- | ----------------- | -- |
| id            | uuid              | 必須 |
| title         | string            | 必須 |
| body          | string            | 必須 |
| pinned        | boolean           | 必須 |
| published\_at | string(date-time) | 必須 |

UserItem
| フィールド       | 型                               | 必須 |
| ----------- | ------------------------------- | -- |
| id          | uuid                            | 必須 |
| username    | string                          | 必須 |
| role        | enum(owner/staff/vendor/viewer) | 必須 |
| created\_at | string(date-time)               | 必須 |


