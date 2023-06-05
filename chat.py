
def read_file(filename):
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):#格式轉換
	new = []
	person = None#先宣告person 避免第一行不是人名則當掉
	for line in lines:
		if line == "Allen":
			person = "Allen"
			continue
		elif line == "Tom":
			person = "Tom"
			continue
		if person:#if person有值才去執行這一行
			new.append(person + ":"+ line)
	return new

def write_file(filename,lines):
	with open(filename, "w", encoding = "utf-8") as f:#f 就是檔案
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file("input.txt")
	lines = convert(lines)#把聊天紀錄存在lines 裡面投進去
	write_file("output.txt", lines)

main()



		
