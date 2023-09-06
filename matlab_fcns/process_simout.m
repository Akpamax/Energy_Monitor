% Create a sample JSON structure
data = struct();
data.name = 'John Doe';
data.age = 30;
data.city = 'New York';

% Convert the structure to a JSON string
jsonStr = jsonencode(data);

% Print the JSON string
disp(jsonStr);

%Send JSON to aws 
topic1 = 'machines/mach1';
payload = jsonStr;
pyrunfile("../python_mqtt_interface/main.py",topic= topic1,payload=jsonStr);
