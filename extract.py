import pandas as pd
import json

def excel_to_json():
    excel_file = "audit_list.xlsx" # Apnar file-er namer sathe miliye nin
    output_file = "audit_data.json"

    print("Excel file reading shuru hoyeche...")

    try:
        # Excel read kora
        df = pd.read_excel(excel_file)

        # Khali row thakle muche fela
        df = df.dropna(how='all')

        data_list = []
        
        # Row wise data JSON-e convert kora
        for index, row in df.iterrows():
            # Iloc use kora hoyeche jate column-er namer jhamela na hoy
            # Index 0=SL, 1=TIN, 2=Zone, 3=Circle (PDF/Excel-er sequence onujayi)
            data_list.append({
                "tin": str(row.iloc[1]).strip(),
                "zone": str(row.iloc[2]).strip(),
                "circle": str(row.iloc[3]).strip()
            })

        # JSON file toiri kora
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4)

        print(f"Success! Total {len(data_list)} ti records JSON-e save hoyeche.")

    except Exception as e:
        print(f"Opps! Error hoyeche: {e}")

if __name__ == "__main__":
    excel_to_json()