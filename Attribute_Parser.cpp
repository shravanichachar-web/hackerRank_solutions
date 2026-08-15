#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    cin.ignore(); // Ignore the newline character after reading n and q

    map<string, string> attributes;
    vector<string> tags;

    // Read HRML source code
    for (int i = 0; i < n; ++i) {
        string line;
        getline(cin, line);

        // If it's a closing tag
        if (line.substr(0, 2) == "</") {
            tags.pop_back();
        } 
        // If it's an opening tag
        else {
            int space_pos = line.find(' ');
            int close_pos = line.rfind('>');

            string tag_name;
            // If there are no attributes
            if (space_pos == string::npos || close_pos < space_pos) {
                tag_name = line.substr(1, close_pos - 1);
            } 
            // If there are attributes
            else {
                tag_name = line.substr(1, space_pos - 1);

                int pos = space_pos;
                while (pos < close_pos) {
                    // Skip any leading spaces
                    while (pos < line.length() && line[pos] == ' ') pos++;
                    if (pos >= close_pos) break;

                    // Find the equals sign
                    int eq_pos = line.find('=', pos);
                    if (eq_pos == string::npos) break;

                    // Extract and trim the attribute name
                    string attr_name = line.substr(pos, eq_pos - pos);
                    size_t start = attr_name.find_first_not_of(" ");
                    size_t end = attr_name.find_last_not_of(" ");
                    if (start != string::npos && end != string::npos) {
                        attr_name = attr_name.substr(start, end - start + 1);
                    }

                    // Find the attribute value inside the quotes
                    int quote1 = line.find('"', eq_pos);
                    int quote2 = line.find('"', quote1 + 1);
                    
                    if (quote1 == string::npos || quote2 == string::npos) break;

                    string attr_val = line.substr(quote1 + 1, quote2 - quote1 - 1);

                    // Construct the full path key (e.g., tag1.tag2~name)
                    string path = "";
                    for (const string& t : tags) {
                        path += t + ".";
                    }
                    path += tag_name;

                    // Store the attribute in the map
                    attributes[path + "~" + attr_name] = attr_val;

                    // Move position past the current attribute value
                    pos = quote2 + 1;
                }
            }
            // Add the new tag to our current nested state
            tags.push_back(tag_name);
        }
    }

    // Process the queries
    for (int i = 0; i < q; ++i) {
        string query;
        getline(cin, query);
        
        // Output the result if it exists, otherwise "Not Found!"
        if (attributes.find(query) != attributes.end()) {
            cout << attributes[query] << endl;
        } else {
            cout << "Not Found!" << endl;
        }
    }

    return 0;
}
