## Build Steps

pip install -r requirements.txt

## Run tests

python -m pytest -v

## Execute the solution

python -m geektrust <absolute_path_to_input_file>

## Assumptions

1. Every line in the file has a kingdom name followed by a non-blank message.
2. The kingdom name should have a valid predefined sybmol defined in config/kingdom_emblem.json.
3. Any invalid kingdom name or blank names will error out with a custom exception.
4. If multiple messages are sent to the same kingdom, all messages are considered till they become an ally. All messages to an allied kingdom are ignored thereafter.

    a. Example: In the following file -
              AIR **O**WLAOWLBOWLC
              AIR **ROZ**O
              AIR WATE**R**
              AIR **ROZ**
     The second transmission convinces AIR kingdom to become an ally as per the criteria. Hence, the third and fourth messages are not processed.

## Guidelines for future Enhancements

1. Any newly formed kingdoms in the universe of Southeros can be brought into consideration by adding the name and it's corresponding symbol to config/kingdom_emblem.json. The test case for invalid kingdom needs to be updated to include the newly added kingdom. 
2. The criteria for the ruler selection will be automatically modified to attainment of support of the majority of the kingdoms. It is defined as ceiling(number_of_kingdoms/2). This is desgined with the consideration that the candidate king has already secured his kingdom's support.
3. Tests for newly added code or features can be added under the tests/ directory and the required mock input data can be placed under tests/input/.
