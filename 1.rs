fn main() {
    let data = std::fs::read("1.input").unwrap();
    let text = std::str::from_utf8(&data).unwrap();
    let mut lines = text.lines().map(str::trim_end);
    let mut sums: Vec<u32> = vec![];
    loop {
        let group: Vec<_> = lines.by_ref().take_while(|line| !line.is_empty()).collect();
        if group.is_empty() {
            break;
        }
        sums.push(
            group
                .into_iter()
                .map(|line| line.parse::<u32>().unwrap())
                .sum(),
        );
    }
    sums.sort_unstable();

    let largest = sums.pop().unwrap();
    println!("Largest: {largest}");

    let largest3 = largest + sums.pop().unwrap() + sums.pop().unwrap();
    println!("Largest 3: {largest3}");
}
