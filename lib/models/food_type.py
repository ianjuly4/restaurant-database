# lib/models/food_type.py
from models.__init__ import CURSOR, CONN

class Food_type:
    
    all = {}

    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.description}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description) < 10:
            self._description = description
        else:
            raise ValueError(
                "Description must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Food_type instances """
        sql = """
            CREATE TABLE IF NOT EXISTS food_types (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Food_type instances """
        sql = """
            DROP TABLE IF EXISTS food_types;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Food_type instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO food_types (name, description)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, description):
        """ Initialize a new Food_type instance and save the object to the database """
        department = cls(name, description)
        department.save()
        return department

    def update(self):
        """Update the table row corresponding to the current food_type instance."""
        sql = """
            UPDATE food_types
            SET name = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Food_type instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM food_types
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Food_type object having the attribute values from the table row."""

        food_type = cls.all.get(row[0])
        if food_type:
            food_type.name = row[1]
            food_type.description = row[2]
        else:
            food_type = cls(row[1], row[2])
            food_type.id = row[0]
            cls.all[food_type.id] = food_type
        return food_type

    @classmethod
    def get_all(cls):
        """Return a list containing a Food_type object per row in the table"""
        sql = """
            SELECT *
            FROM food_types
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Food_type object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM food_types
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Food_type object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM food_types
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def employees(self):
        """Return list of restaurants associated with current food type"""
        from models.restaurant import Restaurant
        sql = """
            SELECT * FROM restaurants
            WHERE food_type_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Restaurant.instance_from_db(row) for row in rows
        ]