#include <algorithm>
#include <iostream>
#include <vector>
#include <iterator>

std::string esc_str(const std::string& str, char ch)
{
    std::vector<char> buffer(str.size());

    for(auto curr = str.begin(); curr != str.end(); ++curr)
    {
        if (*curr == ch) {
            buffer.push_back('\\');
        }
        buffer.push_back(*curr);
    }

    std::string res(buffer.begin(), buffer.end());
    //std::cout << "Result:";
    //std::copy(buffer.begin(), buffer.end(), std::ostream_iterator<char>(std::cout, ""));
    //std::cout << std::endl;

    return res;
}

int main()
{
    std::cout << "Result: " << esc_str("Hello world!", 'l') << std::endl;
  return 0;
}
