# QT PySide2 Sample Projects


1. Currency Converter, loading csv file

2. Expression evaluator

3. more signals, custom signals


### Documentation:

#### Dialog Categories

By Intelligence:

- Dumb
- Standard
- Smart

By Modality:
- Application modal
- Window modal
- Modeless

#### Modality Classification

- Application modal: once the dialog is invoked, it's the only part of the app you can interact with.

- Window modal: similar as the above, except it prevents interaction with all its parents

- Modeless: when invoked, you can interact with the dialog and the rest of the application, 
has an effect on how we write the code

#### Dumb Dialogs

- A dumb dialog is a dialog whose widgets are set to their 
initial values by dialog's caller (parent)

- It is unaware of the data it contains

- Advantage: no need for additional API code

- Disadvantage: tied to the user interface, 
lack of ability to add complex validation

#### Standard Dialogs

- A standard dialog initializes its widgets in accordance
with the values set through the methods (or the initializer)

- Its values are obtained by method calls or instance variables
and not directly

- Advantage: the caller needs not know its implementation
just how to get end values

- Disadvantage: clutters code if there's lots of settings to 
be handled


#### Smart Dialogs

- A smart dialog initializes its data based on data 
references or structures passed to it.

- It is capable of updating the data directly (in real time)
in response to user interaction

- Usually modeless

- Advantages: looks cool, little code involved

- Disadvantages: being modeless, we are risking not handling data changes 
if the user interactacts with the bottom part of the app
