// Copyright 2024 Steve Nginyo
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Define an interface
abstract class Bird {
  void fly();
}

// Define a class that implements the interface
class Sparrow implements Bird {
  @override
  void fly() {
    print('The sparrow is flying.');
  }
}

// Define a class that extends the Sparrow class and overrides the fly method
class Penguin extends Sparrow {
  @override
  void fly() {
    print('Penguins cannot fly!');
  }
}

void main() {
  // Create an instance of the Sparrow class
  var sparrow = Sparrow();
  sparrow.fly(); // Outputs: The sparrow is flying.

  // Create an instance of the Penguin class
  var penguin = Penguin();
  penguin.fly(); // Outputs: Penguins cannot fly!

  // Simulate reading data from a file
  var birdsData = ['sparrow', 'penguin', 'sparrow', 'sparrow', 'penguin'];

  // Use a loop to create instances of classes based on the data
  for (var birdData in birdsData) {
    if (birdData == 'sparrow') {
      var bird = Sparrow();
      bird.fly();
    } else if (birdData == 'penguin') {
      var bird = Penguin();
      bird.fly();
    }
  }
}
