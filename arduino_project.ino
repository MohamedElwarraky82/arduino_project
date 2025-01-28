void serial_init();
String read_data();
void write_data(String res);
void start_tests();
void  end_test();
void assert_equal(String name, int x, int y);
void assert_not_equal(String name, int x, int y);


void test1(){
  int x = 5;
  int y = 5;
  assert_equal("Test1", x, y);
}

void test2(){
  int x = 5;
  int y = 6;
  assert_not_equal("Test2", x, y);
}

void setup() {
  serial_init();
  start_tests();
}

void loop() {
  test1();
  test2();
  end_test();
  return;
}


void serial_init(){
  Serial.begin(115200);
  Serial.setTimeout(1);
}


String read_data(){
  if (Serial.available() > 0){
    Serial.flush();
    return Serial.readString();
  }
}

void write_data(String res){
  Serial.println(res.c_str());
  Serial.flush();
}

void start_tests(){
  while(!read_data() == 'S');
  write_data("1");
}

void  end_test(){
  write_data("End");
  Serial.end();
}

void assert_equal(String name, int x, int y){
  if(x==y){
    write_data(name +":1" );
  }
  else{
    write_data(name +":0" );
  }
}

void assert_not_equal(String name, int x, int y){
  if(x==y){
    write_data(name +":0" );
  }
  else{
    write_data(name +":1" );
  }
}