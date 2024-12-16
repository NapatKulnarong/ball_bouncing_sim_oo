import csv
import os


class UserManager:
    def __init__(self, file_name):
        self.file_name = file_name
        # Initialize file with headers if it does not exist
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["username", "balance", "longest_distance"])

    def get_user_balance(self, username):
        """Get the balance"""
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    return int(row["balance"])
        return 0

    def get_longest_distance(self, username):
        """Get the longest distance"""
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    return float(row.get("longest_distance", 0.0))  # Defaults to 0.0 if missing
        return 0.0

    def get_user_data(self, username):
        """Get the user data as a dict."""
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    return {
                        "balance": int(row.get("balance", 0)),
                        "longest_distance": float(row["longest_distance"]) if row["longest_distance"] else 0.0                    }
        return {"balance": 0, "longest_distance": 0.0}

    def update_user_balance(self, username, coins):
        """Update user's balance, or create a new user"""
        updated = False
        rows = []
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    row["balance"] = str(int(row["balance"]) + coins)
                    updated = True
                rows.append(row)
        if not updated:
            rows.append({"username": username, "balance": str(coins), "longest_distance": "0.0"})
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["username", "balance", "longest_distance"])
            writer.writeheader()
            writer.writerows(rows)

    def update_longest_distance(self, username, new_distance):
        """Update user's longest distance"""
        rows = []
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    current_distance = float(row.get("longest_distance", 0.0) or 0.0)
                    if new_distance > current_distance:
                        row["longest_distance"] = f"{new_distance:.2f}"
                rows.append(row)
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["username", "balance", "longest_distance"])
            writer.writeheader()
            writer.writerows(rows)

    def get_top_players(self, top_n=10):
        """Get the top 10 players"""
        players = []
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                longest_distance = (
                    float(row["longest_distance"]) if row["longest_distance"].strip() else 0.0
                )
                players.append({"username": row["username"], "longest_distance": longest_distance})

        # Sort players
        players.sort(key=lambda x: x["longest_distance"], reverse=True)
        return players[:top_n]
