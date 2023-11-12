#!/usr/bin/python3
"""
    models/base.py module
"""
import json
import csv


class Base:
    """
    This is the superclass for managing id attributes in future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): If specified, assigns the public instance attribute
            'id' with this value.Otherwise, increments __nb_objects
            and assigns the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        # Get the class name
        class_name = cls.__name__
        # Create the filename
        filename = f"{class_name}.json"
        obls = []
        for obj in list_objs:
            ob = obj.to_dictionary()
            obls.append(ob)
        json_string = cls.to_json_string(obls)
        # Write the JSON string to the file
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        if json_string == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
        """
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
        """
        instance = cls(**dict(dictionary))
        return instance

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in list_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to CSV format and writes to a file.
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if class_name == 'Rectangle':
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif class_name == 'Square':
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    continue

                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes from CSV format and returns a list of instances.
        """
        filename = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)

                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(int(row[0]), int(row[1]), int(row[2]),
                                  int(row[3]), int(row[4]))
                    elif cls.__name__ == 'Square':
                        obj = cls(int(row[0]), int(row[1]), int(row[2]),
                                  int(row[3]))
                    else:
                        continue

                    instances.append(obj)

        except FileNotFoundError:
            pass

        return instances
