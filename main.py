def convert_to_one_line(text):
    return text.replace('\n', '\\n')

def main():
    print("Enter your multi-line text (press Ctrl+D or Ctrl+Z when done):")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        multi_line_text = '\n'.join(lines)
        one_line_text = convert_to_one_line(multi_line_text)
        print("\nConverted text:")
        print(one_line_text)
    except KeyboardInterrupt:
        print("\nInput cancelled.")

if __name__ == "__main__":
    main()