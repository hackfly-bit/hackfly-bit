"""Render profile stat cards from the GitHub API.

One repository can contain a bundled frontend large enough to hide the
languages actually used to build the apps. Each language is capped per
repository so the chart stays representative.
"""

import json
import subprocess
from pathlib import Path

USER = "hackfly-bit"
CAP_BYTES = 1_500_000
SKIP = {"HTML", "CSS", "SCSS", "Sass", "Less", "Hack"}
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

LANG_QUERY = """
query {
  user(login: "%s") {
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      nodes {
        stargazerCount
        languages(first: 8, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
""" % USER


def gh_json(args):
    result = subprocess.run(
        ["gh", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def comma(value):
    return f"{value:,}"


def load_stats():
    user = gh_json(["api", f"users/{USER}"])
    commits = gh_json(
        [
            "api",
            f"search/commits?q=author:{USER}&per_page=1",
            "-H",
            "Accept: application/vnd.github.cloak-preview+json",
        ]
    )["total_count"]
    pulls = gh_json(
        ["api", f"search/issues?q=author:{USER}+type:pr&per_page=1"]
    )["total_count"]
    issues = gh_json(
        ["api", f"search/issues?q=author:{USER}+type:issue&per_page=1"]
    )["total_count"]
    repos = gh_json(["api", "graphql", "-f", f"query={LANG_QUERY}"])
    nodes = repos["data"]["user"]["repositories"]["nodes"]
    stars = sum(node["stargazerCount"] or 0 for node in nodes)
    languages = {}
    for node in nodes:
        for edge in node["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in SKIP:
                continue
            languages.setdefault(name, {"size": 0, "color": edge["node"]["color"]})
            languages[name]["size"] += min(edge["size"], CAP_BYTES)
    ranked = sorted(languages.items(), key=lambda item: -item[1]["size"])[:6]
    total = sum(item[1]["size"] for item in ranked) or 1
    return {
        "stars": stars,
        "commits": commits,
        "pulls": pulls,
        "issues": issues,
        "repos": user["public_repos"],
        "followers": user["followers"],
        "languages": [
            (name, info["color"], round(info["size"] * 100 / total, 1))
            for name, info in ranked
        ],
    }


def text(x, y, value, fill, size=14, weight="400"):
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" font-family="Segoe UI, Ubuntu, Sans-Serif">{value}</text>'
    )


def stats_svg(stats):
    rows = [
        (28, "Total Stars", comma(stats["stars"]), 250, "Total Commits", comma(stats["commits"])),
        (78, "Total PRs", comma(stats["pulls"]), 250, "Total Issues", comma(stats["issues"])),
        (128, "Public Repos", comma(stats["repos"]), 250, "Followers", comma(stats["followers"])),
    ]
    body = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="495" height="195" viewBox="0 0 495 195">',
        '<rect width="495" height="195" rx="8" fill="#141321"/>',
        text(24, 36, "GitHub Stats", "#fe428e", 18, "600"),
    ]
    for y, left_label, left_value, right_x, right_label, right_value in rows:
        body.append(f'<circle cx="32" cy="{y + 22}" r="4" fill="#f8d847"/>')
        body.append(text(46, y + 18, left_label, "#a9fef7", 13))
        body.append(text(46, y + 40, left_value, "#f8f8f2", 18, "600"))
        body.append(f'<circle cx="{right_x}" cy="{y + 22}" r="4" fill="#fe428e"/>')
        body.append(text(right_x + 14, y + 18, right_label, "#a9fef7", 13))
        body.append(text(right_x + 14, y + 40, right_value, "#f8f8f2", 18, "600"))
    body.append("</svg>")
    return "\n".join(body) + "\n"


def languages_svg(languages):
    height = 58 + len(languages) * 28
    body = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}">',
        f'<rect width="400" height="{height}" rx="8" fill="#141321"/>',
        text(20, 32, "Top Languages", "#fe428e", 16, "600"),
    ]
    for index, (name, color, percent) in enumerate(languages):
        y = 52 + index * 28
        width = max(4, round(170 * percent / 100))
        body.append(text(20, y + 14, name, "#f8f8f2", 12))
        body.append(f'<rect x="158" y="{y + 4}" width="170" height="8" rx="4" fill="#2a2738"/>')
        body.append(f'<rect x="158" y="{y + 4}" width="{width}" height="8" rx="4" fill="{color}"/>')
        body.append(
            f'<text x="384" y="{y + 14}" fill="#a9fef7" font-size="11" text-anchor="end" '
            f'font-family="Segoe UI, Ubuntu, Sans-Serif">{percent:.1f}%</text>'
        )
    body.append("</svg>")
    return "\n".join(body) + "\n"


def main():
    stats = load_stats()
    OUT.mkdir(exist_ok=True)
    (OUT / "github-stats.svg").write_text(stats_svg(stats), encoding="utf-8")
    (OUT / "top-langs.svg").write_text(languages_svg(stats["languages"]), encoding="utf-8")
    print(json.dumps({k: v for k, v in stats.items()}, indent=2))


if __name__ == "__main__":
    main()
