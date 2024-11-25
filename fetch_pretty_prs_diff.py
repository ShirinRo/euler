#!/usr/bin/env python3

import argparse
import datetime
from github import Github


def main():
    args = parse_args()
    repo = repo_named(args.repo_name, args.personal_access_token)

    pulls = repo.get_pulls(state="closed", sort="updated", direction="desc", base="develop")
    relevant_pulls, breaking_prs = get_relevant_pulls(pulls, repo, args.start_commit,
                                                      args.target_commit)

    breaking_prs_texts = get_breaking_pulls_texts(breaking_prs, args.repo_name)
    print_opening_message(args.repo_name, breaking_prs_texts)

    print("# Included PRs:\n\n")
    pull_texts = get_pull_request_texts(relevant_pulls, args.repo_name, args.ndl)
    print("\n".join(pull_texts))


def parse_args():
    parser = argparse.ArgumentParser(
        description="""Creates a body for a PR that advances a submodule.""")
    parser.add_argument("personal_access_token", help="Personal access token of an org admin")
    parser.add_argument("repo_name", help="Name of the repo of the advanced submodule.")
    parser.add_argument("start_commit", help="Commit which the repo currently points to.")
    parser.add_argument("target_commit", help="Commit which the repo is advanced to.")
    parser.add_argument("--ndl", nargs="*", help="Labels for which description shouldn't be "
                                                 "added. PRs with any label that is not listed "
                                                 "will include a description.")
    return parser.parse_args()


def repo_named(name, access_token):
    github_handle = Github(login_or_token=access_token)
    all_repos = github_handle.get_user().get_repos()
    for repo in all_repos:
        if name in [repo.name, repo.full_name]:
            return repo
    raise Exception(f"No repo found for name {name}")


def get_relevant_pulls(pulls, repo, start_commit, target_commit):
    start_commit_date = date_from_commit(repo.get_commit(start_commit))
    target_commit_date = date_from_commit(repo.get_commit(target_commit))
    relevant_pulls = []
    breaking_pull_nums = []
    for pull in pulls:
        if pull.merged and start_commit_date < pull.merged_at <= target_commit_date:
            relevant_pulls += [pull]
            if is_breaking_change_pull(pull):
                breaking_pull_nums += [pull.number]
        if pull.updated_at < start_commit_date:
            break
    return relevant_pulls, breaking_pull_nums


def date_from_commit(commit):
    date_str = commit.last_modified
    date_format = "%a, %d %b %Y %H:%M:%S %Z"
    return datetime.datetime.strptime(date_str, date_format)


def is_breaking_change_pull(pull):
    return bool([label for label in pull.labels if "breaking" in label.name.lower()])


def get_pull_request_texts(relevant_pulls, repo_name, no_description_labels):
    return [pull_request_text(repo_name, pull, no_description_labels) for pull in relevant_pulls]

def pull_request_text(repo_name, pull, no_description_labels):
    title = f"## {pull.title}"
    metadata = f"[#{pull.number}](https://github.com/Lightricks/{repo_name}/pull/{pull.number}) " \
               f"Merged at: {pull.merged_at}"
    labels_text = "*Labels:* " + ", ".join([pretty_label_text(label) for label in pull.labels])
    description = ""
    if pull.body and [label for label in pull.labels if label.name not in no_description_labels]:
        description = "\n#### Description:\n" + remove_mentions(pull.body)
    return title + "\n" + metadata + "\n" + labels_text + description + "\n\n---"


def pretty_label_text(label):
    hex_color = label.color
    color_square = f"![#{hex_color}](https://via.placeholder.com/15/{hex_color}/000000?text=+)"
    return f"{color_square} **{label.name}** {color_square}"


def remove_mentions(pull_body):
    return pull_body.replace("@", " ")


def get_breaking_pulls_texts(pulls_nums, repo_name):
    return [f"[#{number}](https://github.com/Lightricks/{repo_name}/pull/{number})"
            for number in pulls_nums]


def print_opening_message(repo_name, breaking_prs):
    print(f"Automatic ++{repo_name} created by checking out latest develop in {repo_name}.")
    breaking_prs_msg = f"This advancement includes {len(breaking_prs)} breaking PRs"
    if breaking_prs:
        breaking_prs_msg += f": {', '.join(breaking_prs)}"
    print(breaking_prs_msg + ".\n")
    print("If you're assigned to this PR you should:\n"
          "1. If there are breaking changes, fix them.\n"
          "2. Go over PRs to see if there are non-breaking changes that might affect the app, and "
          "make sure everything is OK.\n"
          "3. Pull the branch, compile it and run it for a sanity check.\n")


if __name__ == "__main__":
    main()