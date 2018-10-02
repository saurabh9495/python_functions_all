byte_array = bytearray('XYZ', 'utf-8') 
print('Before update:', byte_array) 
mem_view = memoryview(byte_array)  
mem_view[2]= 80
print('After update:', byte_array) 

# Before update: bytearray(b'XYZ')
# After update: bytearray(b'XYP')