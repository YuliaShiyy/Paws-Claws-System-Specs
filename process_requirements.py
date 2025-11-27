import pandas as pd
import csv
import re

input_file = 'requirements_specification.csv'
output_file = 'REQUIREMENTS_SORTED.md'


# --- Helper functions: Text enhancement ---
def format_confirmation(text):
    if not text: return "N/A"
    formatted = text.replace('Test', '<br>• **Test**')
    if formatted.startswith('<br>'): formatted = formatted[4:]
    return formatted.strip()


def format_conversation(text):
    if not text: return ""
    text = text.replace('e.g.', 'e_g_')
    text = text.replace('.', '.<br>')
    text = text.replace('e_g_', 'e.g.')
    return text.strip()


# --- Core function: Parses the ID and Title, and extracts the Key for sorting. ---
def parse_id_title_sort_key(raw_string):
    clean_str = raw_string.replace('–', '-').replace('—', '-')

    parts = clean_str.split('-')

    # default value
    final_id = raw_string
    final_title = ""
    sort_group = "ZZZ"  # 默认排最后
    sort_num = 9999  # 默认排最后

    if len(parts) >= 3:
        # Assembly ID: "GRM" + " - " + "USC 1"
        final_id = f"{parts[0].strip()} - {parts[1].strip()}"

        # Assemble the Title: Reassemble all remaining parts
        # (to prevent horizontal lines from appearing in the Title as well).
        final_title = "-".join(parts[2:]).strip()

        # Extract the sort key.
        # Group: Take the first part (e.g., "GRM")
        sort_group = parts[0].strip()

        # Number: Take the number from the middle part (e.g., "USC 1" -> 1)
        num_match = re.search(r'\d+', parts[1])
        if num_match:
            sort_num = int(num_match.group())
        else:
            sort_num = 0

    elif len(parts) == 2:
        # Error tolerance: If there is only one section (e.g., only GRM-1), without a title
        final_id = raw_string
        sort_group = parts[0].strip()
        num_match = re.search(r'\d+', parts[1])
        if num_match: sort_num = int(num_match.group())

    return final_id, final_title, sort_group, sort_num


# --- Main program ---
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()[2:]  # skip metadata

reader = csv.reader(lines)
parsed_data = []

for row in reader:
    if len(row) >= 2:
        raw_first_col = row[0].strip()

        # 1. Parsing ID, Title, and Sort Key
        req_id, req_title, sort_group, sort_num = parse_id_title_sort_key(raw_first_col)

        category = row[-1].strip()
        full_text = ",".join(row[1:-1])

        # 2. CCC split
        split_card = re.split(r'Conversation:', full_text, flags=re.IGNORECASE)
        card_content = split_card[0].replace('GRM - USC', '').replace('USC', '').strip()  # 清理残留
        remaining = split_card[1] if len(split_card) > 1 else ""

        split_conv = re.split(r'Confirmation:', remaining, flags=re.IGNORECASE)
        conversation_raw = split_conv[0].strip()
        remaining_2 = split_conv[1] if len(split_conv) > 1 else ""

        split_conf = re.split(r'Dependencies:', remaining_2, flags=re.IGNORECASE)
        confirmation_raw = split_conf[0].strip()

        # 3. Filter invalid lines
        if len(card_content) < 5: continue

        parsed_data.append([
            sort_group,  # Used for sorting (hidden columns)
            sort_num,  # Used for sorting (hidden columns)
            req_id,  # First column：GRM - USC 1
            req_title,  # Second column：Create grooming...
            card_content,
            format_conversation(conversation_raw),
            format_confirmation(confirmation_raw)
        ])

# Generate DataFrame
columns = ['Sort_Group', 'Sort_Num', 'ID', 'Title', 'User Story', 'Details', 'Verification']
df = pd.DataFrame(parsed_data, columns=columns)

# Sort by Group (GRM, BRD) alphabetically, then sort by Num (1, 2, 10).
df = df.sort_values(by=['Sort_Group', 'Sort_Num'], ascending=[True, True])

df_final = df[['ID', 'Title', 'User Story', 'Details', 'Verification']]

df_final = df_final.replace(r'\n', '<br>', regex=True)

# Generate Markdown
markdown_table = df_final.to_markdown(index=False)

# Save file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Paws & Claws - Requirements Specification\n\n")
    f.write(f"> **Total User Stories:** {len(df_final)}\n")
    f.write(f"> *Sorted by Module ID (Natural Order)*\n\n")
    f.write(markdown_table)

print(f"✅ Sorted {len(df_final)} requirements.")
print(f"📄 File saved as: {output_file}")
print(f"   Example Order: {df_final['ID'].iloc[0]} -> {df_final['ID'].iloc[1]} ...")