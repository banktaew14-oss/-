import random
from typing import Dict, List, Tuple

# ==========================================
# CREDITS / เครดิตผู้พัฒนา
# ==========================================
AUTHOR = "Bank Basketman"
FOOTER = f"--- ทำนายผลโดย {AUTHOR} ---"

def print_header(title: str) -> None:
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)


# ==========================================
# 1. ระบบทำนายหวยไทย (Thai Lottery Predictor)
# ==========================================
class ThaiLotteryPredictor:
    """
    วิเคราะห์และทำนายตัวเลขหวยไทย โดยอิงจากสถิติเลขเด่น ความถี่ และชุดตัวเลข
    """
    def __init__(self):
        # ตัวอย่างข้อมูลสถิติความถี่ตัวเลข (0-9) ที่ออกบ่อย
        self.digit_weights = [12, 15, 8, 19, 14, 11, 17, 9, 16, 13]

    def predict_2digit(self, count: int = 3) -> List[str]:
        """ทำนายเลขท้าย 2 ตัว"""
        predictions = set()
        digits = list(range(10))
        while len(predictions) < count:
            # สุ่มเลือกตัวเลขตามน้ำหนักความถี่สถิติ
            d1 = random.choices(digits, weights=self.digit_weights)[0]
            d2 = random.choices(digits, weights=self.digit_weights)[0]
            predictions.add(f"{d1}{d2}")
        return list(predictions)

    def predict_3digit(self, count: int = 3) -> List[str]:
        """ทำนายเลขท้าย 3 ตัว"""
        predictions = set()
        digits = list(range(10))
        while len(predictions) < count:
            d1 = random.choices(digits, weights=self.digit_weights)[0]
            d2 = random.choices(digits, weights=self.digit_weights)[0]
            d3 = random.choices(digits, weights=self.digit_weights)[0]
            predictions.add(f"{d1}{d2}{d3}")
        return list(predictions)


# ==========================================
# 2. ระบบวิเคราะห์ผลบอล (Football Analytics)
# ==========================================
class FootballAnalyzer:
    """
    วิเคราะห์ผลการแข่งขันฟุตบอลจากค่าเฉลี่ยประตูและฟอร์มการเล่น
    """
    def analyze_match(self, home_team: str, away_team: str, home_avg: float, away_avg: float) -> Dict[str, str]:
        # คำนวณแต้มคาดการณ์ง่ายๆ จากค่าเฉลี่ยประตู
        exp_home_goals = round(home_avg * 1.1)  # ได้เปรียบในบ้าน
        exp_away_goals = round(away_avg * 0.9)

        if exp_home_goals > exp_away_goals:
            outcome = f"{home_team} มีโอกาสชนะสูงกว่า"
        elif exp_home_goals < exp_away_goals:
            outcome = f"{away_team} มีโอกาสชนะสูงกว่า"
        else:
            outcome = "โอกาสเสมอสูง"

        return {
            "match": f"{home_team} vs {away_team}",
            "predicted_score": f"{exp_home_goals} - {exp_away_goals}",
            "analysis": outcome
        }


# ==========================================
# 3. ระบบวิเคราะห์ผลบาสเกตบอล (Basketball Analytics)
# ==========================================
class BasketballAnalyzer:
    """
    วิเคราะห์ผลการแข่งขันบาสเกตบอล (Pace, PPG, และคาดการณ์สกอร์สูง/ต่ำ)
    """
    def analyze_match(self, home_team: str, away_team: str, 
                      home_ppg: float, home_opp_ppg: float,
                      away_ppg: float, away_opp_ppg: float) -> Dict[str, str]:
        
        # คาดการณ์คะแนนรวมของทั้งสองทีม
        est_home_score = (home_ppg + away_opp_ppg) / 2
        est_away_score = (away_ppg + home_opp_ppg) / 2
        total_score = est_home_score + est_away_score

        winner = home_team if est_home_score > est_away_score else away_team
        margin = abs(est_home_score - est_away_score)

        return {
            "match": f"{home_team} vs {away_team}",
            "projected_score": f"{round(est_home_score, 1)} - {round(est_away_score, 1)}",
            "predicted_winner": f"{winner} (ต่อแต้มประมาณ {round(margin, 1)} แต้ม)",
            "total_points_exp": f"คาดการณ์แต้มรวม: {round(total_score, 1)}"
        }


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":

    # 1. ทำนายหวยไทย
    print_header("🎯 สรุปแนวทางหวยไทย (Thai Lottery)")
    lottery = ThaiLotteryPredictor()
    print("เลขเด่น 2 ตัวท้าย:", ", ".join(lottery.predict_2digit(4)))
    print("เลขเด่น 3 ตัวท้าย:", ", ".join(lottery.predict_3digit(3)))
    print(FOOTER)

    # 2. วิเคราะห์ผลบอล
    print_header("⚽ วิเคราะห์ผลฟุตบอล (Football Prediction)")
    fb = FootballAnalyzer()
    fb_res = fb.analyze_match("Arsenal", "Chelsea", home_avg=2.1, away_avg=1.2)
    print(f"คู่แข่งขัน: {fb_res['match']}")
    print(f"คาดการณ์สกอร์: {fb_res['predicted_score']}")
    print(f"บทวิเคราะห์: {fb_res['analysis']}")
    print(FOOTER)

    # 3. วิเคราะห์ผลบาสเกตบอล
    print_header("🏀 วิเคราะห์ผลบาสเกตบอล (Basketball Prediction)")
    bb = BasketballAnalyzer()
    bb_res = bb.analyze_match(
        home_team="LA Lakers", 
        away_team="Golden State Warriors",
        home_ppg=115.4, home_opp_ppg=112.0,
        away_ppg=118.2, away_opp_ppg=115.1
    )
    print(f"คู่แข่งขัน: {bb_res['match']}")
    print(f"คาดการณ์คะแนน: {bb_res['projected_score']}")
    print(f"ทีมคาดว่าจะชนะ: {bb_res['predicted_winner']}")
    print(f"คะแนนรวมคาดการณ์: {bb_res['total_points_exp']}")
    print(FOOTER)
