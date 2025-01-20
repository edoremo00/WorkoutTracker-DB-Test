from sqlalchemy import (DATE, DECIMAL, TEXT, TIMESTAMP, VARCHAR, Boolean, Column, Date,ForeignKey, Integer, Interval, String, Text, UniqueConstraint,create_engine, func, select)
from sqlalchemy.orm import DeclarativeBase,relationship,sessionmaker,mapped_column
from config import DATABASE_URL

engine=create_engine(DATABASE_URL)

Session=sessionmaker(bind=engine)

session=Session()

class Base(DeclarativeBase):
        pass
    
# class User(Base):
#     __tablename__="users"
#     id=mapped_column(Integer,primary_key=True,autoincrement=True)
#     username=mapped_column(VARCHAR(255),unique=True,nullable=False)
#     email=mapped_column(VARCHAR(50),unique=True,nullable=False)
#     created_at=mapped_column(TIMESTAMP(timezone=True),default=func.current_timestamp())
#     updated_at=mapped_column(TIMESTAMP(timezone=True))
#     password_hash=mapped_column(VARCHAR(255),nullable=False)
#     #da risolvere perchè rompe tutto
#     workouts=relationship("Workout",back_populates="user")
    

# class WorkoutExercise(Base):
#     __tablename__="workout_exercises"
#     id=mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False)
#     workout_id=mapped_column(Integer,ForeignKey("workouts.id"))
#     exercise_id=mapped_column(Integer,ForeignKey("exercises.id"))
#     sets=mapped_column(Integer,nullable=False)
#     weight=mapped_column(DECIMAL(5,2),nullable=False)
#     recovery_time=mapped_column(Interval,nullable=False)
#     # workout = relationship("Workout", back_populates="exercises")
#     # exercise = relationship("Exercise", back_populates="workout_exercises")
    
# class Workout(Base):
#     __tablename__ = "workouts"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     date = Column(Date, server_default=func.current_date())
#     notes = Column(Text)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
#     completed = Column(Boolean, default=False)

#     # Relationships
#     user = relationship("User", back_populates="workouts")
#     exercises = relationship(
#         "Exercise",secondary="workout_exercises"
#     )



# class Categories(Base):
#     __tablename__="categories"
#     id=mapped_column(Integer,primary_key=True,nullable=False,autoincrement=True)
#     name=mapped_column(VARCHAR,nullable=False,unique=True)
#     exercise_categories=relationship("Exercise",secondary="exercise_categories")
    
# class ExerciseCategory(Base):
#     __tablename__="exercise_categories"
#     id = mapped_column(Integer, primary_key=True, autoincrement=True)
#     exercise_id = mapped_column(Integer, ForeignKey("exercises.id"), nullable=False)
#     category_id = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)

#     # exercise = relationship("Exercise", back_populates="exercise_categories")
#     # category = relationship("Categories", back_populates="exercise_categories")

#     __table_args__ = (
#         UniqueConstraint("exercise_id", "category_id", name="uix_exercise_category"),
#     )
    
# class Exercise(Base):
#     __tablename__="exercises"
#     id=mapped_column(Integer,primary_key=True,autoincrement=True)
#     exercisename=mapped_column(VARCHAR(50),nullable=False)
#     # category = mapped_column(VARCHAR(50), nullable=False)
#     notes=mapped_column(TEXT)
#     workout_exercises = relationship("Workout", secondary="workout_exercises")
#     exercise_categories = relationship("Category",secondary="exercise_categories")
    
    
class User(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(VARCHAR(255), unique=True, nullable=False)
    email = mapped_column(VARCHAR(50), unique=True, nullable=False)
    created_at = mapped_column(TIMESTAMP(timezone=True), default=func.current_timestamp())
    updated_at = mapped_column(TIMESTAMP(timezone=True))
    password_hash = mapped_column(VARCHAR(255), nullable=False)

    # Relationships
    workouts = relationship("Workout", back_populates="user")


class Workout(Base):
    __tablename__ = "workouts"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    date = mapped_column(Date, server_default=func.current_date())
    notes = mapped_column(Text)
    user_id = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    completed = mapped_column(Boolean, default=False)

    # Relationships
    user = relationship("User", back_populates="workouts")
    exercises = relationship(
        "Exercise", secondary="workout_exercises", back_populates="workouts"
    )


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"
    id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    workout_id = mapped_column(Integer, ForeignKey("workouts.id"),nullable=False)
    exercise_id = mapped_column(Integer, ForeignKey("exercises.id"),nullable=False)
    sets = mapped_column(Integer, nullable=False)
    weight = mapped_column(DECIMAL(5, 2), nullable=False)
    recovery_time = mapped_column(Interval, nullable=False)



class Exercise(Base):
    __tablename__ = "exercises"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    exercisename = mapped_column(VARCHAR(50), nullable=False,unique=True)
    notes = mapped_column(TEXT)

    workouts = relationship("Workout", secondary="workout_exercises", back_populates="exercises")
    categories=relationship("Categories",secondary="exercise_categories",back_populates="exercises")


class Categories(Base):
    __tablename__ = "categories"
    id = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = mapped_column(VARCHAR, nullable=False, unique=True)

    # Relationships
    exercises=relationship("Exercise",secondary="exercise_categories",back_populates="categories")


class ExerciseCategory(Base):
    __tablename__ = "exercise_categories"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    exercise_id = mapped_column(Integer, ForeignKey("exercises.id"), nullable=False)
    category_id = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)


    __table_args__ = (
        UniqueConstraint("exercise_id", "category_id", name="uix_exercise_category"),
    )

Base.metadata.create_all(engine)

# utente1=User(username="Pippolo",email="pippolo@pip.com",password_hash="asasasasasasadadad1213")
# categoria1=Categories(name="gambe")
# categoria1=session.query(Categories).filter_by(name="gambe").first()
# exercise1=Exercise(exercisename="Leg press 45")
# exercise1.categories.append(categoria1)



esercizio1search=session.query(Exercise).filter_by(exercisename="Leg press 45").first()
categoriasearch=session.query(Categories).filter_by(name="quadricipiti").first()
# esercizio1search.categories.append(categoriasearch)

exercisecategories=[category.name for category in esercizio1search.categories]

print(exercisecategories)

# exercise1=Exercise(exercisename="Leg curl seduto")

exercise2search=session.query(Exercise).filter_by(exercisename="Leg curl seduto").first()
categoria1search=session.query(Categories).filter_by(name="gambe").first()
categoria2search=session.query(Categories).filter_by(name="quadricipiti").first()



# categoria2=Categories(
#     name="femorali"
# )

# exercise1.categories.extend([categoria1search,categoria2])

# session.add_all([categoria2,exercise1])

exercisecategories2=[category.name for category in exercise2search.categories]
print(exercisecategories2)

esercizicategambe=[exercise.exercisename for exercise in categoria1search.exercises]
esercizicatquadricipiti=[exercise.exercisename for exercise in categoria2search.exercises]
print(esercizicategambe)
print(esercizicatquadricipiti)



# session.add(exercise1)



# session.add_all([utente1,categoria1])
# session.add(workout1)

#associa esercizio a workout

#crea workout: deve esssere associato ad un utente per via della FK
# workout1=Workout(
#     user_id=1,
#     notes="Leg Day test"
# )

workout2=Workout(
    user_id=1,
    notes="Chest Day test"
)

workout3=Workout(
    user_id=1,
    notes="Pull day test"
)

utente2=User(
    username="Gianluchino",email="gianlu@chino.com",password_hash="asasasasasasadadad1213"
)

workout4=Workout(
    user_id=2,
    notes="Chest day test gianluchino"
)


# exercise2=Exercise(exercisename="Chest Press")
# exercise3=Exercise(exercisename="Croci ai cavi")
# exercise4=Exercise(exercisename="Flessioni")

# categoriapetto=Categories(name="petto")

# exercise2.categories.append(categoriapetto)
# exercise3.categories.append(categoriapetto)
# exercise4.categories.append(categoriapetto)



# session.add_all([exercise2,exercise3,exercise4,categoriapetto])
workoutsgianluchino=session.scalars(select(Workout).where(Workout.user_id==2)).all()
print(workoutsgianluchino[0].notes)
# for workout in workoutsgianluchino:
#     print(workout.notes)


    
    

session.commit()

