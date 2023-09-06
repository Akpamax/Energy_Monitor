function py_mat_iface(mach_id, mach_type, mach_energy)
%
data = struct();
data.machine_id = mach_id;
data.machine_type = mach_type;
data.energy = mach_energy;

coder.extrinsic('jsonencode');
coder.extrinsic('pyrunfile');
% Convert the structure to a JSON string
jsonStr = jsonencode(data);

% Print the JSON string
%disp(jsonStr);

%Send JSON payload to aws 
topic1 = 'workshop/machines';
payload = jsonStr;
pyrunfile("main.py",topic= topic1,payload=jsonStr);
end
